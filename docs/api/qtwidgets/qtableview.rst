:orphan:

.. sip:class:: PyQt6.QtWidgets.QTableView
    :inherits: :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView`
    :description: QtWidgets/QTableView-c.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :description: QtWidgets/QTableView-__init__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.clearSpans
        :description: QtWidgets/QTableView-clearSpans-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.columnAt
        :args:
            int
        :returns:
            int
        :description: QtWidgets/QTableView-columnAt-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.columnCountChanged
        :args:
            int
            int
        :description: QtWidgets/QTableView-columnCountChanged-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.columnMoved
        :args:
            int
            int
            int
        :description: QtWidgets/QTableView-columnMoved-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.columnResized
        :args:
            int
            int
            int
        :description: QtWidgets/QTableView-columnResized-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.columnSpan
        :args:
            int
            int
        :returns:
            int
        :description: QtWidgets/QTableView-columnSpan-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.columnViewportPosition
        :args:
            int
        :returns:
            int
        :description: QtWidgets/QTableView-columnViewportPosition-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.columnWidth
        :args:
            int
        :returns:
            int
        :description: QtWidgets/QTableView-columnWidth-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.currentChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QTableView-currentChanged-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.dropEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QDropEvent`
        :description: QtWidgets/QTableView-dropEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.gridStyle
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.PenStyle`
        :description: QtWidgets/QTableView-gridStyle-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.hideColumn
        :args:
            int
        :description: QtWidgets/QTableView-hideColumn-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.hideRow
        :args:
            int
        :description: QtWidgets/QTableView-hideRow-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.horizontalHeader
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QHeaderView`
        :description: QtWidgets/QTableView-horizontalHeader-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.horizontalOffset
        :returns:
            int
        :description: QtWidgets/QTableView-horizontalOffset-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.horizontalScrollbarAction
        :args:
            int
        :description: QtWidgets/QTableView-horizontalScrollbarAction-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.indexAt
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QTableView-indexAt-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.initViewItemOption
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QStyleOptionViewItem`
        :description: QtWidgets/QTableView-initViewItemOption-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.isColumnHidden
        :args:
            int
        :returns:
            bool
        :description: QtWidgets/QTableView-isColumnHidden-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.isCornerButtonEnabled
        :returns:
            bool
        :description: QtWidgets/QTableView-isCornerButtonEnabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.isIndexHidden
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            bool
        :description: QtWidgets/QTableView-isIndexHidden-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.isRowHidden
        :args:
            int
        :returns:
            bool
        :description: QtWidgets/QTableView-isRowHidden-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.isSortingEnabled
        :returns:
            bool
        :description: QtWidgets/QTableView-isSortingEnabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.moveCursor
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.CursorAction`
            :sip:ref:`~PyQt6.QtCore.Qt.KeyboardModifier`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QTableView-moveCursor-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.paintEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QPaintEvent`
        :description: QtWidgets/QTableView-paintEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.resizeColumnsToContents
        :description: QtWidgets/QTableView-resizeColumnsToContents-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.resizeColumnToContents
        :args:
            int
        :description: QtWidgets/QTableView-resizeColumnToContents-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.resizeRowsToContents
        :description: QtWidgets/QTableView-resizeRowsToContents-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.resizeRowToContents
        :args:
            int
        :description: QtWidgets/QTableView-resizeRowToContents-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.rowAt
        :args:
            int
        :returns:
            int
        :description: QtWidgets/QTableView-rowAt-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.rowCountChanged
        :args:
            int
            int
        :description: QtWidgets/QTableView-rowCountChanged-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.rowHeight
        :args:
            int
        :returns:
            int
        :description: QtWidgets/QTableView-rowHeight-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.rowMoved
        :args:
            int
            int
            int
        :description: QtWidgets/QTableView-rowMoved-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.rowResized
        :args:
            int
            int
            int
        :description: QtWidgets/QTableView-rowResized-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.rowSpan
        :args:
            int
            int
        :returns:
            int
        :description: QtWidgets/QTableView-rowSpan-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.rowViewportPosition
        :args:
            int
        :returns:
            int
        :description: QtWidgets/QTableView-rowViewportPosition-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.scrollContentsBy
        :args:
            int
            int
        :description: QtWidgets/QTableView-scrollContentsBy-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.scrollTo
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            hint: :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.ScrollHint` = :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.ScrollHint.EnsureVisible`
        :description: QtWidgets/QTableView-scrollTo-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.selectColumn
        :args:
            int
        :description: QtWidgets/QTableView-selectColumn-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.selectedIndexes
        :returns:
            list[:sip:ref:`~PyQt6.QtCore.QModelIndex`]
        :description: QtWidgets/QTableView-selectedIndexes-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.selectionChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QItemSelection`
            :sip:ref:`~PyQt6.QtCore.QItemSelection`
        :description: QtWidgets/QTableView-selectionChanged-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.selectRow
        :args:
            int
        :description: QtWidgets/QTableView-selectRow-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.setColumnHidden
        :args:
            int
            bool
        :description: QtWidgets/QTableView-setColumnHidden-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.setColumnWidth
        :args:
            int
            int
        :description: QtWidgets/QTableView-setColumnWidth-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.setCornerButtonEnabled
        :args:
            bool
        :description: QtWidgets/QTableView-setCornerButtonEnabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.setGridStyle
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.PenStyle`
        :description: QtWidgets/QTableView-setGridStyle-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.setHorizontalHeader
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QHeaderView`
        :description: QtWidgets/QTableView-setHorizontalHeader-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.setModel
        :args:
            :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`
        :description: QtWidgets/QTableView-setModel-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.setRootIndex
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QTableView-setRootIndex-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.setRowHeight
        :args:
            int
            int
        :description: QtWidgets/QTableView-setRowHeight-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.setRowHidden
        :args:
            int
            bool
        :description: QtWidgets/QTableView-setRowHidden-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.setSelection
        :args:
            :sip:ref:`~PyQt6.QtCore.QRect`
            :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.SelectionFlag`
        :description: QtWidgets/QTableView-setSelection-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.setSelectionModel
        :args:
            :sip:ref:`~PyQt6.QtCore.QItemSelectionModel`
        :description: QtWidgets/QTableView-setSelectionModel-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.setShowGrid
        :args:
            bool
        :description: QtWidgets/QTableView-setShowGrid-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.setSortingEnabled
        :args:
            bool
        :description: QtWidgets/QTableView-setSortingEnabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.setSpan
        :args:
            int
            int
            int
            int
        :description: QtWidgets/QTableView-setSpan-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.setVerticalHeader
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QHeaderView`
        :description: QtWidgets/QTableView-setVerticalHeader-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.setWordWrap
        :args:
            bool
        :description: QtWidgets/QTableView-setWordWrap-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.showColumn
        :args:
            int
        :description: QtWidgets/QTableView-showColumn-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.showGrid
        :returns:
            bool
        :description: QtWidgets/QTableView-showGrid-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.showRow
        :args:
            int
        :description: QtWidgets/QTableView-showRow-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.sizeHintForColumn
        :args:
            int
        :returns:
            int
        :description: QtWidgets/QTableView-sizeHintForColumn-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.sizeHintForRow
        :args:
            int
        :returns:
            int
        :description: QtWidgets/QTableView-sizeHintForRow-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.sortByColumn
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.Qt.SortOrder`
        :description: QtWidgets/QTableView-sortByColumn-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.timerEvent
        :args:
            :sip:ref:`~PyQt6.QtCore.QTimerEvent`
        :description: QtWidgets/QTableView-timerEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.updateGeometries
        :description: QtWidgets/QTableView-updateGeometries-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.verticalHeader
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QHeaderView`
        :description: QtWidgets/QTableView-verticalHeader-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.verticalOffset
        :returns:
            int
        :description: QtWidgets/QTableView-verticalOffset-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.verticalScrollbarAction
        :args:
            int
        :description: QtWidgets/QTableView-verticalScrollbarAction-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.viewportSizeHint
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QTableView-viewportSizeHint-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.visualRect
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtWidgets/QTableView-visualRect-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.visualRegionForSelection
        :args:
            :sip:ref:`~PyQt6.QtCore.QItemSelection`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QRegion`
        :description: QtWidgets/QTableView-visualRegionForSelection-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableView.wordWrap
        :returns:
            bool
        :description: QtWidgets/QTableView-wordWrap-f.rst
