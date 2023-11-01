:orphan:

.. sip:class:: PyQt6.QtWidgets.QSplitter
    :inherits: :sip:ref:`~PyQt6.QtWidgets.QFrame`
    :description: QtWidgets/QSplitter-c.rst

    .. sip:method:: PyQt6.QtWidgets.QSplitter.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :description: QtWidgets/QSplitter-__init__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSplitter.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.Orientation`
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :description: QtWidgets/QSplitter-__init__-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QSplitter.addWidget
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QSplitter-addWidget-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSplitter.changeEvent
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :description: QtWidgets/QSplitter-changeEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSplitter.childEvent
        :args:
            :sip:ref:`~PyQt6.QtCore.QChildEvent`
        :description: QtWidgets/QSplitter-childEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSplitter.childrenCollapsible
        :returns:
            bool
        :description: QtWidgets/QSplitter-childrenCollapsible-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSplitter.closestLegalPosition
        :args:
            int
            int
        :returns:
            int
        :description: QtWidgets/QSplitter-closestLegalPosition-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSplitter.count
        :returns:
            int
        :description: QtWidgets/QSplitter-count-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSplitter.createHandle
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QSplitterHandle`
        :description: QtWidgets/QSplitter-createHandle-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSplitter.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtWidgets/QSplitter-event-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSplitter.getRange
        :args:
            int
        :returns:
            int
            int
        :description: QtWidgets/QSplitter-getRange-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSplitter.handle
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QSplitterHandle`
        :description: QtWidgets/QSplitter-handle-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSplitter.handleWidth
        :returns:
            int
        :description: QtWidgets/QSplitter-handleWidth-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSplitter.indexOf
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :returns:
            int
        :description: QtWidgets/QSplitter-indexOf-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSplitter.insertWidget
        :args:
            int
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QSplitter-insertWidget-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSplitter.isCollapsible
        :args:
            int
        :returns:
            bool
        :description: QtWidgets/QSplitter-isCollapsible-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSplitter.__len__
        :returns:
            int
        :description: QtWidgets/QSplitter-__len__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSplitter.minimumSizeHint
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QSplitter-minimumSizeHint-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSplitter.moveSplitter
        :args:
            int
            int
        :description: QtWidgets/QSplitter-moveSplitter-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSplitter.opaqueResize
        :returns:
            bool
        :description: QtWidgets/QSplitter-opaqueResize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSplitter.orientation
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.Orientation`
        :description: QtWidgets/QSplitter-orientation-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QSplitter.refresh
        :description: QtWidgets/QSplitter-refresh-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSplitter.replaceWidget
        :args:
            int
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QSplitter-replaceWidget-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSplitter.resizeEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QResizeEvent`
        :description: QtWidgets/QSplitter-resizeEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSplitter.restoreState
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            bool
        :description: QtWidgets/QSplitter-restoreState-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QSplitter.saveState
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtWidgets/QSplitter-saveState-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSplitter.setChildrenCollapsible
        :args:
            bool
        :description: QtWidgets/QSplitter-setChildrenCollapsible-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSplitter.setCollapsible
        :args:
            int
            bool
        :description: QtWidgets/QSplitter-setCollapsible-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSplitter.setHandleWidth
        :args:
            int
        :description: QtWidgets/QSplitter-setHandleWidth-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSplitter.setOpaqueResize
        :args:
            opaque: bool = True
        :description: QtWidgets/QSplitter-setOpaqueResize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSplitter.setOrientation
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.Orientation`
        :description: QtWidgets/QSplitter-setOrientation-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QSplitter.setRubberBand
        :args:
            int
        :description: QtWidgets/QSplitter-setRubberBand-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSplitter.setSizes
        :args:
            Iterable[int]
        :description: QtWidgets/QSplitter-setSizes-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSplitter.setStretchFactor
        :args:
            int
            int
        :description: QtWidgets/QSplitter-setStretchFactor-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSplitter.sizeHint
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QSplitter-sizeHint-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSplitter.sizes
        :returns:
            List[int]
        :description: QtWidgets/QSplitter-sizes-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSplitter.widget
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QSplitter-widget-f.rst

    .. sip:signal:: PyQt6.QtWidgets.QSplitter.splitterMoved
        :args:
            int
            int
        :description: QtWidgets/QSplitter-splitterMoved-s.rst
