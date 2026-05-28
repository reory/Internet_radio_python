# Internet radio player
# 6.1.26 (lazy VLC init, faster startup)

import os
import vlc


# Try to reduce VLC verbosity
os.environ["VLC_VERBOSE"] = "-1"


class RadioPlayer:
    def __init__(self):
        # Lazy init: don't create VLC instance yet
        self.instance: vlc.Instance | None = None 
        self.player: vlc.MediaPlayer | None = None 
        self.media: vlc.Media | None = None 

        # Add these flags to make VLC more "brave" with internet streams
        self.instance = vlc.Instance('--quiet', '--no-xlib', '--network-caching=3000')

    def _ensure_instance(self):
        """Create VLC instance and player on first use."""

        if self.instance is None:
            # Options:
            # --aout=directsound      → stable audio on Windows
            # --quiet                 → reduce logging
            # --no-plugins-cache      → avoid slow cache rebuild
            self.instance = vlc.Instance(
                "--aout=directsound",
                "--quiet",
                "--no-plugins-cache",
            )  # type: ignore

        if self.player is None:
            self.player = self.instance.media_player_new()

    def play(self, url: str) -> bool:
        """Play a radio stream from a URL. Return True if successful."""

        try:
            self._ensure_instance()

            if self.player:
                self.player.stop()

            self.media = self.instance.media_new(url)
            self.player.set_media(self.media)

            result = self.player.play()

            if result == -1:
                return False

            return True

        except Exception:
            return False

    def stop(self) -> None:
        """Stop the playback of the player."""

        if self.player:
            self.player.stop()

    def set_volume(self, volume: int) -> None:

        """Set volume (0-100)."""
        if self.player:
            volume = max(0, min(100, int(volume)))
            self.player.audio_set_volume(volume)

    def get_metadata(self):
        """Return metadata (title/artist) if available, else None."""

        if not self.media:
            return None

        try:
            self.media.parse_with_options(
                vlc.MediaParseFlag.network, timeout=0
            )
        except Exception:
            return None

        title = self.media.get_meta(vlc.Meta.Title) or ""
        artist = self.media.get_meta(vlc.Meta.Artist) or ""

        if artist and title:
            return f"{artist} - {title}"
        if title:
            return title
        if artist:
            return artist

        return None
