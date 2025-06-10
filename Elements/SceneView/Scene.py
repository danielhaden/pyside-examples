from PySide6.QtGui import QPen
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QGraphicsScene,
    QGraphicsLineItem
)
from Elements.LineItem import LineItem

class Scene(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)

        simple_line = self.addLine(60, 80, 90, 20)
        custom_line = self.addCustomLine(20, 50, 100, 40)

    def addLine(self, x1, y1, x2, y2):
        """
        Adds a simple line to the scene.
        :param x1:
        :param y1:
        :param x2:
        :param y2:
        :return:
        """

        black_pen = QPen(Qt.black, 2)
        line = super().addLine(x1, y1, x2, y2, black_pen)
        line.setFlag(QGraphicsLineItem.GraphicsItemFlag.ItemIsMovable)
        line.setFlag(QGraphicsLineItem.GraphicsItemFlag.ItemIsSelectable)
        return line

    def addCustomLine(self, x1, y1, x2, y2):
        """
        Like addLine() but uses LineItem for extended customization
        :param x1:
        :param y1:
        :param x2:
        :param y2:
        :return:
        """

        line = LineItem(x1, y1, x2, y2)
        self.addItem(line)
        return line
