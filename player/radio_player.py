# Internet radio player
# 6.1.26

import vlc

class RadioPlayer:
    def __init__(self):
        self.player = None
        self.media = None

    def play(self, url: str):
        """Play a radio stream from a URL. Return true if successful."""
        try:
            if self.player:
                self.player.stop()

            instance:  vlc.Instance = vlc.Instance()
            self.media = instance.media_new(url)
            self.player = instance.media_player_new()
            self.player.set_media(self.media)
            result = self.player.play()

            # VLC returns -1 on failure.

            if result == -1:
                return False
            
            return True
        
        except Exception:
            return False

    def stop(self):
        """Stop the playback of the player."""
        if self.player:
            self.player.stop()

    def set_volume(self, volume: int): # int a string must be numbers
        """Set volume (0-100)."""
        if self.player:
            self.player.audio_set_volume(volume)
    
    def get_metadata(self):
        """Return metadata (title/artist) if available."""
        if not self.media:
            return None

        # Ask VLC to parse metadata (non-blocking)
        try:
            self.media.parse_with_options(vlc.MediaParseFlag.network, timeout=0)
        except Exception:
            return None

        # Always define variables to avoid NameError
        title = self.media.get_meta(vlc.Meta.Title) or ""
        artist = self.media.get_meta(vlc.Meta.Artist) or ""

        if artist and title:
            return f"{artist} - {title}"
        if title:
            return title
        elif artist:
            return artist
        return None