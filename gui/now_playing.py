# UI for the now playing section.

import customtkinter as ctk

class NowPlayingCard(ctk.CTkFrame):
    def __init__(self, parent, flags):
        super().__init__(parent, corner_radius=10)

        self.flags = flags

        # Flag
        self.flag_label = ctk.CTkLabel(self, text="")
        self.flag_label.pack(side="left", padx=10, pady=10)

        # Station name
        self.station_label = ctk.CTkLabel(
            self, text="No station playing", font=("Arial", 14, "bold")
        )
        self.station_label.pack(anchor="w", padx=10)

        # Live indicator (hidden by default)
        self.live_indicator = ctk.CTkLabel(
            self, text="● LIVE",
            text_color="#FF3B30",
            font=("Arial", 14, "bold")
        )
        self.live_indicator.pack(anchor="w", padx=10)
        self.live_indicator.pack_forget()

        self.live_pulse_state = True

        # Track metadata
        self.track_label = ctk.CTkLabel(self, text="", font=("Arial", 13))
        self.track_label.pack(anchor="w", padx=10, pady=(0, 10))

        # Start pulse loop
        self.after(1000, self.pulse)

    def pulse(self):
        if self.live_indicator.winfo_ismapped():
            color = "#FF3B30" if self.live_pulse_state else "#802020"
            self.live_indicator.configure(text_color=color)
            self.live_pulse_state = not self.live_pulse_state

        self.after(1000, self.pulse)

    def update_station(self, name, country):
        self.station_label.configure(text=name)
        self.flag_label.configure(image=self.flags.get(country))
        # LIVE is NOT shown here anymore

    def clear(self):
        self.station_label.configure(text="No station playing")
        self.track_label.configure(text="")
        self.flag_label.configure(image=None)
        self.live_indicator.pack_forget()