#!/bin/bash
# Installation script for Orange TV Viewer (Qt6 version for KDE Plasma 6)

echo "=========================================="
echo "Orange TV Viewer Installation Script"
echo "For Fedora 43 KDE Edition (Plasma 6.5+)"
echo "=========================================="
echo

# Check if running on Fedora
if ! grep -q "Fedora" /etc/os-release 2>/dev/null; then
    echo "Warning: This script is designed for Fedora Linux"
    read -p "Do you want to continue anyway? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Install dependencies
echo "Step 1: Installing dependencies..."
echo "This requires sudo privileges."
sudo dnf install -y python3-pyqt6 python3-pyqt6-webengine

if [ $? -ne 0 ]; then
    echo "Error: Failed to install dependencies"
    exit 1
fi

echo "✓ Dependencies installed successfully"
echo

# Make script executable
echo "Step 2: Making script executable..."
chmod +x orange-tv-viewer-qt6.py

if [ $? -ne 0 ]; then
    echo "Error: Failed to make script executable"
    exit 1
fi

echo "✓ Script is now executable"
echo

# Ask if user wants system-wide installation
read -p "Do you want to install system-wide (available in application menu)? (y/N) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "Step 3: Installing system-wide..."
    
    # Copy script to /usr/local/bin
    sudo cp orange-tv-viewer-qt6.py /usr/local/bin/orange-tv-viewer
    sudo chmod +x /usr/local/bin/orange-tv-viewer
    
    # Copy icon to system pixmaps directory
    if [ -f "tv-128.ico" ]; then
        sudo mkdir -p /usr/local/share/pixmaps
        sudo cp tv-128.ico /usr/local/share/pixmaps/orange-tv-viewer.ico
        echo "✓ Icon installed"
    else
        echo "⚠ Warning: tv-128.ico not found, icon will not be installed"
    fi
    
    # Copy desktop entry
    sudo cp orange-tv-viewer.desktop /usr/share/applications/
    
    # Update desktop database
    sudo update-desktop-database /usr/share/applications/
    
    echo "✓ System-wide installation complete"
    echo
    echo "=========================================="
    echo "Installation Complete!"
    echo "=========================================="
    echo
    echo "You can now:"
    echo "1. Search for 'Orange TV Viewer' in your KDE application menu"
    echo "2. Run from terminal: orange-tv-viewer"
    echo
else
    echo "Skipping system-wide installation"
    echo
    echo "=========================================="
    echo "Installation Complete!"
    echo "=========================================="
    echo
    echo "You can run the application with:"
    echo "./orange-tv-viewer-qt6.py"
    echo
fi

echo "Enjoy watching Orange TV!"
