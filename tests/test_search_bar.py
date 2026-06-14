from unittest.mock import MagicMock
from gui.search_bar import SearchBar


def test_search_triggers_callback():
    parent = MagicMock()
    on_search = MagicMock()

    widget = SearchBar(parent, on_search)

    # Override DummyEntry.get() return value
    widget.entry.get.return_value = "  Rock FM  "

    widget._search()

    on_search.assert_called_once_with("rock fm")


def test_search_empty_string():
    parent = MagicMock()
    on_search = MagicMock()

    widget = SearchBar(parent, on_search)

    widget.entry.get.return_value = "   "

    widget._search()

    on_search.assert_called_once_with("")


def test_bind_called():
    parent = MagicMock()
    on_search = MagicMock()

    widget = SearchBar(parent, on_search)

    # DummyEntry.bind is a MagicMock created in conftest.py
    widget.entry.bind.assert_called_once_with("<KeyRelease>", widget._search)
