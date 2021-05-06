:orphan:

.. sip:class:: PyQt6.QtWidgets.QAbstractScrollArea
    :inherits: :sip:ref:`~PyQt6.QtWidgets.QFrame`
    :description: QtWidgets/QAbstractScrollArea-c.rst

    .. sip:enum:: PyQt6.QtWidgets.QAbstractScrollArea.SizeAdjustPolicy
        :description: QtWidgets/QAbstractScrollArea-SizeAdjustPolicy-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored
            :description: QtWidgets/QAbstractScrollArea-SizeAdjustPolicy-AdjustIgnored-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents
            :description: QtWidgets/QAbstractScrollArea-SizeAdjustPolicy-AdjustToContents-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow
            :description: QtWidgets/QAbstractScrollArea-SizeAdjustPolicy-AdjustToContentsOnFirstShow-v.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :description: QtWidgets/QAbstractScrollArea-__init__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.addScrollBarWidget
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            :sip:ref:`~PyQt6.QtCore.Qt.AlignmentFlag`
        :description: QtWidgets/QAbstractScrollArea-addScrollBarWidget-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.contextMenuEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QContextMenuEvent`
        :description: QtWidgets/QAbstractScrollArea-contextMenuEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.cornerWidget
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QAbstractScrollArea-cornerWidget-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.dragEnterEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QDragEnterEvent`
        :description: QtWidgets/QAbstractScrollArea-dragEnterEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.dragLeaveEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QDragLeaveEvent`
        :description: QtWidgets/QAbstractScrollArea-dragLeaveEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.dragMoveEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QDragMoveEvent`
        :description: QtWidgets/QAbstractScrollArea-dragMoveEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.dropEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QDropEvent`
        :description: QtWidgets/QAbstractScrollArea-dropEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtWidgets/QAbstractScrollArea-event-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.eventFilter
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtWidgets/QAbstractScrollArea-eventFilter-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.horizontalScrollBar
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QScrollBar`
        :description: QtWidgets/QAbstractScrollArea-horizontalScrollBar-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.horizontalScrollBarPolicy
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.ScrollBarPolicy`
        :description: QtWidgets/QAbstractScrollArea-horizontalScrollBarPolicy-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.keyPressEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QKeyEvent`
        :description: QtWidgets/QAbstractScrollArea-keyPressEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.maximumViewportSize
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QAbstractScrollArea-maximumViewportSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.minimumSizeHint
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QAbstractScrollArea-minimumSizeHint-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.mouseDoubleClickEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtWidgets/QAbstractScrollArea-mouseDoubleClickEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.mouseMoveEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtWidgets/QAbstractScrollArea-mouseMoveEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.mousePressEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtWidgets/QAbstractScrollArea-mousePressEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.mouseReleaseEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtWidgets/QAbstractScrollArea-mouseReleaseEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.paintEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QPaintEvent`
        :description: QtWidgets/QAbstractScrollArea-paintEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.resizeEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QResizeEvent`
        :description: QtWidgets/QAbstractScrollArea-resizeEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.scrollBarWidgets
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.AlignmentFlag`
        :returns:
            List[:sip:ref:`~PyQt6.QtWidgets.QWidget`]
        :description: QtWidgets/QAbstractScrollArea-scrollBarWidgets-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.scrollContentsBy
        :args:
            int
            int
        :description: QtWidgets/QAbstractScrollArea-scrollContentsBy-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.setCornerWidget
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QAbstractScrollArea-setCornerWidget-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.setHorizontalScrollBar
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QScrollBar`
        :description: QtWidgets/QAbstractScrollArea-setHorizontalScrollBar-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.setHorizontalScrollBarPolicy
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.ScrollBarPolicy`
        :description: QtWidgets/QAbstractScrollArea-setHorizontalScrollBarPolicy-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.setSizeAdjustPolicy
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.SizeAdjustPolicy`
        :description: QtWidgets/QAbstractScrollArea-setSizeAdjustPolicy-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.setupViewport
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QAbstractScrollArea-setupViewport-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.setVerticalScrollBar
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QScrollBar`
        :description: QtWidgets/QAbstractScrollArea-setVerticalScrollBar-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.setVerticalScrollBarPolicy
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.ScrollBarPolicy`
        :description: QtWidgets/QAbstractScrollArea-setVerticalScrollBarPolicy-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.setViewport
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QAbstractScrollArea-setViewport-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.setViewportMargins
        :args:
            :sip:ref:`~PyQt6.QtCore.QMargins`
        :description: QtWidgets/QAbstractScrollArea-setViewportMargins-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.setViewportMargins
        :args:
            int
            int
            int
            int
        :description: QtWidgets/QAbstractScrollArea-setViewportMargins-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.sizeAdjustPolicy
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea.SizeAdjustPolicy`
        :description: QtWidgets/QAbstractScrollArea-sizeAdjustPolicy-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.sizeHint
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QAbstractScrollArea-sizeHint-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.verticalScrollBar
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QScrollBar`
        :description: QtWidgets/QAbstractScrollArea-verticalScrollBar-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.verticalScrollBarPolicy
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.ScrollBarPolicy`
        :description: QtWidgets/QAbstractScrollArea-verticalScrollBarPolicy-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.viewport
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QAbstractScrollArea-viewport-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.viewportEvent
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtWidgets/QAbstractScrollArea-viewportEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.viewportMargins
        :returns:
            :sip:ref:`~PyQt6.QtCore.QMargins`
        :description: QtWidgets/QAbstractScrollArea-viewportMargins-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.viewportSizeHint
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QAbstractScrollArea-viewportSizeHint-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractScrollArea.wheelEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QWheelEvent`
        :description: QtWidgets/QAbstractScrollArea-wheelEvent-f.rst
