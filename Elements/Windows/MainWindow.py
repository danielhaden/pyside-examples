from PySide6.QtWidgets import (
    QMainWindow
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QMainWindow Element")
        self.setMinimumSize(800,600)