import customtkinter as ctk
from datetime import datetime
import pytz

class WorldClock(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # A dictionary mapping your country codes to timezone strings
        self.tz_map = {
            "aus": "Australia/Sydney",
            "br": "America/Sao_Paulo",
            "can": "America/Toronto",
            "ch": "Europe/Zurich",
            "chi": "Asia/Shanghai",
            "es": "Europe/Madrid",
            "fr": "Europe/Paris",
            "it": "Europe/Rome",
            "ind": "Asia/Kolkata",
            "ngr": "Africa/Lagos",
            "pl": "Europe/Warsaw",
            "sa": "Africa/Johannesburg",
            "us": "America/New_York",
            "uk": "Europe/London"
        }

        self.time_label = ctk.CTkLabel(
            self,
            text="--:--",
            font=("Arial", 14, "bold")
        )
        self.time_label.pack(pady=5)

        self.location_label = ctk.CTkLabel(
            self, 
            text="Select a country",
            font=("Arial", 12)
        )
        self.location_label.pack()

    def update_time(self, country_code):

        code = country_code.lower()
        if code in self.tz_map:
            timezone = pytz.timezone(self.tz_map[code])
            now = datetime.now(timezone)
            self.time_label.configure(text=now.strftime("%H:%M"))
            self.location_label.configure(text=f"Local Time: {code.upper()}")