# Controls for the UI.

import customtkinter as ctk

class Controls(ctk.CTkFrame):
    def __init__(self, parent, stop_icon, stop_callback, volume_callback):
        super().__init__(parent)

        # Stop button
        self.stop_button = ctk.CTkButton(
            self,
            text="",
            image=stop_icon,
            width=100,
            height=80,
            command=stop_callback
        )
        self.stop_button.pack(pady=10)

        # Volume slider
        self.volume_slider = ctk.CTkSlider(
            self,
            from_=0,
            to=100,
            command=volume_callback,
            width=250
        )
        self.volume_slider.set(70)
        self.volume_slider.pack(pady=10)