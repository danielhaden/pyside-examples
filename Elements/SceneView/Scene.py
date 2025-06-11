from PySide6.QtGui import QPen
from PySide6.QtCore import Qt, QRect
from PySide6.QtWidgets import (
    QGraphicsScene,
    QGraphicsLineItem, QGraphicsSceneWheelEvent
)
from Elements.GraphicsShapes.LineItem import LineItem
import random

class Scene(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.lines = []
        for i in range(0, 1000):
            x1 = random.randint(0, 700)
            y1 = random.randint(0, 700)
            x2 = random.randint(0, 700)
            y2 = random.randint(0, 700)

            self.lines.append(self.addCustomLine(x1, y1, x2, y2))

        # activePanel
        # activeWindow
        # advance
        # backgroundBrush
        # blockSignals
        # bspTreeDepth
        # changed
        # childEvent
        # children
        # clear
        # clearFocus
        # clearSelection
        # collidingItems
        # connect
        # connectNotify
        # contextMenuEvent
        # createItemGroup
        # customEvent
        # deleteLater
        # destroyItemGroup
        # destroyed
        # disconnect
        # disconnectNotify
        # dragEnterEvent
        # dragLeaveEvent
        # dragMoveEvent
        # drawBackground
        # drawForeground
        # dropEvent
        # dumpObjectInfo
        # dumpObjectTree
        # dynamicPropertyNames
        # emit
        # event
        # eventFilter
        # findChild
        # findChildren
        # focusInEvent
        # focusItem
        # focusItemChanged
        # focusNextPrevChild
        # focusOnTouch
        # focusOutEvent
        # font
        # foregroundBrush
        # hasFocus
        # height
        # helpEvent
        # inherits
        # inputMethodEvent
        # inputMethodQuery
        # installEventFilter
        # invalidate
        # isActive
        # isQuickItemType
        # isSignalConnected
        # isWidgetType
        # isWindowType
        # itemAt
        # itemIndexMethod
        # items
        # itemsBoundingRect
        # keyPressEvent
        # keyReleaseEvent
        # killTimer
        # metaObject
        # minimumRenderSize
        # mouseDoubleClickEvent
        # mouseGrabberItem
        # mouseMoveEvent
        # mousePressEvent
        # mouseReleaseEvent
        # moveToThread
        # objectName
        # objectNameChanged
        # palette
        # parent
        # property
        # receivers
        # removeEventFilter
        # removeItem
        # render
        # sceneRect
        # sceneRectChanged
        # selectedItems
        # selectionArea
        # selectionChanged
        # sendEvent
        # sender
        # senderSignalIndex
        # setActivePanel
        # setActiveWindow
        # setBackgroundBrush
        # setBspTreeDepth
        # setFocus
        # setFocusItem
        # setFocusOnTouch
        # setFont
        # setForegroundBrush
        # setItemIndexMethod
        # setMinimumRenderSize
        # setObjectName
        # setPalette
        # setParent
        # setProperty
        # setSceneRect
        # setSelectionArea
        # setStickyFocus
        # setStyle
        # signalsBlocked
        # startTimer
        # stickyFocus
        # style
        # thread
        # timerEvent
        # tr
        # update
        # views
        # wheelEvent
        # width

    def children(self):
        """
        Returns child elements. For a QGraphicsScene, this is typically a singleton QObject
        :return:
        """
        return super().children()



        # event.accept()
        # event.clone()

        # isInputEvent
        # isInverted
        # isPointerEvent
        # isSinglePointEvent
        # modifiers
        # orientation
        # phase
        # pixelDelta
        # pos
        # registerEventType
        # scenePos
        # screenPos
        # setAccepted
        # setButtons
        # setDelta
        # setInverted
        # setModifiers
        # setOrientation
        # setPhase
        # setPixelDelta
        # setPos
        # setScenePos
        # setScreenPos
        # setTimestamp
        # spontaneous
        # timestamp
        # type
        # widget

    def addPath(self):
        return

    def addPixmap(self, pixmap):
        return

    def addPolygon(self, polygon):
        return

    def addRect(self, rect):
        return

    def addSimpleText(self, text):
        return

    def addText(self, text):
        return

    def addWidget(self, widget):
        return

    def addEllipse(self):
        super().addEllipse(QRect(20, 20, 100, 100))

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
