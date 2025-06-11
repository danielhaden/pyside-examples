from PySide6.QtGui import QPen, Qt, QPainter
from PySide6.QtWidgets import QGraphicsItem, QGraphicsEllipseItem, QVBoxLayout, QGraphicsLinearLayout


class GraphicsItem(QGraphicsItem):
    def __init__(self, x1, y1, x2, y2, parent=None):
        super().__init__(parent)
        self._selected_pen = QPen(Qt.green,3)
        self._default_pen = QPen(Qt.black, 2)

        # make the items movable and selectable
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        self.setAcceptHoverEvents(True)

        self.boundary = QGraphicsEllipseItem(20, 20, 120, 120)
        self.boundary.setPen(self._default_pen)

        layout = QGraphicsLinearLayout()

    def paint(self, painter, option, widget):
        super().paint(painter, option, widget)

    def boundingRect(self):
        super().boundingRect()