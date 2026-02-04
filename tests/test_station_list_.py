import pytest
from unittest.mock import MagicMock, patch
import sys

# Mock customtkinter module before importing station_list
class DummyScrollableFrame:
    def __init__(self, *args, **kwargs):
        pass

# Create a mock customtkinter module
mock_ctk = MagicMock()
mock_ctk.CTkScrollableFrame = DummyScrollableFrame
mock_ctk.CTkFrame = MagicMock
mock_ctk.CTkLabel = MagicMock
mock_ctk.CTkButton = MagicMock

sys.modules['customtkinter'] = mock_ctk

from gui.station_list import StationList


# FIXTURE: fake stations + flags
@pytest.fixture
def sample_stations():
    return {
        "Rock FM": {"category": "Rock", "country": "US"},
        "Jazz FM": {"category": "Jazz", "country": "UK"},
    }


@pytest.fixture
def sample_flags():
    return {
        "US": MagicMock(name="US_flag"),
        "UK": MagicMock(name="UK_flag"),
    }


# TEST: build_list creates rows
def test_build_list_creates_rows(sample_stations, sample_flags):
    # Create mocks that return properly configured instances
    mock_frame_instance = MagicMock()
    mock_frame_instance.pack = MagicMock()
    mock_frame_instance.pack_forget = MagicMock()
    mock_frame_instance.destroy = MagicMock()
    
    mock_frame_class = MagicMock(return_value=mock_frame_instance)
    mock_label_class = MagicMock()
    mock_button_class = MagicMock()
    
    with patch("gui.station_list.ctk.CTkFrame", mock_frame_class), \
         patch("gui.station_list.ctk.CTkLabel", mock_label_class), \
         patch("gui.station_list.ctk.CTkButton", mock_button_class):
        
        parent = MagicMock()
        play_callback = MagicMock()

        widget = StationList(parent, sample_stations, sample_flags, play_callback)

        # Should create one row per station
        assert len(widget.rows) == 2
        assert "Rock FM" in widget.rows
        assert "Jazz FM" in widget.rows


# TEST: play button callback
def test_play_button_calls_callback(sample_stations, sample_flags):
    # Create mocks that return properly configured instances
    mock_frame_instance = MagicMock()
    mock_frame_instance.pack = MagicMock()
    mock_frame_instance.pack_forget = MagicMock()
    mock_frame_instance.destroy = MagicMock()
    
    mock_frame_class = MagicMock(return_value=mock_frame_instance)
    mock_label_class = MagicMock()
    mock_button_class = MagicMock()
    
    with patch("gui.station_list.ctk.CTkFrame", mock_frame_class), \
         patch("gui.station_list.ctk.CTkLabel", mock_label_class), \
         patch("gui.station_list.ctk.CTkButton", mock_button_class):
        
        parent = MagicMock()
        play_callback = MagicMock()

        widget = StationList(parent, sample_stations, sample_flags, play_callback)

        # Grab the first created button's command
        # mock_ctk.CTkButton was called with command=lambda: play_callback(name)
        command = mock_button_class.call_args_list[0].kwargs["command"]
       
        # Simulate clicking the button
        command()

        play_callback.assert_called_once_with("Rock FM")


# TEST: filter() hides/shows rows
def test_filter_logic(sample_stations, sample_flags):
    # Track created frame instances
    frame_instances = []
    
    def create_frame_instance(*args, **kwargs):
        instance = MagicMock()
        instance.pack = MagicMock()
        instance.pack_forget = MagicMock()
        instance.destroy = MagicMock()
        frame_instances.append(instance)
        return instance
    
    mock_frame_class = MagicMock(side_effect=create_frame_instance)
    mock_label_class = MagicMock()
    mock_button_class = MagicMock()
    
    with patch("gui.station_list.ctk.CTkFrame", mock_frame_class), \
         patch("gui.station_list.ctk.CTkLabel", mock_label_class), \
         patch("gui.station_list.ctk.CTkButton", mock_button_class):
        
        parent = MagicMock()
        play_callback = MagicMock()

        widget = StationList(parent, sample_stations, sample_flags, play_callback)

        # Each row is a mocked CTkFrame
        row_rock = widget.rows["Rock FM"]
        row_jazz = widget.rows["Jazz FM"]

        # Reset mock call history
        row_rock.pack.reset_mock()
        row_rock.pack_forget.reset_mock()
        row_jazz.pack.reset_mock()
        row_jazz.pack_forget.reset_mock()

        # Filter for "rock"
        widget.filter("rock")

        row_rock.pack.assert_called_once()
        row_jazz.pack_forget.assert_called_once()

        # Filter for "jazz"
        row_rock.pack.reset_mock()
        row_rock.pack_forget.reset_mock()
        row_jazz.pack.reset_mock()
        row_jazz.pack_forget.reset_mock()

        widget.filter("jazz")

        row_jazz.pack.assert_called_once()
        row_rock.pack_forget.assert_called_once()


# TEST: filter ignores non-string
def test_filter_non_string(sample_stations, sample_flags):
    # Track created frame instances
    frame_instances = []
    
    def create_frame_instance(*args, **kwargs):
        instance = MagicMock()
        instance.pack = MagicMock()
        instance.pack_forget = MagicMock()
        instance.destroy = MagicMock()
        frame_instances.append(instance)
        return instance
    
    mock_frame_class = MagicMock(side_effect=create_frame_instance)
    mock_label_class = MagicMock()
    mock_button_class = MagicMock()
    
    with patch("gui.station_list.ctk.CTkFrame", mock_frame_class), \
         patch("gui.station_list.ctk.CTkLabel", mock_label_class), \
         patch("gui.station_list.ctk.CTkButton", mock_button_class):
        
        parent = MagicMock()
        play_callback = MagicMock()

        widget = StationList(parent, sample_stations, sample_flags, play_callback)

        # Reset call counts after creation
        for instance in frame_instances:
            instance.pack.reset_mock()
            instance.pack_forget.reset_mock()

        # Ensure no crash and no calls
        widget.filter(None)

        for row in widget.rows.values():
            row.pack.assert_not_called()
            row.pack_forget.assert_not_called()
