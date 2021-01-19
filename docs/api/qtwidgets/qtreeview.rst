:orphan:

.. sip:class:: PyQt6.QtWidgets.QTreeView
    :inherits: :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView`
    :description: QtWidgets/QTreeView-c.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :description: QtWidgets/QTreeView-__init__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.allColumnsShowFocus
        :returns:
            bool
        :description: QtWidgets/QTreeView-allColumnsShowFocus-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.autoExpandDelay
        :returns:
            int
        :description: QtWidgets/QTreeView-autoExpandDelay-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.changeEvent
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :description: QtWidgets/QTreeView-changeEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.collapse
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QTreeView-collapse-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.collapseAll
        :description: QtWidgets/QTreeView-collapseAll-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.columnAt
        :args:
            int
        :returns:
            int
        :description: QtWidgets/QTreeView-columnAt-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.columnCountChanged
        :args:
            int
            int
        :description: QtWidgets/QTreeView-columnCountChanged-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.columnMoved
        :description: QtWidgets/QTreeView-columnMoved-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.columnResized
        :args:
            int
            int
            int
        :description: QtWidgets/QTreeView-columnResized-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.columnViewportPosition
        :args:
            int
        :returns:
            int
        :description: QtWidgets/QTreeView-columnViewportPosition-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.columnWidth
        :args:
            int
        :returns:
            int
        :description: QtWidgets/QTreeView-columnWidth-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.currentChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QTreeView-currentChanged-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.dataChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            roles: Iterable[int] = []
        :description: QtWidgets/QTreeView-dataChanged-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.dragMoveEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QDragMoveEvent`
        :description: QtWidgets/QTreeView-dragMoveEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.drawBranches
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            :sip:ref:`~PyQt6.QtCore.QRect`
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QTreeView-drawBranches-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.drawRow
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            :sip:ref:`~PyQt6.QtWidgets.QStyleOptionViewItem`
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QTreeView-drawRow-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.drawTree
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            :sip:ref:`~PyQt6.QtGui.QRegion`
        :description: QtWidgets/QTreeView-drawTree-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.expand
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QTreeView-expand-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.expandAll
        :description: QtWidgets/QTreeView-expandAll-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.expandRecursively
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            depth: int = -1
        :description: QtWidgets/QTreeView-expandRecursively-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.expandsOnDoubleClick
        :returns:
            bool
        :description: QtWidgets/QTreeView-expandsOnDoubleClick-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.expandToDepth
        :args:
            int
        :description: QtWidgets/QTreeView-expandToDepth-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.header
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QHeaderView`
        :description: QtWidgets/QTreeView-header-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.hideColumn
        :args:
            int
        :description: QtWidgets/QTreeView-hideColumn-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.horizontalOffset
        :returns:
            int
        :description: QtWidgets/QTreeView-horizontalOffset-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.horizontalScrollbarAction
        :args:
            int
        :description: QtWidgets/QTreeView-horizontalScrollbarAction-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.indentation
        :returns:
            int
        :description: QtWidgets/QTreeView-indentation-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.indexAbove
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QTreeView-indexAbove-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.indexAt
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QTreeView-indexAt-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.indexBelow
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QTreeView-indexBelow-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.indexRowSizeHint
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            int
        :description: QtWidgets/QTreeView-indexRowSizeHint-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.isAnimated
        :returns:
            bool
        :description: QtWidgets/QTreeView-isAnimated-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.isColumnHidden
        :args:
            int
        :returns:
            bool
        :description: QtWidgets/QTreeView-isColumnHidden-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.isExpanded
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            bool
        :description: QtWidgets/QTreeView-isExpanded-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.isFirstColumnSpanned
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            bool
        :description: QtWidgets/QTreeView-isFirstColumnSpanned-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.isHeaderHidden
        :returns:
            bool
        :description: QtWidgets/QTreeView-isHeaderHidden-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.isIndexHidden
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            bool
        :description: QtWidgets/QTreeView-isIndexHidden-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.isRowHidden
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            bool
        :description: QtWidgets/QTreeView-isRowHidden-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.isSortingEnabled
        :returns:
            bool
        :description: QtWidgets/QTreeView-isSortingEnabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.itemsExpandable
        :returns:
            bool
        :description: QtWidgets/QTreeView-itemsExpandable-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.keyboardSearch
        :args:
            str
        :description: QtWidgets/QTreeView-keyboardSearch-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.keyPressEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QKeyEvent`
        :description: QtWidgets/QTreeView-keyPressEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.mouseDoubleClickEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtWidgets/QTreeView-mouseDoubleClickEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.mouseMoveEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtWidgets/QTreeView-mouseMoveEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.mousePressEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtWidgets/QTreeView-mousePressEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.mouseReleaseEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtWidgets/QTreeView-mouseReleaseEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.moveCursor
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.CursorAction`
            :sip:ref:`~PyQt6.QtCore.Qt.KeyboardModifiers`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QTreeView-moveCursor-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.paintEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QPaintEvent`
        :description: QtWidgets/QTreeView-paintEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.reexpand
        :description: QtWidgets/QTreeView-reexpand-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.reset
        :description: QtWidgets/QTreeView-reset-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.resetIndentation
        :description: QtWidgets/QTreeView-resetIndentation-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.resizeColumnToContents
        :args:
            int
        :description: QtWidgets/QTreeView-resizeColumnToContents-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.rootIsDecorated
        :returns:
            bool
        :description: QtWidgets/QTreeView-rootIsDecorated-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.rowHeight
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            int
        :description: QtWidgets/QTreeView-rowHeight-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.rowsAboutToBeRemoved
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            int
        :description: QtWidgets/QTreeView-rowsAboutToBeRemoved-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.rowsInserted
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            int
        :description: QtWidgets/QTreeView-rowsInserted-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.rowsRemoved
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            int
        :description: QtWidgets/QTreeView-rowsRemoved-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.scrollContentsBy
        :args:
            int
            int
        :description: QtWidgets/QTreeView-scrollContentsBy-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.scrollTo
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            hint: :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.ScrollHint` = :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.ScrollHint.EnsureVisible`
        :description: QtWidgets/QTreeView-scrollTo-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.selectAll
        :description: QtWidgets/QTreeView-selectAll-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.selectedIndexes
        :returns:
            List[:sip:ref:`~PyQt6.QtCore.QModelIndex`]
        :description: QtWidgets/QTreeView-selectedIndexes-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.selectionChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QItemSelection`
            :sip:ref:`~PyQt6.QtCore.QItemSelection`
        :description: QtWidgets/QTreeView-selectionChanged-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.setAllColumnsShowFocus
        :args:
            bool
        :description: QtWidgets/QTreeView-setAllColumnsShowFocus-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.setAnimated
        :args:
            bool
        :description: QtWidgets/QTreeView-setAnimated-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.setAutoExpandDelay
        :args:
            int
        :description: QtWidgets/QTreeView-setAutoExpandDelay-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.setColumnHidden
        :args:
            int
            bool
        :description: QtWidgets/QTreeView-setColumnHidden-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.setColumnWidth
        :args:
            int
            int
        :description: QtWidgets/QTreeView-setColumnWidth-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.setExpanded
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            bool
        :description: QtWidgets/QTreeView-setExpanded-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.setExpandsOnDoubleClick
        :args:
            bool
        :description: QtWidgets/QTreeView-setExpandsOnDoubleClick-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.setFirstColumnSpanned
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            bool
        :description: QtWidgets/QTreeView-setFirstColumnSpanned-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.setHeader
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QHeaderView`
        :description: QtWidgets/QTreeView-setHeader-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.setHeaderHidden
        :args:
            bool
        :description: QtWidgets/QTreeView-setHeaderHidden-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.setIndentation
        :args:
            int
        :description: QtWidgets/QTreeView-setIndentation-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.setItemsExpandable
        :args:
            bool
        :description: QtWidgets/QTreeView-setItemsExpandable-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.setModel
        :args:
            :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`
        :description: QtWidgets/QTreeView-setModel-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.setRootIndex
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QTreeView-setRootIndex-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.setRootIsDecorated
        :args:
            bool
        :description: QtWidgets/QTreeView-setRootIsDecorated-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.setRowHidden
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            bool
        :description: QtWidgets/QTreeView-setRowHidden-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.setSelection
        :args:
            :sip:ref:`~PyQt6.QtCore.QRect`
            :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.SelectionFlags`
        :description: QtWidgets/QTreeView-setSelection-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.setSelectionModel
        :args:
            :sip:ref:`~PyQt6.QtCore.QItemSelectionModel`
        :description: QtWidgets/QTreeView-setSelectionModel-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.setSortingEnabled
        :args:
            bool
        :description: QtWidgets/QTreeView-setSortingEnabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.setTreePosition
        :args:
            int
        :description: QtWidgets/QTreeView-setTreePosition-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.setUniformRowHeights
        :args:
            bool
        :description: QtWidgets/QTreeView-setUniformRowHeights-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.setWordWrap
        :args:
            bool
        :description: QtWidgets/QTreeView-setWordWrap-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.showColumn
        :args:
            int
        :description: QtWidgets/QTreeView-showColumn-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.sizeHintForColumn
        :args:
            int
        :returns:
            int
        :description: QtWidgets/QTreeView-sizeHintForColumn-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.sortByColumn
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.Qt.SortOrder`
        :description: QtWidgets/QTreeView-sortByColumn-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.timerEvent
        :args:
            :sip:ref:`~PyQt6.QtCore.QTimerEvent`
        :description: QtWidgets/QTreeView-timerEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.treePosition
        :returns:
            int
        :description: QtWidgets/QTreeView-treePosition-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.uniformRowHeights
        :returns:
            bool
        :description: QtWidgets/QTreeView-uniformRowHeights-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.updateGeometries
        :description: QtWidgets/QTreeView-updateGeometries-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.verticalOffset
        :returns:
            int
        :description: QtWidgets/QTreeView-verticalOffset-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.viewportEvent
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtWidgets/QTreeView-viewportEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.viewportSizeHint
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QTreeView-viewportSizeHint-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.visualRect
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtWidgets/QTreeView-visualRect-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.visualRegionForSelection
        :args:
            :sip:ref:`~PyQt6.QtCore.QItemSelection`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QRegion`
        :description: QtWidgets/QTreeView-visualRegionForSelection-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeView.wordWrap
        :returns:
            bool
        :description: QtWidgets/QTreeView-wordWrap-f.rst

    .. sip:signal:: PyQt6.QtWidgets.QTreeView.collapsed
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QTreeView-collapsed-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QTreeView.expanded
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QTreeView-expanded-s.rst
