from PySide6.QtWidgets import QGraphicsView


class View(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)

        for key in dir(self):
            if callable(getattr(self, key)):
                print(key)

        # acceptDrops
        # accessibleDescription
        # accessibleIdentifier
        # accessibleName
        # actionEvent
        # actions
        # activateWindow
        # addAction
        # addActions
        # addScrollBarWidget
        # adjustSize
        # alignment
        # autoFillBackground
        # backgroundBrush
        # backgroundRole
        # backingStore
        # baseSize
        # blockSignals
        # cacheMode
        # centerOn
        # changeEvent
        # childAt
        # childEvent
        # children
        # childrenRect
        # childrenRegion
        # clearFocus
        # clearMask
        # close
        # closeEvent
        # colorCount
        # connect
        # connectNotify
        # contentsMargins
        # contentsRect
        # contextMenuEvent
        # contextMenuPolicy
        # cornerWidget
        # create
        # createWinId
        # createWindowContainer
        # cursor
        # customContextMenuRequested
        # customEvent
        # deleteLater
        # depth
        # destroy
        # destroyed
        # devType
        # devicePixelRatio
        # devicePixelRatioF
        # devicePixelRatioFScale
        # disconnect
        # disconnectNotify
        # dragEnterEvent
        # dragLeaveEvent
        # dragMode
        # dragMoveEvent
        # drawBackground
        # drawForeground
        # drawFrame
        # drawItems
        # dropEvent
        # dumpObjectInfo
        # dumpObjectTree
        # dynamicPropertyNames
        # effectiveWinId
        # emit
        # encodeMetricF
        # ensurePolished
        # ensureVisible
        # enterEvent
        # event
        # eventFilter
        # find
        # findChild
        # findChildren
        # fitInView
        # focusInEvent
        # focusNextChild
        # focusNextPrevChild
        # focusOutEvent
        # focusPolicy
        # focusPreviousChild
        # focusProxy
        # focusWidget
        # font
        # fontInfo
        # fontMetrics
        # foregroundBrush
        # foregroundRole
        # frameGeometry
        # frameRect
        # frameShadow
        # frameShape
        # frameSize
        # frameStyle
        # frameWidth
        # geometry
        # grab
        # grabGesture
        # grabKeyboard
        # grabMouse
        # grabShortcut
        # graphicsEffect
        # graphicsProxyWidget
        # hasFocus
        # hasHeightForWidth
        # hasMouseTracking
        # hasTabletTracking
        # height
        # heightForWidth
        # heightMM
        # hide
        # hideEvent
        # horizontalScrollBar
        # horizontalScrollBarPolicy
        # inherits
        # initPainter
        # initStyleOption
        # inputMethodEvent
        # inputMethodHints
        # inputMethodQuery
        # insertAction
        # insertActions
        # installEventFilter
        # internalWinId
        # invalidateScene
        # isActiveWindow
        # isAncestorOf
        # isEnabled
        # isEnabledTo
        # isFullScreen
        # isHidden
        # isInteractive
        # isLeftToRight
        # isMaximized
        # isMinimized
        # isModal
        # isQuickItemType
        # isRightToLeft
        # isSignalConnected
        # isTopLevel
        # isTransformed
        # isVisible
        # isVisibleTo
        # isWidgetType
        # isWindow
        # isWindowModified
        # isWindowType
        # itemAt
        # items
        # keyPressEvent
        # keyReleaseEvent
        # keyboardGrabber
        # killTimer
        # layout
        # layoutDirection
        # leaveEvent
        # lineWidth
        # locale
        # logicalDpiX
        # logicalDpiY
        # lower
        # mapFrom
        # mapFromGlobal
        # mapFromParent
        # mapFromScene
        # mapTo
        # mapToGlobal
        # mapToParent
        # mapToScene
        # mask
        # maximumHeight
        # maximumSize
        # maximumViewportSize
        # maximumWidth
        # metaObject
        # metric
        # midLineWidth
        # minimumHeight
        # minimumSize
        # minimumSizeHint
        # minimumWidth
        # mouseDoubleClickEvent
        # mouseGrabber
        # mouseMoveEvent
        # mousePressEvent
        # mouseReleaseEvent
        # move
        # moveEvent
        # moveToThread
        # nativeEvent
        # nativeParentWidget
        # nextInFocusChain
        # normalGeometry
        # objectName
        # objectNameChanged
        # optimizationFlags
        # overrideWindowFlags
        # overrideWindowState
        # paintEngine
        # paintEvent
        # paintingActive
        # palette
        # parent
        # parentWidget
        # physicalDpiX
        # physicalDpiY
        # pos
        # previousInFocusChain
        # property
        # raise_
        # receivers
        # rect
        # redirected
        # releaseKeyboard
        # releaseMouse
        # releaseShortcut
        # removeAction
        # removeEventFilter
        # render
        # renderHints
        # repaint
        # resetCachedContent
        # resetTransform
        # resize
        # resizeAnchor
        # resizeEvent
        # restoreGeometry
        # rotate
        # rubberBandChanged
        # rubberBandRect
        # rubberBandSelectionMode
        # saveGeometry
        # scale
        # scene
        # sceneRect
        # screen
        # scroll
        # scrollBarWidgets
        # scrollContentsBy
        # sender
        # senderSignalIndex
        # setAcceptDrops
        # setAccessibleDescription
        # setAccessibleIdentifier
        # setAccessibleName
        # setAlignment
        # setAttribute
        # setAutoFillBackground
        # setBackgroundBrush
        # setBackgroundRole
        # setBaseSize
        # setCacheMode
        # setContentsMargins
        # setContextMenuPolicy
        # setCornerWidget
        # setCursor
        # setDisabled
        # setDragMode
        # setEnabled
        # setFixedHeight
        # setFixedSize
        # setFixedWidth
        # setFocus
        # setFocusPolicy
        # setFocusProxy
        # setFont
        # setForegroundBrush
        # setForegroundRole
        # setFrameRect
        # setFrameShadow
        # setFrameShape
        # setFrameStyle
        # setGeometry
        # setGraphicsEffect
        # setHidden
        # setHorizontalScrollBar
        # setHorizontalScrollBarPolicy
        # setInputMethodHints
        # setInteractive
        # setLayout
        # setLayoutDirection
        # setLineWidth
        # setLocale
        # setMask
        # setMaximumHeight
        # setMaximumSize
        # setMaximumWidth
        # setMidLineWidth
        # setMinimumHeight
        # setMinimumSize
        # setMinimumWidth
        # setMouseTracking
        # setObjectName
        # setOptimizationFlag
        # setOptimizationFlags
        # setPalette
        # setParent
        # setProperty
        # setRenderHint
        # setRenderHints
        # setResizeAnchor
        # setRubberBandSelectionMode
        # setScene
        # setSceneRect
        # setScreen
        # setShortcutAutoRepeat
        # setShortcutEnabled
        # setSizeAdjustPolicy
        # setSizeIncrement
        # setSizePolicy
        # setStatusTip
        # setStyle
        # setStyleSheet
        # setTabOrder
        # setTabletTracking
        # setToolTip
        # setToolTipDuration
        # setTransform
        # setTransformationAnchor
        # setUpdatesEnabled
        # setVerticalScrollBar
        # setVerticalScrollBarPolicy
        # setViewport
        # setViewportMargins
        # setViewportUpdateMode
        # setVisible
        # setWhatsThis
        # setWindowFilePath
        # setWindowFlag
        # setWindowFlags
        # setWindowIcon
        # setWindowIconText
        # setWindowModality
        # setWindowModified
        # setWindowOpacity
        # setWindowRole
        # setWindowState
        # setWindowTitle
        # setupViewport
        # sharedPainter
        # shear
        # show
        # showEvent
        # showFullScreen
        # showMaximized
        # showMinimized
        # showNormal
        # signalsBlocked
        # size
        # sizeAdjustPolicy
        # sizeHint
        # sizeIncrement
        # sizePolicy
        # stackUnder
        # startTimer
        # statusTip
        # style
        # styleSheet
        # tabletEvent
        # testAttribute
        # thread
        # timerEvent
        # toolTip
        # toolTipDuration
        # topLevelWidget
        # tr
        # transform
        # transformationAnchor
        # translate
        # underMouse
        # ungrabGesture
        # unsetCursor
        # unsetLayoutDirection
        # unsetLocale
        # update
        # updateGeometry
        # updateMicroFocus
        # updateScene
        # updateSceneRect
        # updatesEnabled
        # verticalScrollBar
        # verticalScrollBarPolicy
        # viewport
        # viewportEvent
        # viewportMargins
        # viewportSizeHint
        # viewportTransform
        # viewportUpdateMode
        # visibleRegion
        # whatsThis
        # wheelEvent
        # width
        # widthMM
        # winId
        # window
        # windowFilePath
        # windowFlags
        # windowHandle
        # windowIcon
        # windowIconChanged
        # windowIconText
        # windowIconTextChanged
        # windowModality
        # windowOpacity
        # windowRole
        # windowState
        # windowTitle
        # windowTitleChanged
        # windowType
        # x
        # y
