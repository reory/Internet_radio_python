import sys
from unittest.mock import MagicMock


class DummyFrame:
    def __init__(self, *args, **kwargs):
        pass

    def pack(self, *args, **kwargs):
        pass

    def grid(self, *args, **kwargs):
        pass

    def place(self, *args, **kwargs):
        pass


class DummyScrollableFrame(DummyFrame):
    pass


class DummyEntry:
    def __init__(self, *args, **kwargs):
        self.bind = MagicMock()
        self.get = MagicMock(return_value="")
        self.pack = MagicMock()


mock_ctk = MagicMock()

mock_ctk.CTk = DummyFrame
mock_ctk.CTkFrame = DummyFrame
mock_ctk.CTkScrollableFrame = DummyScrollableFrame

mock_ctk.CTkLabel = MagicMock
mock_ctk.CTkButton = MagicMock
mock_ctk.CTkEntry = DummyEntry

mock_ctk.CTkImage = MagicMock

mock_ctk.set_appearance_mode = MagicMock()
mock_ctk.set_default_color_theme = MagicMock()

sys.modules["customtkinter"] = mock_ctk
