# Contributing to the Internet Radio (Python) Project

Thank you for your interest in contributing to the **Internet Radio** application.  
This project is built with **Python** and focuses on providing a simple, functional, and extendable internet radio player.  
Contributions of all kinds are welcome — bug fixes, new features, UI improvements, documentation, refactoring, and architectural enhancements.

---

## 🧱 Project Overview

The Internet Radio project aims to:

- Provide a lightweight Python-based radio player  
- Stream online radio stations  
- Offer a simple and clean user interface  
- Allow easy extension for playlists, favourites, metadata, and more  

Understanding the structure will help you contribute effectively.

---

## 📁 Project Structure

Although the structure may evolve, the typical layout includes:

- `main.py` — Application entry point  
- `radio_player/` — Core playback logic  
- `ui/` — User interface components (if applicable)  
- `stations/` — Station lists, presets, or configuration files  
- `utils/` — Helper functions and shared utilities  

If your contribution affects multiple layers, keep responsibilities separated and avoid mixing UI, logic, and configuration.

---

## 🛠️ How to Contribute

### 1. Fork the repository

```bash
git clone https://github.com/<your-username>/Internet_radio_python.git
cd Internet_radio_python
```

### 2. Create a feature branch

```bash
git checkout -b feature/add-new-station-list
```

### 3. Follow the project’s conventions

- Keep functions small and focused  
- Use clear naming  
- Avoid unnecessary complexity  
- Keep UI and playback logic separate  
- Document new functions or modules  

### 4. Run the project locally

```bash
python main.py
```

### 5. Write clean, typed, documented code

- Use type hints where appropriate  
- Add inline comments when logic is non-obvious  
- Follow existing formatting and style  
- Avoid introducing global state  

### 6. Add or update tests (if applicable)

If you add new logic, consider adding tests to ensure stability.

### 7. Commit with clear messages

```bash
git commit -m "Add support for station metadata parsing"
```

### 8. Push and open a Pull Request

```bash
git push origin feature/add-new-station-list
```

Then open a PR on GitHub with:

- A clear description of your changes  
- Screenshots (if UI changes)  
- Notes on design decisions  

---

## 🧪 Code Style & Quality

### Python

- Use type hints where possible  
- Keep functions pure unless side effects are required  
- Prefer modular design  
- Avoid duplicating logic  

### Audio / Streaming Logic

- Ensure streams are handled cleanly  
- Avoid blocking the UI (if applicable)  
- Handle connection errors gracefully  

### UI (if present)

- Keep UI code simple  
- Avoid mixing playback logic into UI components  
- Keep layout readable and maintainable  

---

## 🧩 Adding New Features

When adding a new feature:

1. Keep it modular  
2. Place new logic in the appropriate folder  
3. Avoid breaking existing functionality  
4. Document how the feature works  
5. Update README if needed  

---

## 🧹 Pull Request Checklist

Before submitting a PR, ensure:

- [ ] Code runs without errors  
- [ ] No obvious linter warnings  
- [ ] Type hints are correct  
- [ ] No unnecessary complexity  
- [ ] New files follow naming conventions  
- [ ] PR description explains the change clearly  

---

## 🤝 Code of Conduct

Be respectful, constructive, and collaborative.  
I welcome contributors of all experience levels.

---

## 📬 Need Help?

If you're unsure where to start, feel free to open an **Issue** or **Discussion**.  
I'd be happy to guide you through your first contribution.
