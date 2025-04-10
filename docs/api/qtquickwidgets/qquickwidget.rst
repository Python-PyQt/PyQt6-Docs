:orphan:

.. sip:class:: PyQt6.QtQuickWidgets.QQuickWidget
    :inherits: :sip:ref:`~PyQt6.QtWidgets.QWidget`
    :description: QtQuickWidgets/QQuickWidget-c.rst

    .. sip:enum:: PyQt6.QtQuickWidgets.QQuickWidget.ResizeMode
        :description: QtQuickWidgets/QQuickWidget-ResizeMode-e.rst

        .. sip:enum-member:: PyQt6.QtQuickWidgets.QQuickWidget.ResizeMode.SizeRootObjectToView
            :description: QtQuickWidgets/QQuickWidget-ResizeMode-SizeRootObjectToView-v.rst

        .. sip:enum-member:: PyQt6.QtQuickWidgets.QQuickWidget.ResizeMode.SizeViewToRootObject
            :description: QtQuickWidgets/QQuickWidget-ResizeMode-SizeViewToRootObject-v.rst

    .. sip:enum:: PyQt6.QtQuickWidgets.QQuickWidget.Status
        :description: QtQuickWidgets/QQuickWidget-Status-e.rst

        .. sip:enum-member:: PyQt6.QtQuickWidgets.QQuickWidget.Status.Error
            :description: QtQuickWidgets/QQuickWidget-Status-Error-v.rst

        .. sip:enum-member:: PyQt6.QtQuickWidgets.QQuickWidget.Status.Loading
            :description: QtQuickWidgets/QQuickWidget-Status-Loading-v.rst

        .. sip:enum-member:: PyQt6.QtQuickWidgets.QQuickWidget.Status.Null
            :description: QtQuickWidgets/QQuickWidget-Status-Null-v.rst

        .. sip:enum-member:: PyQt6.QtQuickWidgets.QQuickWidget.Status.Ready
            :description: QtQuickWidgets/QQuickWidget-Status-Ready-v.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :description: QtQuickWidgets/QQuickWidget-__init__-f.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.__init__
        :args:
            :sip:ref:`~PyQt6.QtQml.QQmlEngine`
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtQuickWidgets/QQuickWidget-__init__-f-1.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :description: QtQuickWidgets/QQuickWidget-__init__-f-2.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.__init__
        :args:
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :description: QtQuickWidgets/QQuickWidget-__init__-f-3.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.dragEnterEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QDragEnterEvent`
        :description: QtQuickWidgets/QQuickWidget-dragEnterEvent-f.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.dragLeaveEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QDragLeaveEvent`
        :description: QtQuickWidgets/QQuickWidget-dragLeaveEvent-f.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.dragMoveEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QDragMoveEvent`
        :description: QtQuickWidgets/QQuickWidget-dragMoveEvent-f.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.dropEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QDropEvent`
        :description: QtQuickWidgets/QQuickWidget-dropEvent-f.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.engine
        :returns:
            :sip:ref:`~PyQt6.QtQml.QQmlEngine`
        :description: QtQuickWidgets/QQuickWidget-engine-f.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.errors
        :returns:
            list[:sip:ref:`~PyQt6.QtQml.QQmlError`]
        :description: QtQuickWidgets/QQuickWidget-errors-f-1.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtQuickWidgets/QQuickWidget-event-f.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.focusInEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QFocusEvent`
        :description: QtQuickWidgets/QQuickWidget-focusInEvent-f.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.focusNextPrevChild
        :args:
            bool
        :returns:
            bool
        :description: QtQuickWidgets/QQuickWidget-focusNextPrevChild-f.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.focusOutEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QFocusEvent`
        :description: QtQuickWidgets/QQuickWidget-focusOutEvent-f.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.format
        :returns:
            :sip:ref:`~PyQt6.QtGui.QSurfaceFormat`
        :description: QtQuickWidgets/QQuickWidget-format-f.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.grabFramebuffer
        :returns:
            :sip:ref:`~PyQt6.QtGui.QImage`
        :description: QtQuickWidgets/QQuickWidget-grabFramebuffer-f.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.hideEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QHideEvent`
        :description: QtQuickWidgets/QQuickWidget-hideEvent-f.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.initialSize
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtQuickWidgets/QQuickWidget-initialSize-f.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.keyPressEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QKeyEvent`
        :description: QtQuickWidgets/QQuickWidget-keyPressEvent-f.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.keyReleaseEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QKeyEvent`
        :description: QtQuickWidgets/QQuickWidget-keyReleaseEvent-f.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.loadFromModule
        :args:
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
        :description: QtQuickWidgets/QQuickWidget-loadFromModule-f.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.mouseDoubleClickEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtQuickWidgets/QQuickWidget-mouseDoubleClickEvent-f.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.mouseMoveEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtQuickWidgets/QQuickWidget-mouseMoveEvent-f.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.mousePressEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtQuickWidgets/QQuickWidget-mousePressEvent-f.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.mouseReleaseEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtQuickWidgets/QQuickWidget-mouseReleaseEvent-f.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.paintEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QPaintEvent`
        :description: QtQuickWidgets/QQuickWidget-paintEvent-f.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.quickWindow
        :returns:
            :sip:ref:`~PyQt6.QtQuick.QQuickWindow`
        :description: QtQuickWidgets/QQuickWidget-quickWindow-f.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.resizeEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QResizeEvent`
        :description: QtQuickWidgets/QQuickWidget-resizeEvent-f.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.resizeMode
        :returns:
            :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget.ResizeMode`
        :description: QtQuickWidgets/QQuickWidget-resizeMode-f.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.rootContext
        :returns:
            :sip:ref:`~PyQt6.QtQml.QQmlContext`
        :description: QtQuickWidgets/QQuickWidget-rootContext-f.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.rootObject
        :returns:
            :sip:ref:`~PyQt6.QtQuick.QQuickItem`
        :description: QtQuickWidgets/QQuickWidget-rootObject-f.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.setClearColor
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
        :description: QtQuickWidgets/QQuickWidget-setClearColor-f-1.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.setFormat
        :args:
            :sip:ref:`~PyQt6.QtGui.QSurfaceFormat`
        :description: QtQuickWidgets/QQuickWidget-setFormat-f.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.setInitialProperties
        :args:
            dict[Optional[str], Any]
        :description: QtQuickWidgets/QQuickWidget-setInitialProperties-f.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.setResizeMode
        :args:
            :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget.ResizeMode`
        :description: QtQuickWidgets/QQuickWidget-setResizeMode-f.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.setSource
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtQuickWidgets/QQuickWidget-setSource-f.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.showEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QShowEvent`
        :description: QtQuickWidgets/QQuickWidget-showEvent-f.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.sizeHint
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtQuickWidgets/QQuickWidget-sizeHint-f.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.source
        :returns:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtQuickWidgets/QQuickWidget-source-f.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.status
        :returns:
            :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget.Status`
        :description: QtQuickWidgets/QQuickWidget-status-f.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.timerEvent
        :args:
            :sip:ref:`~PyQt6.QtCore.QTimerEvent`
        :description: QtQuickWidgets/QQuickWidget-timerEvent-f.rst

    .. sip:method:: PyQt6.QtQuickWidgets.QQuickWidget.wheelEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QWheelEvent`
        :description: QtQuickWidgets/QQuickWidget-wheelEvent-f.rst

    .. sip:signal:: PyQt6.QtQuickWidgets.QQuickWidget.sceneGraphError
        :args:
            :sip:ref:`~PyQt6.QtQuick.QQuickWindow.SceneGraphError`
            Optional[str]
        :description: QtQuickWidgets/QQuickWidget-sceneGraphError-s-1.rst

    .. sip:signal:: PyQt6.QtQuickWidgets.QQuickWidget.statusChanged
        :args:
            :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget.Status`
        :description: QtQuickWidgets/QQuickWidget-statusChanged-s.rst
