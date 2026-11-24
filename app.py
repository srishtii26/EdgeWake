import sys
from PySide6.QtWidgets import QApplication
from ui.dashboard import VoiceActivatorWindow

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Edge Voice Activator")
    window = VoiceActivatorWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
