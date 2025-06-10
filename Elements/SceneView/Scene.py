from PySide6.QtGui import QPen
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QGraphicsScene,
    QGraphicsLineItem
)

class Scene(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)
        line = self.addLine(50, 50, 120, 100)

        line.setFlag(QGraphicsLineItem.GraphicsItemFlag.ItemIsMovable)
        line.setFlag(QGraphicsLineItem.GraphicsItemFlag.ItemIsSelectable)

    def addLine(self, x1, y1, x2, y2):
        black_pen = QPen(Qt.black, 2)
        line = super().addLine(x1, y1, x2, y2, black_pen)
        return line