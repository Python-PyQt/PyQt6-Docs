:orphan:

.. sip:class:: PyQt6.QtWidgets.QWidget
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject` :sip:ref:`~PyQt6.QtGui.QPaintDevice`
    :description: QtWidgets/QWidget-c.rst

    .. sip:enum:: PyQt6.QtWidgets.QWidget.RenderFlag
        :description: QtWidgets/QWidget-RenderFlag-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QWidget.RenderFlag.DrawChildren
            :description: QtWidgets/QWidget-RenderFlag-DrawChildren-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QWidget.RenderFlag.DrawWindowBackground
            :description: QtWidgets/QWidget-RenderFlag-DrawWindowBackground-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QWidget.RenderFlag.IgnoreMask
            :description: QtWidgets/QWidget-RenderFlag-IgnoreMask-v.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
            flags: :sip:ref:`~PyQt6.QtCore.Qt.WindowType` = Qt.WindowFlags()
        :description: QtWidgets/QWidget-__init__-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.acceptDrops
        :returns:
            bool
        :description: QtWidgets/QWidget-acceptDrops-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.accessibleDescription
        :returns:
            str
        :description: QtWidgets/QWidget-accessibleDescription-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.accessibleName
        :returns:
            str
        :description: QtWidgets/QWidget-accessibleName-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.actionEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QActionEvent`
        :description: QtWidgets/QWidget-actionEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.actions
        :returns:
            List[:sip:ref:`~PyQt6.QtGui.QAction`]
        :description: QtWidgets/QWidget-actions-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.activateWindow
        :description: QtWidgets/QWidget-activateWindow-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.addAction
        :args:
            Optional[str]
        :returns:
            :sip:ref:`~PyQt6.QtGui.QAction`
        :description: QtWidgets/QWidget-addAction-f-9.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.addAction
        :args:
            :sip:ref:`~PyQt6.QtGui.QAction`
        :description: QtWidgets/QWidget-addAction-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.addAction
        :args:
            :sip:ref:`~PyQt6.QtGui.QIcon`
            Optional[str]
        :returns:
            :sip:ref:`~PyQt6.QtGui.QAction`
        :description: QtWidgets/QWidget-addAction-f-10.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.addAction
        :args:
            Optional[str]
            Union[:sip:ref:`~PyQt6.QtGui.QKeySequence`, :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey`, Optional[str], int]
        :returns:
            :sip:ref:`~PyQt6.QtGui.QAction`
        :description: QtWidgets/QWidget-addAction-f-11.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.addAction
        :args:
            :sip:ref:`~PyQt6.QtGui.QIcon`
            Optional[str]
            Union[:sip:ref:`~PyQt6.QtGui.QKeySequence`, :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey`, Optional[str], int]
        :returns:
            :sip:ref:`~PyQt6.QtGui.QAction`
        :description: QtWidgets/QWidget-addAction-f-12.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.addAction
        :args:
            Optional[str]
            PYQT_SLOT
            type: :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType` = :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType.AutoConnection`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QAction`
        :description: QtWidgets/QWidget-addAction-f-13.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.addAction
        :args:
            :sip:ref:`~PyQt6.QtGui.QIcon`
            Optional[str]
            PYQT_SLOT
            type: :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType` = :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType.AutoConnection`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QAction`
        :description: QtWidgets/QWidget-addAction-f-14.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.addAction
        :args:
            Optional[str]
            Union[:sip:ref:`~PyQt6.QtGui.QKeySequence`, :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey`, Optional[str], int]
            PYQT_SLOT
            type: :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType` = :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType.AutoConnection`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QAction`
        :description: QtWidgets/QWidget-addAction-f-15.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.addAction
        :args:
            :sip:ref:`~PyQt6.QtGui.QIcon`
            Optional[str]
            Union[:sip:ref:`~PyQt6.QtGui.QKeySequence`, :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey`, Optional[str], int]
            PYQT_SLOT
            type: :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType` = :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType.AutoConnection`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QAction`
        :description: QtWidgets/QWidget-addAction-f-16.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.addActions
        :args:
            Iterable[:sip:ref:`~PyQt6.QtGui.QAction`]
        :description: QtWidgets/QWidget-addActions-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.adjustSize
        :description: QtWidgets/QWidget-adjustSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.autoFillBackground
        :returns:
            bool
        :description: QtWidgets/QWidget-autoFillBackground-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.backgroundRole
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPalette.ColorRole`
        :description: QtWidgets/QWidget-backgroundRole-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.baseSize
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QWidget-baseSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.changeEvent
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :description: QtWidgets/QWidget-changeEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.childAt
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QWidget-childAt-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.childAt
        :args:
            int
            int
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QWidget-childAt-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.childrenRect
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtWidgets/QWidget-childrenRect-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.childrenRegion
        :returns:
            :sip:ref:`~PyQt6.QtGui.QRegion`
        :description: QtWidgets/QWidget-childrenRegion-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.clearFocus
        :description: QtWidgets/QWidget-clearFocus-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.clearMask
        :description: QtWidgets/QWidget-clearMask-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.close
        :returns:
            bool
        :description: QtWidgets/QWidget-close-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.closeEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QCloseEvent`
        :description: QtWidgets/QWidget-closeEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.contentsMargins
        :returns:
            :sip:ref:`~PyQt6.QtCore.QMargins`
        :description: QtWidgets/QWidget-contentsMargins-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.contentsRect
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtWidgets/QWidget-contentsRect-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.contextMenuEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QContextMenuEvent`
        :description: QtWidgets/QWidget-contextMenuEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.contextMenuPolicy
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.ContextMenuPolicy`
        :description: QtWidgets/QWidget-contextMenuPolicy-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.create
        :args:
            window: :py:class:`~PyQt6.sip.voidptr` = None
            initializeWindow: bool = True
            destroyOldWindow: bool = True
        :description: QtWidgets/QWidget-create-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.createWindowContainer
        :args:
            :sip:ref:`~PyQt6.QtGui.QWindow`
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
            flags: :sip:ref:`~PyQt6.QtCore.Qt.WindowType` = Qt.WindowFlags()
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :static:
        :description: QtWidgets/QWidget-createWindowContainer-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.cursor
        :returns:
            :sip:ref:`~PyQt6.QtGui.QCursor`
        :description: QtWidgets/QWidget-cursor-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.destroy
        :args:
            destroyWindow: bool = True
            destroySubWindows: bool = True
        :description: QtWidgets/QWidget-destroy-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.devType
        :returns:
            int
        :description: QtWidgets/QWidget-devType-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.dragEnterEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QDragEnterEvent`
        :description: QtWidgets/QWidget-dragEnterEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.dragLeaveEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QDragLeaveEvent`
        :description: QtWidgets/QWidget-dragLeaveEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.dragMoveEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QDragMoveEvent`
        :description: QtWidgets/QWidget-dragMoveEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.dropEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QDropEvent`
        :description: QtWidgets/QWidget-dropEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.effectiveWinId
        :returns:
            :py:class:`~PyQt6.sip.voidptr`
        :description: QtWidgets/QWidget-effectiveWinId-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.ensurePolished
        :description: QtWidgets/QWidget-ensurePolished-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.enterEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QEnterEvent`
        :description: QtWidgets/QWidget-enterEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtWidgets/QWidget-event-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.find
        :args:
            :py:class:`~PyQt6.sip.voidptr`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :static:
        :description: QtWidgets/QWidget-find-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.focusInEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QFocusEvent`
        :description: QtWidgets/QWidget-focusInEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.focusNextChild
        :returns:
            bool
        :description: QtWidgets/QWidget-focusNextChild-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.focusNextPrevChild
        :args:
            bool
        :returns:
            bool
        :description: QtWidgets/QWidget-focusNextPrevChild-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.focusOutEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QFocusEvent`
        :description: QtWidgets/QWidget-focusOutEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.focusPolicy
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.FocusPolicy`
        :description: QtWidgets/QWidget-focusPolicy-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.focusPreviousChild
        :returns:
            bool
        :description: QtWidgets/QWidget-focusPreviousChild-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.focusProxy
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QWidget-focusProxy-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.focusWidget
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QWidget-focusWidget-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.font
        :returns:
            :sip:ref:`~PyQt6.QtGui.QFont`
        :description: QtWidgets/QWidget-font-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.fontInfo
        :returns:
            :sip:ref:`~PyQt6.QtGui.QFontInfo`
        :description: QtWidgets/QWidget-fontInfo-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.fontMetrics
        :returns:
            :sip:ref:`~PyQt6.QtGui.QFontMetrics`
        :description: QtWidgets/QWidget-fontMetrics-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.foregroundRole
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPalette.ColorRole`
        :description: QtWidgets/QWidget-foregroundRole-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.frameGeometry
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtWidgets/QWidget-frameGeometry-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.frameSize
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QWidget-frameSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.geometry
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtWidgets/QWidget-geometry-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.grab
        :args:
            rectangle: :sip:ref:`~PyQt6.QtCore.QRect` = QRect(QPoint(0,0),QSize(-1,-1))
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPixmap`
        :description: QtWidgets/QWidget-grab-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.grabGesture
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.GestureType`
            flags: :sip:ref:`~PyQt6.QtCore.Qt.GestureFlag` = Qt.GestureFlags()
        :description: QtWidgets/QWidget-grabGesture-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.grabKeyboard
        :description: QtWidgets/QWidget-grabKeyboard-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.grabMouse
        :description: QtWidgets/QWidget-grabMouse-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.grabMouse
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QCursor`, :sip:ref:`~PyQt6.QtCore.Qt.CursorShape`]
        :description: QtWidgets/QWidget-grabMouse-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.grabShortcut
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QKeySequence`, :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey`, Optional[str], int]
            context: :sip:ref:`~PyQt6.QtCore.Qt.ShortcutContext` = :sip:ref:`~PyQt6.QtCore.Qt.ShortcutContext.WindowShortcut`
        :returns:
            int
        :description: QtWidgets/QWidget-grabShortcut-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.graphicsEffect
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsEffect`
        :description: QtWidgets/QWidget-graphicsEffect-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.graphicsProxyWidget
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsProxyWidget`
        :description: QtWidgets/QWidget-graphicsProxyWidget-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.hasFocus
        :returns:
            bool
        :description: QtWidgets/QWidget-hasFocus-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.hasHeightForWidth
        :returns:
            bool
        :description: QtWidgets/QWidget-hasHeightForWidth-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.hasMouseTracking
        :returns:
            bool
        :description: QtWidgets/QWidget-hasMouseTracking-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.hasTabletTracking
        :returns:
            bool
        :description: QtWidgets/QWidget-hasTabletTracking-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.height
        :returns:
            int
        :description: QtWidgets/QWidget-height-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.heightForWidth
        :args:
            int
        :returns:
            int
        :description: QtWidgets/QWidget-heightForWidth-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.hide
        :description: QtWidgets/QWidget-hide-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.hideEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QHideEvent`
        :description: QtWidgets/QWidget-hideEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.initPainter
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
        :description: QtWidgets/QWidget-initPainter-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.inputMethodEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QInputMethodEvent`
        :description: QtWidgets/QWidget-inputMethodEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.inputMethodHints
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.InputMethodHint`
        :description: QtWidgets/QWidget-inputMethodHints-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.inputMethodQuery
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.InputMethodQuery`
        :returns:
            Any
        :description: QtWidgets/QWidget-inputMethodQuery-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.insertAction
        :args:
            :sip:ref:`~PyQt6.QtGui.QAction`
            :sip:ref:`~PyQt6.QtGui.QAction`
        :description: QtWidgets/QWidget-insertAction-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.insertActions
        :args:
            :sip:ref:`~PyQt6.QtGui.QAction`
            Iterable[:sip:ref:`~PyQt6.QtGui.QAction`]
        :description: QtWidgets/QWidget-insertActions-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.isActiveWindow
        :returns:
            bool
        :description: QtWidgets/QWidget-isActiveWindow-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.isAncestorOf
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :returns:
            bool
        :description: QtWidgets/QWidget-isAncestorOf-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.isEnabled
        :returns:
            bool
        :description: QtWidgets/QWidget-isEnabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.isEnabledTo
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :returns:
            bool
        :description: QtWidgets/QWidget-isEnabledTo-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.isFullScreen
        :returns:
            bool
        :description: QtWidgets/QWidget-isFullScreen-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.isHidden
        :returns:
            bool
        :description: QtWidgets/QWidget-isHidden-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.isLeftToRight
        :returns:
            bool
        :description: QtWidgets/QWidget-isLeftToRight-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.isMaximized
        :returns:
            bool
        :description: QtWidgets/QWidget-isMaximized-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.isMinimized
        :returns:
            bool
        :description: QtWidgets/QWidget-isMinimized-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.isModal
        :returns:
            bool
        :description: QtWidgets/QWidget-isModal-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.isRightToLeft
        :returns:
            bool
        :description: QtWidgets/QWidget-isRightToLeft-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.isVisible
        :returns:
            bool
        :description: QtWidgets/QWidget-isVisible-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.isVisibleTo
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :returns:
            bool
        :description: QtWidgets/QWidget-isVisibleTo-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.isWindow
        :returns:
            bool
        :description: QtWidgets/QWidget-isWindow-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.isWindowModified
        :returns:
            bool
        :description: QtWidgets/QWidget-isWindowModified-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.keyboardGrabber
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :static:
        :description: QtWidgets/QWidget-keyboardGrabber-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.keyPressEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QKeyEvent`
        :description: QtWidgets/QWidget-keyPressEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.keyReleaseEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QKeyEvent`
        :description: QtWidgets/QWidget-keyReleaseEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.layout
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QLayout`
        :description: QtWidgets/QWidget-layout-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.layoutDirection
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.LayoutDirection`
        :description: QtWidgets/QWidget-layoutDirection-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.leaveEvent
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :description: QtWidgets/QWidget-leaveEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.locale
        :returns:
            :sip:ref:`~PyQt6.QtCore.QLocale`
        :description: QtWidgets/QWidget-locale-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.lower
        :description: QtWidgets/QWidget-lower-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.mapFrom
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :description: QtWidgets/QWidget-mapFrom-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.mapFrom
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtWidgets/QWidget-mapFrom-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.mapFromGlobal
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :description: QtWidgets/QWidget-mapFromGlobal-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.mapFromGlobal
        :args:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtWidgets/QWidget-mapFromGlobal-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.mapFromParent
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :description: QtWidgets/QWidget-mapFromParent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.mapFromParent
        :args:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtWidgets/QWidget-mapFromParent-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.mapTo
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :description: QtWidgets/QWidget-mapTo-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.mapTo
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtWidgets/QWidget-mapTo-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.mapToGlobal
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :description: QtWidgets/QWidget-mapToGlobal-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.mapToGlobal
        :args:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtWidgets/QWidget-mapToGlobal-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.mapToParent
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :description: QtWidgets/QWidget-mapToParent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.mapToParent
        :args:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtWidgets/QWidget-mapToParent-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.mask
        :returns:
            :sip:ref:`~PyQt6.QtGui.QRegion`
        :description: QtWidgets/QWidget-mask-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.maximumHeight
        :returns:
            int
        :description: QtWidgets/QWidget-maximumHeight-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.maximumSize
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QWidget-maximumSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.maximumWidth
        :returns:
            int
        :description: QtWidgets/QWidget-maximumWidth-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.metric
        :args:
            :sip:ref:`~PyQt6.QtGui.QPaintDevice.PaintDeviceMetric`
        :returns:
            int
        :description: QtWidgets/QWidget-metric-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.minimumHeight
        :returns:
            int
        :description: QtWidgets/QWidget-minimumHeight-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.minimumSize
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QWidget-minimumSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.minimumSizeHint
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QWidget-minimumSizeHint-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.minimumWidth
        :returns:
            int
        :description: QtWidgets/QWidget-minimumWidth-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.mouseDoubleClickEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtWidgets/QWidget-mouseDoubleClickEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.mouseGrabber
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :static:
        :description: QtWidgets/QWidget-mouseGrabber-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.mouseMoveEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtWidgets/QWidget-mouseMoveEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.mousePressEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtWidgets/QWidget-mousePressEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.mouseReleaseEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtWidgets/QWidget-mouseReleaseEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.move
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :description: QtWidgets/QWidget-move-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.move
        :args:
            int
            int
        :description: QtWidgets/QWidget-move-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.moveEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMoveEvent`
        :description: QtWidgets/QWidget-moveEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.nativeEvent
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
            :py:class:`~PyQt6.sip.voidptr`
        :returns:
            bool
            :py:class:`~PyQt6.sip.voidptr`
        :description: QtWidgets/QWidget-nativeEvent-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.nativeParentWidget
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QWidget-nativeParentWidget-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.nextInFocusChain
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QWidget-nextInFocusChain-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.normalGeometry
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtWidgets/QWidget-normalGeometry-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.overrideWindowFlags
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.WindowType`
        :description: QtWidgets/QWidget-overrideWindowFlags-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.overrideWindowState
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.WindowState`
        :description: QtWidgets/QWidget-overrideWindowState-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.paintEngine
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPaintEngine`
        :description: QtWidgets/QWidget-paintEngine-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.paintEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QPaintEvent`
        :description: QtWidgets/QWidget-paintEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.palette
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPalette`
        :description: QtWidgets/QWidget-palette-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.parentWidget
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QWidget-parentWidget-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.pos
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :description: QtWidgets/QWidget-pos-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.previousInFocusChain
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QWidget-previousInFocusChain-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.raise_
        :description: QtWidgets/QWidget-raise_-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.rect
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtWidgets/QWidget-rect-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.releaseKeyboard
        :description: QtWidgets/QWidget-releaseKeyboard-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.releaseMouse
        :description: QtWidgets/QWidget-releaseMouse-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.releaseShortcut
        :args:
            int
        :description: QtWidgets/QWidget-releaseShortcut-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.removeAction
        :args:
            :sip:ref:`~PyQt6.QtGui.QAction`
        :description: QtWidgets/QWidget-removeAction-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.render
        :args:
            :sip:ref:`~PyQt6.QtGui.QPaintDevice`
            targetOffset: :sip:ref:`~PyQt6.QtCore.QPoint` = QPoint()
            sourceRegion: :sip:ref:`~PyQt6.QtGui.QRegion` = QRegion()
            flags: :sip:ref:`~PyQt6.QtWidgets.QWidget.RenderFlag` = QWidget.RenderFlags(QWidget.DrawWindowBackground|QWidget.DrawChildren)
        :description: QtWidgets/QWidget-render-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.render
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            targetOffset: :sip:ref:`~PyQt6.QtCore.QPoint` = QPoint()
            sourceRegion: :sip:ref:`~PyQt6.QtGui.QRegion` = QRegion()
            flags: :sip:ref:`~PyQt6.QtWidgets.QWidget.RenderFlag` = QWidget.RenderFlags(QWidget.DrawWindowBackground|QWidget.DrawChildren)
        :description: QtWidgets/QWidget-render-f-3.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.repaint
        :description: QtWidgets/QWidget-repaint-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.repaint
        :args:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtWidgets/QWidget-repaint-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.repaint
        :args:
            :sip:ref:`~PyQt6.QtGui.QRegion`
        :description: QtWidgets/QWidget-repaint-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.repaint
        :args:
            int
            int
            int
            int
        :description: QtWidgets/QWidget-repaint-f-3.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.resize
        :args:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QWidget-resize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.resize
        :args:
            int
            int
        :description: QtWidgets/QWidget-resize-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.resizeEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QResizeEvent`
        :description: QtWidgets/QWidget-resizeEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.restoreGeometry
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            bool
        :description: QtWidgets/QWidget-restoreGeometry-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.saveGeometry
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtWidgets/QWidget-saveGeometry-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.screen
        :returns:
            :sip:ref:`~PyQt6.QtGui.QScreen`
        :description: QtWidgets/QWidget-screen-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.scroll
        :args:
            int
            int
        :description: QtWidgets/QWidget-scroll-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.scroll
        :args:
            int
            int
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtWidgets/QWidget-scroll-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setAcceptDrops
        :args:
            bool
        :description: QtWidgets/QWidget-setAcceptDrops-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setAccessibleDescription
        :args:
            Optional[str]
        :description: QtWidgets/QWidget-setAccessibleDescription-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setAccessibleName
        :args:
            Optional[str]
        :description: QtWidgets/QWidget-setAccessibleName-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setAttribute
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.WidgetAttribute`
            on: bool = True
        :description: QtWidgets/QWidget-setAttribute-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setAutoFillBackground
        :args:
            bool
        :description: QtWidgets/QWidget-setAutoFillBackground-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setBackgroundRole
        :args:
            :sip:ref:`~PyQt6.QtGui.QPalette.ColorRole`
        :description: QtWidgets/QWidget-setBackgroundRole-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setBaseSize
        :args:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QWidget-setBaseSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setBaseSize
        :args:
            int
            int
        :description: QtWidgets/QWidget-setBaseSize-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setContentsMargins
        :args:
            :sip:ref:`~PyQt6.QtCore.QMargins`
        :description: QtWidgets/QWidget-setContentsMargins-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setContentsMargins
        :args:
            int
            int
            int
            int
        :description: QtWidgets/QWidget-setContentsMargins-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setContextMenuPolicy
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.ContextMenuPolicy`
        :description: QtWidgets/QWidget-setContextMenuPolicy-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setCursor
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QCursor`, :sip:ref:`~PyQt6.QtCore.Qt.CursorShape`]
        :description: QtWidgets/QWidget-setCursor-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setDisabled
        :args:
            bool
        :description: QtWidgets/QWidget-setDisabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setEnabled
        :args:
            bool
        :description: QtWidgets/QWidget-setEnabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setFixedHeight
        :args:
            int
        :description: QtWidgets/QWidget-setFixedHeight-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setFixedSize
        :args:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QWidget-setFixedSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setFixedSize
        :args:
            int
            int
        :description: QtWidgets/QWidget-setFixedSize-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setFixedWidth
        :args:
            int
        :description: QtWidgets/QWidget-setFixedWidth-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setFocus
        :description: QtWidgets/QWidget-setFocus-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setFocus
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.FocusReason`
        :description: QtWidgets/QWidget-setFocus-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setFocusPolicy
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.FocusPolicy`
        :description: QtWidgets/QWidget-setFocusPolicy-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setFocusProxy
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QWidget-setFocusProxy-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setFont
        :args:
            :sip:ref:`~PyQt6.QtGui.QFont`
        :description: QtWidgets/QWidget-setFont-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setForegroundRole
        :args:
            :sip:ref:`~PyQt6.QtGui.QPalette.ColorRole`
        :description: QtWidgets/QWidget-setForegroundRole-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setGeometry
        :args:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtWidgets/QWidget-setGeometry-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setGeometry
        :args:
            int
            int
            int
            int
        :description: QtWidgets/QWidget-setGeometry-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setGraphicsEffect
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsEffect`
        :description: QtWidgets/QWidget-setGraphicsEffect-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setHidden
        :args:
            bool
        :description: QtWidgets/QWidget-setHidden-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setInputMethodHints
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.InputMethodHint`
        :description: QtWidgets/QWidget-setInputMethodHints-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setLayout
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QLayout`
        :description: QtWidgets/QWidget-setLayout-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setLayoutDirection
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.LayoutDirection`
        :description: QtWidgets/QWidget-setLayoutDirection-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setLocale
        :args:
            :sip:ref:`~PyQt6.QtCore.QLocale`
        :description: QtWidgets/QWidget-setLocale-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setMask
        :args:
            :sip:ref:`~PyQt6.QtGui.QBitmap`
        :description: QtWidgets/QWidget-setMask-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setMask
        :args:
            :sip:ref:`~PyQt6.QtGui.QRegion`
        :description: QtWidgets/QWidget-setMask-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setMaximumHeight
        :args:
            int
        :description: QtWidgets/QWidget-setMaximumHeight-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setMaximumSize
        :args:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QWidget-setMaximumSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setMaximumSize
        :args:
            int
            int
        :description: QtWidgets/QWidget-setMaximumSize-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setMaximumWidth
        :args:
            int
        :description: QtWidgets/QWidget-setMaximumWidth-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setMinimumHeight
        :args:
            int
        :description: QtWidgets/QWidget-setMinimumHeight-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setMinimumSize
        :args:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QWidget-setMinimumSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setMinimumSize
        :args:
            int
            int
        :description: QtWidgets/QWidget-setMinimumSize-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setMinimumWidth
        :args:
            int
        :description: QtWidgets/QWidget-setMinimumWidth-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setMouseTracking
        :args:
            bool
        :description: QtWidgets/QWidget-setMouseTracking-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setPalette
        :args:
            :sip:ref:`~PyQt6.QtGui.QPalette`
        :description: QtWidgets/QWidget-setPalette-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setParent
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QWidget-setParent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setParent
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            :sip:ref:`~PyQt6.QtCore.Qt.WindowType`
        :description: QtWidgets/QWidget-setParent-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setScreen
        :args:
            :sip:ref:`~PyQt6.QtGui.QScreen`
        :description: QtWidgets/QWidget-setScreen-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setShortcutAutoRepeat
        :args:
            int
            enabled: bool = True
        :description: QtWidgets/QWidget-setShortcutAutoRepeat-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setShortcutEnabled
        :args:
            int
            enabled: bool = True
        :description: QtWidgets/QWidget-setShortcutEnabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setSizeIncrement
        :args:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QWidget-setSizeIncrement-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setSizeIncrement
        :args:
            int
            int
        :description: QtWidgets/QWidget-setSizeIncrement-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setSizePolicy
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QSizePolicy`
        :description: QtWidgets/QWidget-setSizePolicy-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setSizePolicy
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QSizePolicy.Policy`
            :sip:ref:`~PyQt6.QtWidgets.QSizePolicy.Policy`
        :description: QtWidgets/QWidget-setSizePolicy-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setStatusTip
        :args:
            Optional[str]
        :description: QtWidgets/QWidget-setStatusTip-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setStyle
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QStyle`
        :description: QtWidgets/QWidget-setStyle-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setStyleSheet
        :args:
            Optional[str]
        :description: QtWidgets/QWidget-setStyleSheet-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setTabletTracking
        :args:
            bool
        :description: QtWidgets/QWidget-setTabletTracking-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setTabOrder
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :static:
        :description: QtWidgets/QWidget-setTabOrder-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setToolTip
        :args:
            Optional[str]
        :description: QtWidgets/QWidget-setToolTip-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setToolTipDuration
        :args:
            int
        :description: QtWidgets/QWidget-setToolTipDuration-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setUpdatesEnabled
        :args:
            bool
        :description: QtWidgets/QWidget-setUpdatesEnabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setVisible
        :args:
            bool
        :description: QtWidgets/QWidget-setVisible-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setWhatsThis
        :args:
            Optional[str]
        :description: QtWidgets/QWidget-setWhatsThis-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setWindowFilePath
        :args:
            Optional[str]
        :description: QtWidgets/QWidget-setWindowFilePath-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setWindowFlag
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.WindowType`
            on: bool = True
        :description: QtWidgets/QWidget-setWindowFlag-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setWindowFlags
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.WindowType`
        :description: QtWidgets/QWidget-setWindowFlags-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setWindowIcon
        :args:
            :sip:ref:`~PyQt6.QtGui.QIcon`
        :description: QtWidgets/QWidget-setWindowIcon-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setWindowIconText
        :args:
            Optional[str]
        :description: QtWidgets/QWidget-setWindowIconText-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setWindowModality
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.WindowModality`
        :description: QtWidgets/QWidget-setWindowModality-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setWindowModified
        :args:
            bool
        :description: QtWidgets/QWidget-setWindowModified-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setWindowOpacity
        :args:
            float
        :description: QtWidgets/QWidget-setWindowOpacity-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setWindowRole
        :args:
            Optional[str]
        :description: QtWidgets/QWidget-setWindowRole-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setWindowState
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.WindowState`
        :description: QtWidgets/QWidget-setWindowState-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.setWindowTitle
        :args:
            Optional[str]
        :description: QtWidgets/QWidget-setWindowTitle-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.sharedPainter
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPainter`
        :description: QtWidgets/QWidget-sharedPainter-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.show
        :description: QtWidgets/QWidget-show-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.showEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QShowEvent`
        :description: QtWidgets/QWidget-showEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.showFullScreen
        :description: QtWidgets/QWidget-showFullScreen-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.showMaximized
        :description: QtWidgets/QWidget-showMaximized-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.showMinimized
        :description: QtWidgets/QWidget-showMinimized-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.showNormal
        :description: QtWidgets/QWidget-showNormal-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.size
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QWidget-size-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.sizeHint
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QWidget-sizeHint-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.sizeIncrement
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QWidget-sizeIncrement-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.sizePolicy
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QSizePolicy`
        :description: QtWidgets/QWidget-sizePolicy-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.stackUnder
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QWidget-stackUnder-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.statusTip
        :returns:
            str
        :description: QtWidgets/QWidget-statusTip-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.style
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QStyle`
        :description: QtWidgets/QWidget-style-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.styleSheet
        :returns:
            str
        :description: QtWidgets/QWidget-styleSheet-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.tabletEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QTabletEvent`
        :description: QtWidgets/QWidget-tabletEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.testAttribute
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.WidgetAttribute`
        :returns:
            bool
        :description: QtWidgets/QWidget-testAttribute-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.toolTip
        :returns:
            str
        :description: QtWidgets/QWidget-toolTip-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.toolTipDuration
        :returns:
            int
        :description: QtWidgets/QWidget-toolTipDuration-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.underMouse
        :returns:
            bool
        :description: QtWidgets/QWidget-underMouse-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.ungrabGesture
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.GestureType`
        :description: QtWidgets/QWidget-ungrabGesture-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.unsetCursor
        :description: QtWidgets/QWidget-unsetCursor-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.unsetLayoutDirection
        :description: QtWidgets/QWidget-unsetLayoutDirection-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.unsetLocale
        :description: QtWidgets/QWidget-unsetLocale-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.update
        :description: QtWidgets/QWidget-update-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.update
        :args:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtWidgets/QWidget-update-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.update
        :args:
            :sip:ref:`~PyQt6.QtGui.QRegion`
        :description: QtWidgets/QWidget-update-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.update
        :args:
            int
            int
            int
            int
        :description: QtWidgets/QWidget-update-f-3.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.updateGeometry
        :description: QtWidgets/QWidget-updateGeometry-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.updateMicroFocus
        :args:
            query: :sip:ref:`~PyQt6.QtCore.Qt.InputMethodQuery` = :sip:ref:`~PyQt6.QtCore.Qt.InputMethodQuery.ImQueryAll`
        :description: QtWidgets/QWidget-updateMicroFocus-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.updatesEnabled
        :returns:
            bool
        :description: QtWidgets/QWidget-updatesEnabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.visibleRegion
        :returns:
            :sip:ref:`~PyQt6.QtGui.QRegion`
        :description: QtWidgets/QWidget-visibleRegion-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.whatsThis
        :returns:
            str
        :description: QtWidgets/QWidget-whatsThis-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.wheelEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QWheelEvent`
        :description: QtWidgets/QWidget-wheelEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.width
        :returns:
            int
        :description: QtWidgets/QWidget-width-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.window
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QWidget-window-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.windowFilePath
        :returns:
            str
        :description: QtWidgets/QWidget-windowFilePath-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.windowFlags
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.WindowType`
        :description: QtWidgets/QWidget-windowFlags-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.windowHandle
        :returns:
            :sip:ref:`~PyQt6.QtGui.QWindow`
        :description: QtWidgets/QWidget-windowHandle-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.windowIcon
        :returns:
            :sip:ref:`~PyQt6.QtGui.QIcon`
        :description: QtWidgets/QWidget-windowIcon-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.windowIconText
        :returns:
            str
        :description: QtWidgets/QWidget-windowIconText-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.windowModality
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.WindowModality`
        :description: QtWidgets/QWidget-windowModality-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.windowOpacity
        :returns:
            float
        :description: QtWidgets/QWidget-windowOpacity-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.windowRole
        :returns:
            str
        :description: QtWidgets/QWidget-windowRole-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.windowState
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.WindowState`
        :description: QtWidgets/QWidget-windowState-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.windowTitle
        :returns:
            str
        :description: QtWidgets/QWidget-windowTitle-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.windowType
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.WindowType`
        :description: QtWidgets/QWidget-windowType-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.winId
        :returns:
            :py:class:`~PyQt6.sip.voidptr`
        :description: QtWidgets/QWidget-winId-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.x
        :returns:
            int
        :description: QtWidgets/QWidget-x-f.rst

    .. sip:method:: PyQt6.QtWidgets.QWidget.y
        :returns:
            int
        :description: QtWidgets/QWidget-y-f.rst

    .. sip:signal:: PyQt6.QtWidgets.QWidget.customContextMenuRequested
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :description: QtWidgets/QWidget-customContextMenuRequested-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QWidget.windowIconChanged
        :args:
            :sip:ref:`~PyQt6.QtGui.QIcon`
        :description: QtWidgets/QWidget-windowIconChanged-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QWidget.windowIconTextChanged
        :args:
            Optional[str]
        :description: QtWidgets/QWidget-windowIconTextChanged-s-1.rst

    .. sip:signal:: PyQt6.QtWidgets.QWidget.windowTitleChanged
        :args:
            Optional[str]
        :description: QtWidgets/QWidget-windowTitleChanged-s-1.rst
