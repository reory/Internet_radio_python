![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Repo Size](https://img.shields.io/github/repo-size/reory/Internet_radio_python)
![Last Commit](https://img.shields.io/github/last-commit/reory/Internet_radio_python)
![Stars](https://img.shields.io/github/stars/reory/Internet_radio_python?style=social)

# 🎵 Internet Radio Player
### Powered by Python, CustomTkinter, and VLC

A modern, modular Internet Radio application built with **Python**, **CustomTkinter**, and **python-vlc**. This project features a clean UI, live metadata updates, and a modular architecture designed for easy expansion.

---

## 🚀 Features

- **Global Streaming:** Play hundreds of online radio stations.
- **Live Metadata:** Real-time updates for track titles and artist info.
- **Smart Search:** Instant station filtering via the search bar.
- **Visual Cues:** Country flags and "Now Playing" live indicators.
- **User Control:** Integrated volume slider and stop functionality.
- **Modular Design:** Clean separation between GUI components and player logic.

---
### 🖥️ Main Window interface
![Main Window](assets/screenshots/main_.window.png)

### 🎵 Feature Gallery
| Now Playing Card | Station List | Search Bar |
| :--- | :--- | :--- |
| ![Now Playing](assets/screenshots/now_playing.png) | ![Station List](assets/screenshots/station_list.png) | ![Search Bar](assets/screenshots/search_bar.png) |

---

## 🧩 Project Structure

```text
internet_radio/
├── app.py                 # Main entry point
├── requirements.txt       # Python dependencies
├── gui/                   # CustomTkinter UI Components
│   ├── main_window.py
│   ├── now_playing.py
│   ├── station_list.py
│   ├── controls.py
│   └── search_bar.py
├── player/                # Media Engine & Data
│   ├── radio_player.py
│   └── stations.json
└── assets/                # Media & Icons
    └── icons/
```

---

## 📦 Installation

1. **Clone the repository and install:**
```bash
git clone https://github.com/reory/Internet_radio_python.git
cd Internet_radio_python
pip install -r requirements.txt
```

---
> [!IMPORTANT]
> This app requires the VLC media player (64-bit) installed on your system to function.
> **DOWNLOAD VLC here [here](https://www.videolan.org/vlc/)**

---

## Usage

This project requires both the backend and frontend to be running simultaneously.

1. **Run the app:** 
   ```bash
    python app.py
    ```

---

## Testing🚦
The project includes a comprehensive suite of 4 tests covering radio searches, radio player, and the radio UI logic.

To run the tests:
```bash
pytest
```

---

## 🗺️ Future Plans & Roadmap
I am currently working on scaling this project. Planned features include:

- DuckDB Backend: Migrating stations.json to a high-performance database.

- Geospatial Discovery: Interactive map for station selection.

- Graphic Equalizer: Advanced audio frequency control.

---

## 🤝 Contributing
Contributions, ideas, and feedback are welcome! This is my first public project, so constructive feedback is especially appreciated as the app continues to grow.

- Fork the repository.

- Create a new branch (git checkout -b feature/YourFeature).

- Commit your changes.

- Submit a Pull Request.

---

## Notes
- Version 1.0 Initial release. 
- 4 passing unit tests. 

**Built by Roy Peters** — [Click here for contact info😁](https://www.linkedin.com/in/roy-p-74980b382/)
