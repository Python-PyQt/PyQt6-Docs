:orphan:

.. sip:class:: PyQt6.QtWidgets.QListView
    :inherits: :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView`
    :description: QtWidgets/QListView-c.rst

    .. sip:enum:: PyQt6.QtWidgets.QListView.Flow
        :description: QtWidgets/QListView-Flow-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QListView.Flow.LeftToRight
            :description: QtWidgets/QListView-Flow-LeftToRight-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QListView.Flow.TopToBottom
            :description: QtWidgets/QListView-Flow-TopToBottom-v.rst

    .. sip:enum:: PyQt6.QtWidgets.QListView.LayoutMode
        :description: QtWidgets/QListView-LayoutMode-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QListView.LayoutMode.Batched
            :description: QtWidgets/QListView-LayoutMode-Batched-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QListView.LayoutMode.SinglePass
            :description: QtWidgets/QListView-LayoutMode-SinglePass-v.rst

    .. sip:enum:: PyQt6.QtWidgets.QListView.Movement
        :description: QtWidgets/QListView-Movement-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QListView.Movement.Free
            :description: QtWidgets/QListView-Movement-Free-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QListView.Movement.Snap
            :description: QtWidgets/QListView-Movement-Snap-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QListView.Movement.Static
            :description: QtWidgets/QListView-Movement-Static-v.rst

    .. sip:enum:: PyQt6.QtWidgets.QListView.ResizeMode
        :description: QtWidgets/QListView-ResizeMode-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QListView.ResizeMode.Adjust
            :description: QtWidgets/QListView-ResizeMode-Adjust-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QListView.ResizeMode.Fixed
            :description: QtWidgets/QListView-ResizeMode-Fixed-v.rst

    .. sip:enum:: PyQt6.QtWidgets.QListView.ViewMode
        :description: QtWidgets/QListView-ViewMode-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QListView.ViewMode.IconMode
            :description: QtWidgets/QListView-ViewMode-IconMode-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QListView.ViewMode.ListMode
            :description: QtWidgets/QListView-ViewMode-ListMode-v.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :description: QtWidgets/QListView-__init__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.batchSize
        :returns:
            int
        :description: QtWidgets/QListView-batchSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.clearPropertyFlags
        :description: QtWidgets/QListView-clearPropertyFlags-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.currentChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QListView-currentChanged-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.dataChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            roles: Iterable[int] = []
        :description: QtWidgets/QListView-dataChanged-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.dragLeaveEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QDragLeaveEvent`
        :description: QtWidgets/QListView-dragLeaveEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.dragMoveEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QDragMoveEvent`
        :description: QtWidgets/QListView-dragMoveEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.dropEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QDropEvent`
        :description: QtWidgets/QListView-dropEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtWidgets/QListView-event-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.flow
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QListView.Flow`
        :description: QtWidgets/QListView-flow-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.gridSize
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QListView-gridSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.horizontalOffset
        :returns:
            int
        :description: QtWidgets/QListView-horizontalOffset-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.indexAt
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QListView-indexAt-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.initViewItemOption
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QStyleOptionViewItem`
        :description: QtWidgets/QListView-initViewItemOption-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.isIndexHidden
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            bool
        :description: QtWidgets/QListView-isIndexHidden-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.isRowHidden
        :args:
            int
        :returns:
            bool
        :description: QtWidgets/QListView-isRowHidden-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.isSelectionRectVisible
        :returns:
            bool
        :description: QtWidgets/QListView-isSelectionRectVisible-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.isWrapping
        :returns:
            bool
        :description: QtWidgets/QListView-isWrapping-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.itemAlignment
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.AlignmentFlag`
        :description: QtWidgets/QListView-itemAlignment-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.layoutMode
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QListView.LayoutMode`
        :description: QtWidgets/QListView-layoutMode-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.modelColumn
        :returns:
            int
        :description: QtWidgets/QListView-modelColumn-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.mouseMoveEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtWidgets/QListView-mouseMoveEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.mouseReleaseEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtWidgets/QListView-mouseReleaseEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.moveCursor
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.CursorAction`
            :sip:ref:`~PyQt6.QtCore.Qt.KeyboardModifier`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QListView-moveCursor-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.movement
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QListView.Movement`
        :description: QtWidgets/QListView-movement-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.paintEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QPaintEvent`
        :description: QtWidgets/QListView-paintEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.rectForIndex
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtWidgets/QListView-rectForIndex-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.reset
        :description: QtWidgets/QListView-reset-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.resizeEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QResizeEvent`
        :description: QtWidgets/QListView-resizeEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.resizeMode
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QListView.ResizeMode`
        :description: QtWidgets/QListView-resizeMode-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.rowsAboutToBeRemoved
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            int
        :description: QtWidgets/QListView-rowsAboutToBeRemoved-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.rowsInserted
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            int
        :description: QtWidgets/QListView-rowsInserted-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.scrollContentsBy
        :args:
            int
            int
        :description: QtWidgets/QListView-scrollContentsBy-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.scrollTo
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            hint: :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.ScrollHint` = :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.ScrollHint.EnsureVisible`
        :description: QtWidgets/QListView-scrollTo-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.selectedIndexes
        :returns:
            list[:sip:ref:`~PyQt6.QtCore.QModelIndex`]
        :description: QtWidgets/QListView-selectedIndexes-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.selectionChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QItemSelection`
            :sip:ref:`~PyQt6.QtCore.QItemSelection`
        :description: QtWidgets/QListView-selectionChanged-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.setBatchSize
        :args:
            int
        :description: QtWidgets/QListView-setBatchSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.setFlow
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QListView.Flow`
        :description: QtWidgets/QListView-setFlow-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.setGridSize
        :args:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QListView-setGridSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.setItemAlignment
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.AlignmentFlag`
        :description: QtWidgets/QListView-setItemAlignment-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.setLayoutMode
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QListView.LayoutMode`
        :description: QtWidgets/QListView-setLayoutMode-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.setModelColumn
        :args:
            int
        :description: QtWidgets/QListView-setModelColumn-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.setMovement
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QListView.Movement`
        :description: QtWidgets/QListView-setMovement-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.setPositionForIndex
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QListView-setPositionForIndex-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.setResizeMode
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QListView.ResizeMode`
        :description: QtWidgets/QListView-setResizeMode-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.setRootIndex
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QListView-setRootIndex-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.setRowHidden
        :args:
            int
            bool
        :description: QtWidgets/QListView-setRowHidden-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.setSelection
        :args:
            :sip:ref:`~PyQt6.QtCore.QRect`
            :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.SelectionFlag`
        :description: QtWidgets/QListView-setSelection-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.setSelectionRectVisible
        :args:
            bool
        :description: QtWidgets/QListView-setSelectionRectVisible-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.setSpacing
        :args:
            int
        :description: QtWidgets/QListView-setSpacing-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.setUniformItemSizes
        :args:
            bool
        :description: QtWidgets/QListView-setUniformItemSizes-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.setViewMode
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QListView.ViewMode`
        :description: QtWidgets/QListView-setViewMode-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.setWordWrap
        :args:
            bool
        :description: QtWidgets/QListView-setWordWrap-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.setWrapping
        :args:
            bool
        :description: QtWidgets/QListView-setWrapping-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.spacing
        :returns:
            int
        :description: QtWidgets/QListView-spacing-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.startDrag
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.DropAction`
        :description: QtWidgets/QListView-startDrag-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.timerEvent
        :args:
            :sip:ref:`~PyQt6.QtCore.QTimerEvent`
        :description: QtWidgets/QListView-timerEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.uniformItemSizes
        :returns:
            bool
        :description: QtWidgets/QListView-uniformItemSizes-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.updateGeometries
        :description: QtWidgets/QListView-updateGeometries-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.verticalOffset
        :returns:
            int
        :description: QtWidgets/QListView-verticalOffset-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.viewMode
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QListView.ViewMode`
        :description: QtWidgets/QListView-viewMode-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.viewportSizeHint
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QListView-viewportSizeHint-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.visualRect
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtWidgets/QListView-visualRect-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.visualRegionForSelection
        :args:
            :sip:ref:`~PyQt6.QtCore.QItemSelection`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QRegion`
        :description: QtWidgets/QListView-visualRegionForSelection-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.wheelEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QWheelEvent`
        :description: QtWidgets/QListView-wheelEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListView.wordWrap
        :returns:
            bool
        :description: QtWidgets/QListView-wordWrap-f.rst

    .. sip:signal:: PyQt6.QtWidgets.QListView.indexesMoved
        :args:
            Iterable[:sip:ref:`~PyQt6.QtCore.QModelIndex`]
        :description: QtWidgets/QListView-indexesMoved-s.rst
