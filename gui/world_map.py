import customtkinter as ctk
from PIL import Image

class WorldMap(ctk.CTkFrame):
    def __init__(self, parent, image_path="assets/map/world_map.png"):
        super().__init__(parent)
        
        self.configure(width=750, height=150)

        # Store original image for resizing
        self.original_img = Image.open(image_path)
        self.map_image = ctk.CTkImage(
            light_image=self.original_img,
            dark_image=self.original_img,
            size=(750, 150)
        )

        self.label = ctk.CTkLabel(self, image=self.map_image, text="")
        self.pack_propagate(False)
        self.label.pack(expand=True, fill="both")

        self.flag_label = ctk.CTkLabel(self.label, text="", fg_color="transparent")
        self.flag_label.place(x=0, y=0)

        self.country_points = {
            "aus": (0.965, 0.782),
            "br": (0.258, 0.720),
            "can": (0.066, 0.053),
            "ch": (0.456, 0.218),
            "chi": (0.924, 0.182),
            "es": (0.421, 0.276),
            "fr": (0.446, 0.236),
            "it": (0.494, 0.253),
            "ind": (0.750, 0.444),
            "ngr": (0.450, 0.524),
            "pl": (0.483, 0.204),
            "sa": (0.527, 0.796),
            "us": (0.074, 0.227),
            "uk": (0.439, 0.151), 
        }

        # Resize the CTkImage when the label resizes
        self.label.bind("<Configure>", self._on_resize)

        self.label.bind("<Button-1>", lambda e: print(
            f"Click Percentages -> x: {e.x/self.label.winfo_width():.3f}, y: {e.y/self.label.winfo_height():.3f}"
        ))

    def _on_resize(self, event):
        
        # Keep the image in sync with the actual label dimensions
        self.map_image.configure(size=(event.width, event.height))

    def show_flag(self, country, flag_image):
        country = country.lower()

        if country not in self.country_points:
            return

        relx, rely = self.country_points[country]

        self.flag_label.configure(image=flag_image)
        self.flag_label.image = flag_image

        self.flag_label.place(relx=relx, rely=rely, anchor="center")
        self.flag_label.lift()