from PySide6.QtCore import QPoint, QPointF
from PySide6.QtGui import QPen, Qt, QPainter
from PySide6.QtWidgets import QGraphicsWidget, QGraphicsRectItem, QGraphicsLinearLayout


class GraphicsWidget(QGraphicsWidget):
    def __init__(self, x1, y1, x2, y2, content, parent=None):
        super().__init__(parent)

        self.content = content

        self.setFlag(QGraphicsWidget.GraphicsItemFlag.ItemIsMovable)
        self.setFlag(QGraphicsWidget.GraphicsItemFlag.ItemIsSelectable)


        self.boundary = QGraphicsRectItem(x1, y1, x2, y2)
        self.boundary.setPen(QPen(Qt.black, 2))


    def paint(self, painter, option, widget):
        painter.setRenderHints(QPainter.RenderHint.Antialiasing)
        painter.drawRect(self.boundary.boundingRect())
        painter.drawText(self.boundary.boundingRect().topLeft(), self.content)



    def boundingRect(self):
        return super().boundingRect()