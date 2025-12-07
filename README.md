# Orange TV Viewer for KDE Plasma 6 (Qt6)

A native KDE Plasma 6/Qt6 application to view Orange TV live programs.
Optimized for Fedora 43 KDE Edition with Plasma 6.5+.

## Installation on Fedora 43 KDE Edition

### One command Installation

```bash
cd ~/Downloads/ && sudo dnf install python3-pyqt6 python3-pyqt6-webengine -y && git clone https://github.com/alduccino/Orange-TV.git && cd Orange-TV && chmod +x install.sh && ./install.sh
```

## Step by step Installation.

### 1. Install Dependencies

```bash
sudo dnf install python3-pyqt6 python3-pyqt6-webengine
```

### 2. Make the script executable

```bash
chmod +x orange-tv-viewer-qt6.py
```

### 3. Run the application

```bash
./orange-tv-viewer-qt6.py
```

### 4. Optional: Install system-wide

To install system-wide and add to application menu:

```bash
# Copy the script to /usr/local/bin
sudo cp orange-tv-viewer-qt6.py /usr/local/bin/orange-tv-viewer
sudo chmod +x /usr/local/bin/orange-tv-viewer

# Copy the desktop entry
sudo cp orange-tv-viewer.desktop /usr/share/applications/

# Update desktop database
sudo update-desktop-database
```

After this, you can launch "Orange TV Viewer" from your KDE Plasma application menu.

## Features

- **Native Qt6/KDE Plasma 6 interface** - Built specifically for the latest KDE
- **Full keyboard shortcuts** - Standard KDE shortcuts (Ctrl+Q, F11, Ctrl+H, etc.)
- **Web browser controls** - Back, forward, reload, home, stop
- **Fullscreen mode** - Native fullscreen support including web-initiated fullscreen
- **Zoom controls** - Zoom in/out/reset with keyboard shortcuts
- **Breeze integration** - Automatic theme integration with KDE Plasma 6
- **Modern web engine** - Based on Chromium via Qt6 WebEngine

## Keyboard Shortcuts

- **Alt+Left / Backspace** - Go back
- **Alt+Right** - Go forward
- **F5 / Ctrl+R** - Reload page
- **Ctrl+H** - Go to home page
- **F11** - Toggle fullscreen
- **Ctrl++** - Zoom in
- **Ctrl+-** - Zoom out
- **Ctrl+0** - Reset zoom
- **Ctrl+Q** - Quit application
- **Esc** - Exit fullscreen / Stop loading

## Usage

- Use the toolbar buttons or keyboard shortcuts to navigate
- The home button returns you to the main Orange TV programs page
- Video playback is fully supported with autoplay enabled
- Web-initiated fullscreen (from video players) is supported

## System Requirements

- Fedora 43 (or newer) with KDE Plasma 6.5+
- Python 3.11+
- PyQt6
- Qt6 WebEngine

## Why Qt6?

This version is specifically built for KDE Plasma 6, which is based on Qt6 framework.
Qt6 provides:
- Better performance and modern features
- Native Wayland support
- Improved security
- Full compatibility with KDE Plasma 6's Breeze theme
- Modern Chromium-based web engine
