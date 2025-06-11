from PySide6.QtWidgets import (
    QMainWindow, QGraphicsView
)
from Elements.SceneView.Scene import Scene
from Elements.SceneView.View import View

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QMainWindow Element")
        self.setMinimumSize(800,600)

        self.scene = Scene()
        self.custom_view = View()
        self.custom_view.setScene(self.scene)

        self.setCentralWidget(self.custom_view)