import pytest
from unittest.mock import MagicMock, patch
from player.radio_player import RadioPlayer

# PLAY TESTS

@patch("player.radio_player.vlc")
def test_play_success(mock_vlc):
    mock_instance = MagicMock()
    mock_media = MagicMock()
    mock_player = MagicMock()

    mock_vlc.Instance.return_value = mock_instance
    mock_instance.media_new.return_value = mock_media
    mock_instance.media_player_new.return_value = mock_player
    mock_player.play.return_value = 0  # VLC success

    rp = RadioPlayer()
    result = rp.play("http://example.com/stream")

    assert result is True
    mock_player.set_media.assert_called_with(mock_media)
    mock_player.play.assert_called_once()


@patch("player.radio_player.vlc")
def test_play_failure(mock_vlc):
    mock_instance = MagicMock()
    mock_media = MagicMock()
    mock_player = MagicMock()

    mock_vlc.Instance.return_value = mock_instance
    mock_instance.media_new.return_value = mock_media
    mock_instance.media_player_new.return_value = mock_player
    mock_player.play.return_value = -1  # VLC failure

    rp = RadioPlayer()
    result = rp.play("http://example.com/stream")

    assert result is False


# STOP TEST

def test_stop_calls_player_stop():
    rp = RadioPlayer()
    rp.player = MagicMock()

    rp.stop()

    rp.player.stop.assert_called_once()


# VOLUME TEST

def test_set_volume():
    rp = RadioPlayer()
    rp.player = MagicMock()

    rp.set_volume(55)

    rp.player.audio_set_volume.assert_called_with(55)


# METADATA TESTS

@patch("player.radio_player.vlc")
def test_metadata_artist_title(mock_vlc):
    rp = RadioPlayer()
    rp.media = MagicMock()

    rp.media.get_meta.side_effect = [
        "Song Title",   # Title
        "Artist Name"   # Artist
    ]

    result = rp.get_metadata()
    assert result == "Artist Name - Song Title"


@patch("player.radio_player.vlc")
def test_metadata_title_only(mock_vlc):
    rp = RadioPlayer()
    rp.media = MagicMock()

    rp.media.get_meta.side_effect = [
        "Only Title",  # Title
        ""             # Artist
    ]

    assert rp.get_metadata() == "Only Title"


@patch("player.radio_player.vlc")
def test_metadata_artist_only(mock_vlc):
    rp = RadioPlayer()
    rp.media = MagicMock()

    rp.media.get_meta.side_effect = [
        "",             # Title
        "Only Artist"   # Artist
    ]

    assert rp.get_metadata() == "Only Artist"


@patch("player.radio_player.vlc")
def test_metadata_none(mock_vlc):
    rp = RadioPlayer()
    rp.media = MagicMock()

    rp.media.get_meta.side_effect = ["", ""]

    assert rp.get_metadata() is None


def test_metadata_no_media():
    rp = RadioPlayer()
    rp.media = None

    assert rp.get_metadata() is None


@patch("player.radio_player.vlc")
def test_metadata_parse_failure(mock_vlc):
    rp = RadioPlayer()
    rp.media = MagicMock()

    rp.media.parse_with_options.side_effect = Exception("parse error")

    assert rp.get_metadata() is None
