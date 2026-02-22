# 🗺️ Project Roadmap: Internet Radio Python

This document outlines the planned features and technical milestones for the evolution of this application.

## 🟢 Phase 1: Data & Performance (Current Focus)
- [ ] **DuckDB Integration:** Migrate from `stations.json` to a high-performance DuckDB local database.
- [ ] **Search Optimization:** Implement full-text search across the database for instantaneous station filtering.
- [ ] **Data Persistence:** Store user preferences and "Recently Played" history locally.

## 🟡 Phase 2: User Experience (UX)
- [ ] **Favorites System:** Allow users to "Heart" stations and access them via a dedicated tab.
- [ ] **Buffering Feedback:** Visual progress indicator to show stream connection status.
- [ ] **Mini-Player Mode:** A compact UI view for background listening.

## 🔴 Phase 3: Advanced Features
- [ ] **World Map Discovery:** Integration with Folium/CustomTkinter to select stations via a global map.
- [ ] **Radio-Browser API:** Real-time synchronization with the Open Source Radio Browser database (30k+ stations).
- [ ] **Stream Recording:** Capability to save live broadcasts to local MP3 files.

## 🛠️ Technical Debt & Stability
- [ ] Improve VLC error handling for missing DLLs.
- [ ] Implement asynchronous stream loading to prevent UI freezing on slow connections.