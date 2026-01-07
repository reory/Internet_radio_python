import customtkinter as ctk

class SearchBar(ctk.CTkFrame):
    def __init__(self, parent, on_search):
        super().__init__(parent) # filtering logic left to the parent file.

        self.on_search = on_search

        # Renders a search box 

        self.entry = ctk.CTkEntry(
            self,
            placeholder_text="Search stations..",
            width=300
        )
        self.entry.pack(side="left", padx=10, pady=10)

        # Bind key release to live search
        self.entry.bind("<KeyRelease>", self._search)
    
        # Calls on search query whenever a user types in the search box.
    def _search(self, event=None):
        query = self.entry.get().strip().lower()
        self.on_search(query)