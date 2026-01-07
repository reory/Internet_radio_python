# Main_window brings all the files together.

import customtkinter as ctk
from gui.now_playing import NowPlayingCard
from gui.station_list import StationList
from gui.controls import Controls
from gui.search_bar import SearchBar
from player.radio_player import RadioPlayer
from player.stations import load_stations
from PIL import Image
import os

class MainWindow:
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.root = ctk.CTk()
        self.root.title("Internet Radio Made with Python")
        self.root.geometry("500x600")

        self.player = RadioPlayer()
        self.stations = load_stations()

        # Load flags
        self.flags = {}
        for name, info in self.stations.items():
            country = info["country"]
            if country not in self.flags:
                self.flags[country] = self.load_flag(country)

        # Now Playing card
        self.now_playing = NowPlayingCard(self.root, self.flags)
        self.now_playing.pack(fill="x", padx=10, pady=10)

        # Search bar
        self.search_bar = SearchBar(self.root, self.filter_stations)
        self.search_bar.pack(fill="x", padx=10, pady=5)

        # Station list
        self.station_list = StationList(
            self.root, self.stations, self.flags, self.play_station
        )
        self.station_list.pack(fill="both", expand=True, padx=10, pady=10)

        # Controls
        stop_icon = self.load_icon("stop.png", 48)
        self.controls = Controls(
            self.root, stop_icon, self.stop, self.change_volume
        )
        self.controls.pack(pady=10)

        self.root.mainloop()

    def play_station(self, name):
        info = self.stations[name]
        url = info["url"]

        # Try to start playback
        if not self.player.play(url):
            self.now_playing.clear()   # hides LIVE
            return

        # Playback succeeded → update UI
        self.now_playing.update_station(name, info["country"])

        # Apply live indicator
        self.now_playing.live_indicator.pack(anchor="w", padx=10)

        # Apply current volume
        self.player.set_volume(int(self.controls.volume_slider.get()))

        # Begin metadata polling
        self.update_metadata()

    def stop(self):
        self.player.stop()
        self.now_playing.clear()

    def change_volume(self, value):
        self.player.set_volume(int(value))

    def update_metadata(self):
        metadata = self.player.get_metadata()
        self.now_playing.track_label.configure(
            text=f"Track: {metadata}" if metadata else ""
        )
        self.root.after(1000, self.update_metadata)

    def load_flag(self, country):
        path = os.path.join("assets", "icons", f"{country}.png")
        if os.path.exists(path):
            img = Image.open(path)
            return ctk.CTkImage(light_image=img, dark_image=img, size=(20, 20))
        return None

    def load_icon(self, filename, size):
        path = os.path.join("assets", "icons", filename)
        img = Image.open(path).resize((size, size))
        return ctk.CTkImage(light_image=img, dark_image=img, size=(size, size))
    
    def filter_stations(self, query):
        if not isinstance(query, str):
            return 
        self.station_list.filter(query)