# UI for the scrollable station list using CTkScrollableFrame.

import customtkinter as ctk
from PIL import Image

class StationList(ctk.CTkScrollableFrame):
    def __init__(self, parent, stations, flags, play_callback):
        super().__init__(parent, width=450, height=300)

        self.stations = stations
        self.flags = flags
        self.play_callback = play_callback

        self.rows = {} # Store row widgets.
        
        # Track which stations are currently visible
        self.filtered_stations = list(stations.keys())

        self.build_list(stations)

    def on_station_click(self, station_data):
        country_code = station_data.get("country_code", "").lower()

        # Get the flag image
        try:
            path = f"assets/icons/{country_code}.png"
            img = Image.open(path)
            ctk_flag = ctk.CTkImage(light_image=img, dark_image=img, size=(20, 15))

            # Tell the map to show the icons
            self.master.world_map.show_flag(country_code, ctk_flag)
        except Exception as e:
            print(f"Could not load flag for {country_code}: {e}")

    def build_list(self, stations):

        # Clear exisiting rows
        for row in self.rows.values():
            row.destroy()
        self.rows.clear()

        # Build new rows
        for name, info in stations.items():
            row = self._create_row(name, info)
            self.rows[name] = row

    def _create_row(self, station_name, info):
        row = ctk.CTkFrame(self)
        row.pack(fill="x", pady=10, padx=20)

        # Flag
        flag_img = self.flags.get(info["country"])
        if flag_img:
            ctk.CTkLabel(row, image=flag_img, text="").pack(side="left", padx=5)

        # Station name + category
        text = f"{station_name} ({info['category']})"
        ctk.CTkLabel(row, text=text).pack(side="left", padx=5)

        # Play button
        ctk.CTkButton(
            row,
            text="Play",
            width=60,
            command=lambda: self.play_callback(station_name)
        ).pack(side="right", padx=10)

        return row
    
        # A filter query method - instant show and hide of rows.
    def filter(self, query):
        if not isinstance(query, str):
            return

        query = query.lower()
        self.filtered_stations = []

        for name, row in self.rows.items():
            if query in name.lower():
                row.pack(fill="x", pady=10, padx=20)
                self.filtered_stations.append(name)
            else:
                row.pack_forget()

    # Return the list of currently visible stations 
    def get_filtered_stations(self):
        return self.filtered_stations