from PySide6.QtWidgets import (
    QMainWindow, QGraphicsView
)
from Elements.SceneView.Scene import Scene

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QMainWindow Element")
        self.setMinimumSize(800,600)

        self.scene = Scene()
        self.view = QGraphicsView(self.scene)

        self.setCentralWidget(self.view)