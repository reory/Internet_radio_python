# Main_window brings all the files together.

import customtkinter as ctk
from gui.now_playing import NowPlayingCard
from gui.station_list import StationList
from gui.controls import Controls
from gui.search_bar import SearchBar
from player.radio_player import RadioPlayer
from player.stations import load_stations
from PIL import Image
from gui.world_map import WorldMap
from gui.world_clock import WorldClock
import os

class MainWindow:
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.root = ctk.CTk()
        self.root.title("Internet Radio Made with Python")
        self.root.geometry("1000x500")

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

        # World map panel
        self.world_map = WorldMap(
            self.root, 
            image_path="assets/map/world_map.png",
            )
        self.world_map.pack(fill="x", padx=10, pady=10)
        
        # Create the clock and "glue" it to the world map label
        self.clock_widget = WorldClock(self.world_map.label)
        # Position it in the bottom-right corner of the map
        self.clock_widget.place(relx=0.97, rely=0.95, anchor="se")

        # Controls directly under the map
        self.controls = Controls(
            self.root, 
            self.load_icon("stop.png", 20),
            self.stop, 
            self.change_volume
        )
        self.controls.pack(fill="x", padx=5, pady=5)
        
        # Station list below the Controls
        self.station_list = StationList(
            self.root, self.stations, self.flags, self.play_station
        )
        self.station_list.pack(fill="both", expand=True, padx=10, pady=10)

        self.root.mainloop()

    def on_country_click(self, country):
        #print("Country clicked", country)

        # Filter the list
        self.filter_stations(country)

        # Get the filtered stations
        filtered = self.station_list.get_filtered_stations()

        if not filtered:
            print("No stations for that region:", country)
            return

        # Pick the first station
        station = filtered[0]

        # Play the StationList
        self.play_station(station)

    def play_station(self, name):
        info = self.stations[name]
        url = info["url"]

        # Try to start playback
        if not self.player.play(url):
            self.now_playing.clear()   # hides LIVE
            return

        # Playback succeeded → update UI
        self.now_playing.update_station(name, info["country"])

        # Show flag on map
        flag_img = self.flags.get(info["country"])
        
        # DEBUG PRINT
        #print("flag img", flag_img, "country", info["country"])

        self.world_map.show_flag(info["country"], flag_img)

        # World clock
        self.clock_widget.update_time(info["country"])

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
        path = os.path.join("assets", "icons", f"{country.lower()}.png")
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