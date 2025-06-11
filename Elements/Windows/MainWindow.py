from PySide6.QtWidgets import (
    QMainWindow, QGraphicsView, QTabWidget, QWidget, QVBoxLayout, QLabel
)
from Elements.SceneView.Scene import Scene
from Elements.SceneView.View import View

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QMainWindow Element")
        self.setMinimumSize(800,600)

        self.scene = Scene()
        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)
        self.add_tab("Primary View", "StickView 1")
        self.add_tab("Secondary View", "StickView 2")

    def add_tab(self, tab_name, content_text):
        custom_view = View()
        custom_view.setScene(self.scene)

        tab = QWidget()
        layout = QVBoxLayout()
        label = QLabel(content_text)
        layout.addWidget(label)
        layout.addWidget(custom_view)
        tab.setLayout(layout)
        self.tab_widget.addTab(tab, tab_name)



