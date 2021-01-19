:orphan:

.. sip:class:: PyQt6.QtWidgets.QColumnView
    :inherits: :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView`
    :description: QtWidgets/QColumnView-c.rst

    .. sip:method:: PyQt6.QtWidgets.QColumnView.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :description: QtWidgets/QColumnView-__init__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QColumnView.columnWidths
        :returns:
            List[int]
        :description: QtWidgets/QColumnView-columnWidths-f.rst

    .. sip:method:: PyQt6.QtWidgets.QColumnView.createColumn
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView`
        :description: QtWidgets/QColumnView-createColumn-f.rst

    .. sip:method:: PyQt6.QtWidgets.QColumnView.currentChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QColumnView-currentChanged-f.rst

    .. sip:method:: PyQt6.QtWidgets.QColumnView.horizontalOffset
        :returns:
            int
        :description: QtWidgets/QColumnView-horizontalOffset-f.rst

    .. sip:method:: PyQt6.QtWidgets.QColumnView.indexAt
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QColumnView-indexAt-f.rst

    .. sip:method:: PyQt6.QtWidgets.QColumnView.initializeColumn
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView`
        :description: QtWidgets/QColumnView-initializeColumn-f.rst

    .. sip:method:: PyQt6.QtWidgets.QColumnView.isIndexHidden
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            bool
        :description: QtWidgets/QColumnView-isIndexHidden-f.rst

    .. sip:method:: PyQt6.QtWidgets.QColumnView.moveCursor
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.CursorAction`
            :sip:ref:`~PyQt6.QtCore.Qt.KeyboardModifiers`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QColumnView-moveCursor-f.rst

    .. sip:method:: PyQt6.QtWidgets.QColumnView.previewWidget
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QColumnView-previewWidget-f.rst

    .. sip:method:: PyQt6.QtWidgets.QColumnView.resizeEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QResizeEvent`
        :description: QtWidgets/QColumnView-resizeEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QColumnView.resizeGripsVisible
        :returns:
            bool
        :description: QtWidgets/QColumnView-resizeGripsVisible-f.rst

    .. sip:method:: PyQt6.QtWidgets.QColumnView.rowsInserted
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            int
        :description: QtWidgets/QColumnView-rowsInserted-f.rst

    .. sip:method:: PyQt6.QtWidgets.QColumnView.scrollContentsBy
        :args:
            int
            int
        :description: QtWidgets/QColumnView-scrollContentsBy-f.rst

    .. sip:method:: PyQt6.QtWidgets.QColumnView.scrollTo
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            hint: :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.ScrollHint` = :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.ScrollHint.EnsureVisible`
        :description: QtWidgets/QColumnView-scrollTo-f.rst

    .. sip:method:: PyQt6.QtWidgets.QColumnView.selectAll
        :description: QtWidgets/QColumnView-selectAll-f.rst

    .. sip:method:: PyQt6.QtWidgets.QColumnView.setColumnWidths
        :args:
            Iterable[int]
        :description: QtWidgets/QColumnView-setColumnWidths-f.rst

    .. sip:method:: PyQt6.QtWidgets.QColumnView.setModel
        :args:
            :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`
        :description: QtWidgets/QColumnView-setModel-f.rst

    .. sip:method:: PyQt6.QtWidgets.QColumnView.setPreviewWidget
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QColumnView-setPreviewWidget-f.rst

    .. sip:method:: PyQt6.QtWidgets.QColumnView.setResizeGripsVisible
        :args:
            bool
        :description: QtWidgets/QColumnView-setResizeGripsVisible-f.rst

    .. sip:method:: PyQt6.QtWidgets.QColumnView.setRootIndex
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QColumnView-setRootIndex-f.rst

    .. sip:method:: PyQt6.QtWidgets.QColumnView.setSelection
        :args:
            :sip:ref:`~PyQt6.QtCore.QRect`
            :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.SelectionFlags`
        :description: QtWidgets/QColumnView-setSelection-f.rst

    .. sip:method:: PyQt6.QtWidgets.QColumnView.setSelectionModel
        :args:
            :sip:ref:`~PyQt6.QtCore.QItemSelectionModel`
        :description: QtWidgets/QColumnView-setSelectionModel-f.rst

    .. sip:method:: PyQt6.QtWidgets.QColumnView.sizeHint
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QColumnView-sizeHint-f.rst

    .. sip:method:: PyQt6.QtWidgets.QColumnView.verticalOffset
        :returns:
            int
        :description: QtWidgets/QColumnView-verticalOffset-f.rst

    .. sip:method:: PyQt6.QtWidgets.QColumnView.visualRect
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtWidgets/QColumnView-visualRect-f.rst

    .. sip:method:: PyQt6.QtWidgets.QColumnView.visualRegionForSelection
        :args:
            :sip:ref:`~PyQt6.QtCore.QItemSelection`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QRegion`
        :description: QtWidgets/QColumnView-visualRegionForSelection-f.rst

    .. sip:signal:: PyQt6.QtWidgets.QColumnView.updatePreviewWidget
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QColumnView-updatePreviewWidget-s.rst
