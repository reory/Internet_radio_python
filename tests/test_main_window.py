import pytest  # noqa
from unittest.mock import MagicMock
from gui.main_window import MainWindow  # noqa


def test_on_country_click_no_results(monkeypatch):
    mw = MainWindow.__new__(MainWindow)  # bypass __init__
    mw.filter_stations = MagicMock()
    mw.station_list = MagicMock()
    mw.station_list.get_filtered_stations.return_value = []

    mw.play_station = MagicMock()

    mw.on_country_click("US")

    mw.play_station.assert_not_called()


def test_on_country_click_plays_first(monkeypatch):
    mw = MainWindow.__new__(MainWindow)
    mw.filter_stations = MagicMock()
    mw.station_list = MagicMock()
    mw.station_list.get_filtered_stations.return_value = ["Rock FM", "Jazz FM"]

    mw.play_station = MagicMock()

    mw.on_country_click("US")

    mw.play_station.assert_called_once_with("Rock FM")


def test_play_station_failure(monkeypatch):
    mw = MainWindow.__new__(MainWindow)
    mw.stations = {"Rock FM": {"url": "http://example.com", "country": "US"}}

    mw.player = MagicMock()
    mw.player.play.return_value = False

    mw.now_playing = MagicMock()
    mw.world_map = MagicMock()
    mw.clock_widget = MagicMock()
    mw.controls = MagicMock()
    mw.controls.volume_slider.get.return_value = 50

    mw.update_metadata = MagicMock()

    mw.play_station("Rock FM")

    mw.now_playing.clear.assert_called_once()


def test_play_station_success(monkeypatch):
    mw = MainWindow.__new__(MainWindow)
    mw.stations = {"Rock FM": {"url": "http://example.com", "country": "US"}}

    mw.player = MagicMock()
    mw.player.play.return_value = True

    mw.now_playing = MagicMock()
    mw.world_map = MagicMock()
    mw.clock_widget = MagicMock()
    mw.controls = MagicMock()
    mw.controls.volume_slider.get.return_value = 30

    mw.flags = {"US": MagicMock()}
    mw.update_metadata = MagicMock()

    mw.play_station("Rock FM")

    mw.now_playing.update_station.assert_called_once()
    mw.world_map.show_flag.assert_called_once()
    mw.clock_widget.update_time.assert_called_once()
    mw.player.set_volume.assert_called_once_with(30)
    mw.update_metadata.assert_called_once()


def test_stop():
    mw = MainWindow.__new__(MainWindow)
    mw.player = MagicMock()
    mw.now_playing = MagicMock()

    mw.stop()

    mw.player.stop.assert_called_once()
    mw.now_playing.clear.assert_called_once()


def test_change_volume():
    mw = MainWindow.__new__(MainWindow)
    mw.player = MagicMock()

    mw.change_volume("42")

    mw.player.set_volume.assert_called_once_with(42)


def test_filter_stations_calls_list_filter():
    mw = MainWindow.__new__(MainWindow)
    mw.station_list = MagicMock()

    mw.filter_stations("rock")

    mw.station_list.filter.assert_called_once_with("rock")


def test_filter_stations_non_string():
    mw = MainWindow.__new__(MainWindow)
    mw.station_list = MagicMock()

    mw.filter_stations(None)

    mw.station_list.filter.assert_not_called()
