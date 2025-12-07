#!/usr/bin/env python3
"""
Orange TV Viewer - A KDE Plasma 6/Qt6 application to view Orange TV live programs
"""

import sys
from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QToolBar, 
                             QVBoxLayout, QWidget)
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEngineSettings, QWebEnginePage
from PyQt6.QtGui import QAction, QKeySequence

class OrangeTVViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Orange TV - Programmes en Direct")
        self.setGeometry(100, 100, 1400, 900)
        
        # Store the home URL
        self.home_url = "https://tv.orange.fr/en-direct/programmes-en-cours"
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Create the web view
        self.browser = QWebEngineView()
        layout.addWidget(self.browser)
        
        # Configure web engine settings
        settings = self.browser.settings()
        settings.setAttribute(QWebEngineSettings.WebAttribute.PluginsEnabled, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.JavascriptEnabled, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.JavascriptCanOpenWindows, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.LocalStorageEnabled, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.AllowRunningInsecureContent, False)
        settings.setAttribute(QWebEngineSettings.WebAttribute.PlaybackRequiresUserGesture, False)
        settings.setAttribute(QWebEngineSettings.WebAttribute.FullScreenSupportEnabled, True)
        
        # Create toolbar
        self.create_toolbar()
        
        # Create menu bar
        self.create_menu_bar()
        
        # Load the Orange TV page
        self.browser.setUrl(QUrl(self.home_url))
        
        # Update title when page loads
        self.browser.titleChanged.connect(self.update_title)
        
        # Handle fullscreen requests from web content
        self.browser.page().fullScreenRequested.connect(self.handle_fullscreen_request)
    
    def create_toolbar(self):
        """Create the navigation toolbar"""
        toolbar = QToolBar("Navigation")
        toolbar.setMovable(False)
        self.addToolBar(toolbar)
        
        # Back button
        back_action = QAction("← Back", self)
        back_action.setStatusTip("Go back")
        back_action.setShortcut(QKeySequence.StandardKey.Back)
        back_action.triggered.connect(self.browser.back)
        toolbar.addAction(back_action)
        
        # Forward button
        forward_action = QAction("→ Forward", self)
        forward_action.setStatusTip("Go forward")
        forward_action.setShortcut(QKeySequence.StandardKey.Forward)
        forward_action.triggered.connect(self.browser.forward)
        toolbar.addAction(forward_action)
        
        # Reload button
        reload_action = QAction("⟳ Reload", self)
        reload_action.setStatusTip("Reload page")
        reload_action.setShortcut(QKeySequence.StandardKey.Refresh)
        reload_action.triggered.connect(self.browser.reload)
        toolbar.addAction(reload_action)
        
        # Home button
        home_action = QAction("⌂ Home", self)
        home_action.setStatusTip("Go to home page")
        home_action.setShortcut(QKeySequence("Ctrl+H"))
        home_action.triggered.connect(self.navigate_home)
        toolbar.addAction(home_action)
        
        # Stop button
        stop_action = QAction("✕ Stop", self)
        stop_action.setStatusTip("Stop loading")
        stop_action.setShortcut(QKeySequence("Escape"))
        stop_action.triggered.connect(self.browser.stop)
        toolbar.addAction(stop_action)
        
        # Separator
        toolbar.addSeparator()
        
        # Fullscreen button
        self.fullscreen_action = QAction("⛶ Fullscreen", self)
        self.fullscreen_action.setStatusTip("Toggle fullscreen")
        self.fullscreen_action.setShortcut(QKeySequence.StandardKey.FullScreen)
        self.fullscreen_action.triggered.connect(self.toggle_fullscreen)
        toolbar.addAction(self.fullscreen_action)
    
    def create_menu_bar(self):
        """Create the menu bar"""
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu("&File")
        
        quit_action = QAction("&Quit", self)
        quit_action.setShortcut(QKeySequence.StandardKey.Quit)
        quit_action.triggered.connect(self.close)
        file_menu.addAction(quit_action)
        
        # View menu
        view_menu = menubar.addMenu("&View")
        view_menu.addAction(self.fullscreen_action)
        
        zoom_in_action = QAction("Zoom &In", self)
        zoom_in_action.setShortcut(QKeySequence.StandardKey.ZoomIn)
        zoom_in_action.triggered.connect(lambda: self.browser.setZoomFactor(self.browser.zoomFactor() + 0.1))
        view_menu.addAction(zoom_in_action)
        
        zoom_out_action = QAction("Zoom &Out", self)
        zoom_out_action.setShortcut(QKeySequence.StandardKey.ZoomOut)
        zoom_out_action.triggered.connect(lambda: self.browser.setZoomFactor(self.browser.zoomFactor() - 0.1))
        view_menu.addAction(zoom_out_action)
        
        reset_zoom_action = QAction("&Reset Zoom", self)
        reset_zoom_action.setShortcut(QKeySequence("Ctrl+0"))
        reset_zoom_action.triggered.connect(lambda: self.browser.setZoomFactor(1.0))
        view_menu.addAction(reset_zoom_action)
        
        # Navigation menu
        nav_menu = menubar.addMenu("&Navigation")
        nav_menu.addAction(back_action := QAction("&Back", self))
        back_action.setShortcut(QKeySequence.StandardKey.Back)
        back_action.triggered.connect(self.browser.back)
        
        nav_menu.addAction(forward_action := QAction("&Forward", self))
        forward_action.setShortcut(QKeySequence.StandardKey.Forward)
        forward_action.triggered.connect(self.browser.forward)
        
        nav_menu.addAction(reload_action := QAction("&Reload", self))
        reload_action.setShortcut(QKeySequence.StandardKey.Refresh)
        reload_action.triggered.connect(self.browser.reload)
        
        nav_menu.addSeparator()
        
        nav_menu.addAction(home_action := QAction("&Home", self))
        home_action.setShortcut(QKeySequence("Ctrl+H"))
        home_action.triggered.connect(self.navigate_home)
    
    def navigate_home(self):
        """Navigate to the home page"""
        self.browser.setUrl(QUrl(self.home_url))
    
    def update_title(self, title):
        """Update window title with page title"""
        self.setWindowTitle(f"{title} - Orange TV Viewer")
    
    def toggle_fullscreen(self):
        """Toggle fullscreen mode"""
        if self.isFullScreen():
            self.showNormal()
            self.fullscreen_action.setText("⛶ Fullscreen")
        else:
            self.showFullScreen()
            self.fullscreen_action.setText("⛶ Exit Fullscreen")
    
    def handle_fullscreen_request(self, request):
        """Handle fullscreen requests from web content"""
        request.accept()
        if request.toggleOn():
            # Hide menubar and toolbar when video goes fullscreen
            self.menuBar().hide()
            toolbar = self.findChild(QToolBar)
            if toolbar:
                toolbar.hide()
            self.showFullScreen()
        else:
            # Restore menubar and toolbar when exiting fullscreen
            self.menuBar().show()
            toolbar = self.findChild(QToolBar)
            if toolbar:
                toolbar.show()
            self.showNormal()
    
    def keyPressEvent(self, event):
        """Handle key press events"""
        # Allow ESC to exit fullscreen
        if event.key() == Qt.Key.Key_Escape:
            if self.isFullScreen():
                # Check if there's a fullscreen web element
                self.browser.page().triggerAction(QWebEnginePage.WebAction.ExitFullScreen)
                self.menuBar().show()
                toolbar = self.findChild(QToolBar)
                if toolbar:
                    toolbar.show()
                self.showNormal()
        super().keyPressEvent(event)

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Orange TV Viewer")
    app.setOrganizationName("OrangeTVViewer")
    app.setApplicationDisplayName("Orange TV Viewer")
    
    # The application will automatically use the system theme (Breeze for KDE Plasma 6)
    
    window = OrangeTVViewer()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
