from PySide6.QtWidgets import QGraphicsLineItem
from PySide6.QtGui import QPen
from PySide6.QtCore import Qt
import inspect

class LineItem(QGraphicsLineItem):
    def __init__(self, x1, y1, x2, y2, parent=None):
        super().__init__(x1, y1, x2, y2, parent)
        self._selected_pen = QPen(Qt.green,3)
        self._default_pen = QPen(Qt.black, 2)

        # make the items movable and selectable
        self.setFlag(QGraphicsLineItem.GraphicsItemFlag.ItemIsMovable)
        self.setFlag(QGraphicsLineItem.GraphicsItemFlag.ItemIsSelectable)
        self.setAcceptHoverEvents(True)

        # Tool Tip getter/setter
        #self.setToolTip("LineItem ToolTip!")
        #print(self.toolTip())
        # self.acceptDrops()
        # self.setAcceptDrops(True)
        #item.acceptDrops()
        #item.acceptHoverEvents()
        #item.acceptedMouseButtons()
        #item.addToIndex()
        #item.advance(3)
        #item.boundingRect()
        #item.boundingRegion()
        #item.boundingRegionGranularity()
        #item.cacheMode()
        #item.childItems()
        #item.childrenBoundingRect()
        #item.clearFocus()
        #item.clipPath()
        #item.collidesWithItem()
        #item.collidesWithPath()
        #item.collidingItems()
        #item.commonAncestorItem()
        #item.contains(point)
        #item.contextMenuEvent()
        #item.cursor()
        #item.data()
        #item.deviceTransform()
        #item.dragEnterEvent()
        #item.dragLeaveEvent()
        #item.dragMoveEvent()
        #item.dropEvent()
        #item.effectiveOpacity()
        #item.ensureVisible()
        #item.extension()
        #item.filtersChildEvents()
        #item.flags
        #item.focusInEvent
        #item.focusItem
        #item.focusOutEvent
        #item.focusProxy
        #item.focusScopeItem
        #item.grabKeyboard
        #item.grabMouse
        #item.graphicsEffect
        #item.group
        #item.handlesChildEvents()
        #item.hasCursor()
        #item.hasFocus()
        #item.hide()

        #item.inputMethodEvent()
        #item.inputMethodHints()
        #item.inputMethodQuery()
        #item.installSceneEventFilter()
        #item.IsActive
        #item.IsAncestorOf
        #item.IsBlockedByModalPanel
        #item.IsClipped
        #item.IsEnabled
        #item.IsObscured
        #item.IsObscuredBy
        #item.IsPanel
        #item.IsSelected
        #item.IsUnderMouse
        #item.IsVisible
        #item.IsVisibleTo
        #item.IsWidget
        #item.IsWindow
        #item.itemChange
        #item.itemTransform
        #item.keyPressEvent
        #item.keyReleaseEvent
        #item.line
        #item.mapFromItem
        #item.mapFromParent
        #item.mapFromScene
        #item.mapRectFromItem
        #item.mapRectFromParent
        #item.mapRectFromScene
        #item.mapRectToItem
        #item.mapRectToParent
        #item.mapRectToScene
        #item.mapToItem
        #item.mapToParent
        #item.mapToScene
        #item.mouseDoubleClickEvent
        #item.mouseMoveEvent
        #item.mousePressEvent
        #item.mouseReleaseEvent
        #item.moveBy
        #item.opacity
        #item.opaqueArea
        #item.paint
        #item.panel
        #item.panelModality
        #item.parentItem
        #item.parentObject
        #item.parentWidget
        #item.pen()
        #item.ops()
        #item.prepareGeometryChange()
        #item.removeFromIndex()
        #item.removeSceneEventFilter()
        #item.resetTransform()
        #item.rotation()
        #item.scale()
        #item.scene()
        #item.sceneBoundingRect()
        #item.sceneEvent()
        #item.sceneEventFilter()
        #item.scenePos()
        #item.sceneTransform()
        #item.scroll()
        #item.setAcceptDrops()
        #item.setAcceptHoverEvents()
        #item.setAcceptTouchEvents()
        #item.setAcceptedMouseButtons()
        #item.setActive()
        #item.setBoundingRegionGranularity()
        #item.setCacheMode()
        #item.setCursor()
        #item.setData()
        #item.setEnabled()
        #item.setFiltersChildEvents()
        #item.setFlag()
        #item.setFlags()
        #item.setFocus()
        #item.setFocusProxy()
        #item.setGraphicsEffect()
        #item.setGroup()
        #item.setHandlesChildEvents()
        #item.setInputMethodHints()
        #item.setLine()
        #item.setOpacity()
        #item.setPanelModality()
        #item.setParentItem()
        #item.setPen()
        #item.setPos()
        #item.setRotation()
        #item.setScale()
        #item.setSelected()
        #item.setToolTip()
        #item.setTransform()
        #item.setTransformOriginPoint()
        #item.setTransformations()
        #item.setVisible()
        #item.setX
        #item.setY
        #item.setZValue
        #item.shape()

        # for key in dir(item):
        #     if callable(getattr(item, key)):
        #         print(key)

    # item.hoverLeaveEvent()
    # item.hoverMoveEvent()

    def hoverEnterEvent(self, event):
        self.setPen(QPen(Qt.red, 3))
        event.accept()

    def hoverMoveEvent(self, event):
        event.accept()

    def hoverLeaveEvent(self, event):
        self.setPen(self._default_pen)
        event.accept()
        self.itemChange(None, None)

    def pen(self):
        return self._default_pen

    def setPen(self, pen):
        self._default_pen = pen

    def itemChange(self, change, value):
        """
        Fires when the item has changed in some way
        :param change: The type of change that has occurred
        :param value: A value associated with the change. In the case of ItemSelectedChange, value=1 if selected, and value=0 if deselected.
        :return: value by default
        """

        if change == None:
            return super().itemChange(QGraphicsLineItem.GraphicsItemChange.ItemSelectedChange, value)

        if change == QGraphicsLineItem.GraphicsItemChange.ItemSelectedChange:

            if value:
                self.setPen(self._selected_pen)

            else:
                self.setPen(QPen(Qt.black, 2))

        return super().itemChange(change, value)

    def paint(self, painter, option, widget):
        painter.setPen(self._default_pen)
        painter.drawLine(self.line())



