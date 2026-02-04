import pytest
from unittest.mock import MagicMock, patch
import sys

# Mock customtkinter BEFORE importing SearchBar
class DummyFrame:
    def __init__(self, *args, **kwargs):
        pass

mock_ctk = MagicMock()
mock_ctk.CTkFrame = DummyFrame
mock_ctk.CTkEntry = MagicMock()

# Inject into sys.modules so import uses the mock
sys.modules["customtkinter"] = mock_ctk

from gui.search_bar import SearchBar



# TEST: typing triggers callback
def test_search_triggers_callback():
    # Mock entry instance
    mock_entry_instance = MagicMock()
    mock_entry_instance.get.return_value = "  Rock FM  "

    # Make CTkEntry return our mock instance
    mock_ctk.CTkEntry.return_value = mock_entry_instance

    on_search = MagicMock()
    parent = MagicMock()

    widget = SearchBar(parent, on_search)

    # Simulate key release event
    widget._search()

    on_search.assert_called_once_with("rock fm")


# TEST: empty input
def test_search_empty_string():
    mock_entry_instance = MagicMock()
    mock_entry_instance.get.return_value = "   "

    mock_ctk.CTkEntry.return_value = mock_entry_instance

    on_search = MagicMock()
    parent = MagicMock()

    widget = SearchBar(parent, on_search)

    widget._search()

    on_search.assert_called_once_with("")



# TEST: bind is called correctly
def test_bind_called():
    mock_entry_instance = MagicMock()
    mock_ctk.CTkEntry.return_value = mock_entry_instance

    on_search = MagicMock()
    parent = MagicMock()

    widget = SearchBar(parent, on_search)

    mock_entry_instance.bind.assert_called_once_with("<KeyRelease>", widget._search)
