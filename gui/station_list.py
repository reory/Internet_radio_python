# UI for the scrollable station list using CTkScrollableFrame.

import customtkinter as ctk

class StationList(ctk.CTkScrollableFrame):
    def __init__(self, parent, stations, flags, play_callback):
        super().__init__(parent, width=450, height=300)

        self.stations = stations
        self.flags = flags
        self.play_callback = play_callback

        self.rows = {} # Store row widgets.

        self.build_list(stations)

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
        for name, row in self.rows.items():
            if query in name.lower():
                row.pack(fill="x", pady=10, padx=20)
            else:
                row.pack_forget()