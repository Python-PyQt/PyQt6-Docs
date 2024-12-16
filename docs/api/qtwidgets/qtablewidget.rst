:orphan:

.. sip:class:: PyQt6.QtWidgets.QTableWidget
    :inherits: :sip:ref:`~PyQt6.QtWidgets.QTableView`
    :description: QtWidgets/QTableWidget-c.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :description: QtWidgets/QTableWidget-__init__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.__init__
        :args:
            int
            int
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :description: QtWidgets/QTableWidget-__init__-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.cellWidget
        :args:
            int
            int
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QTableWidget-cellWidget-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.clear
        :description: QtWidgets/QTableWidget-clear-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.clearContents
        :description: QtWidgets/QTableWidget-clearContents-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.closePersistentEditor
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`
        :description: QtWidgets/QTableWidget-closePersistentEditor-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.column
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`
        :returns:
            int
        :description: QtWidgets/QTableWidget-column-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.columnCount
        :returns:
            int
        :description: QtWidgets/QTableWidget-columnCount-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.currentColumn
        :returns:
            int
        :description: QtWidgets/QTableWidget-currentColumn-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.currentItem
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`
        :description: QtWidgets/QTableWidget-currentItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.currentRow
        :returns:
            int
        :description: QtWidgets/QTableWidget-currentRow-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.dropEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QDropEvent`
        :description: QtWidgets/QTableWidget-dropEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.dropMimeData
        :args:
            int
            int
            :sip:ref:`~PyQt6.QtCore.QMimeData`
            :sip:ref:`~PyQt6.QtCore.Qt.DropAction`
        :returns:
            bool
        :description: QtWidgets/QTableWidget-dropMimeData-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.editItem
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`
        :description: QtWidgets/QTableWidget-editItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtWidgets/QTableWidget-event-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.findItems
        :args:
            Optional[str]
            :sip:ref:`~PyQt6.QtCore.Qt.MatchFlag`
        :returns:
            list[:sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`]
        :description: QtWidgets/QTableWidget-findItems-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.horizontalHeaderItem
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`
        :description: QtWidgets/QTableWidget-horizontalHeaderItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.indexFromItem
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QTableWidget-indexFromItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.insertColumn
        :args:
            int
        :description: QtWidgets/QTableWidget-insertColumn-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.insertRow
        :args:
            int
        :description: QtWidgets/QTableWidget-insertRow-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.isPersistentEditorOpen
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`
        :returns:
            bool
        :description: QtWidgets/QTableWidget-isPersistentEditorOpen-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.isSortingEnabled
        :returns:
            bool
        :description: QtWidgets/QTableWidget-isSortingEnabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.item
        :args:
            int
            int
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`
        :description: QtWidgets/QTableWidget-item-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.itemAt
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`
        :description: QtWidgets/QTableWidget-itemAt-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.itemAt
        :args:
            int
            int
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`
        :description: QtWidgets/QTableWidget-itemAt-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.itemFromIndex
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`
        :description: QtWidgets/QTableWidget-itemFromIndex-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.itemPrototype
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`
        :description: QtWidgets/QTableWidget-itemPrototype-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.items
        :args:
            :sip:ref:`~PyQt6.QtCore.QMimeData`
        :returns:
            list[:sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`]
        :description: QtWidgets/QTableWidget-items-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.mimeData
        :args:
            Iterable[:sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`]
        :returns:
            :sip:ref:`~PyQt6.QtCore.QMimeData`
        :description: QtWidgets/QTableWidget-mimeData-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.mimeTypes
        :returns:
            list[str]
        :description: QtWidgets/QTableWidget-mimeTypes-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.openPersistentEditor
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`
        :description: QtWidgets/QTableWidget-openPersistentEditor-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.removeCellWidget
        :args:
            int
            int
        :description: QtWidgets/QTableWidget-removeCellWidget-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.removeColumn
        :args:
            int
        :description: QtWidgets/QTableWidget-removeColumn-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.removeRow
        :args:
            int
        :description: QtWidgets/QTableWidget-removeRow-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.row
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`
        :returns:
            int
        :description: QtWidgets/QTableWidget-row-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.rowCount
        :returns:
            int
        :description: QtWidgets/QTableWidget-rowCount-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.scrollToItem
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`
            hint: :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.ScrollHint` = :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.ScrollHint.EnsureVisible`
        :description: QtWidgets/QTableWidget-scrollToItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.selectedItems
        :returns:
            list[:sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`]
        :description: QtWidgets/QTableWidget-selectedItems-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.selectedRanges
        :returns:
            list[:sip:ref:`~PyQt6.QtWidgets.QTableWidgetSelectionRange`]
        :description: QtWidgets/QTableWidget-selectedRanges-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.setCellWidget
        :args:
            int
            int
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QTableWidget-setCellWidget-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.setColumnCount
        :args:
            int
        :description: QtWidgets/QTableWidget-setColumnCount-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.setCurrentCell
        :args:
            int
            int
        :description: QtWidgets/QTableWidget-setCurrentCell-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.setCurrentCell
        :args:
            int
            int
            :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.SelectionFlag`
        :description: QtWidgets/QTableWidget-setCurrentCell-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.setCurrentItem
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`
        :description: QtWidgets/QTableWidget-setCurrentItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.setCurrentItem
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`
            :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.SelectionFlag`
        :description: QtWidgets/QTableWidget-setCurrentItem-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.setHorizontalHeaderItem
        :args:
            int
            :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`
        :description: QtWidgets/QTableWidget-setHorizontalHeaderItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.setHorizontalHeaderLabels
        :args:
            Iterable[Optional[str]]
        :description: QtWidgets/QTableWidget-setHorizontalHeaderLabels-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.setItem
        :args:
            int
            int
            :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`
        :description: QtWidgets/QTableWidget-setItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.setItemPrototype
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`
        :description: QtWidgets/QTableWidget-setItemPrototype-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.setRangeSelected
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTableWidgetSelectionRange`
            bool
        :description: QtWidgets/QTableWidget-setRangeSelected-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.setRowCount
        :args:
            int
        :description: QtWidgets/QTableWidget-setRowCount-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.setSortingEnabled
        :args:
            bool
        :description: QtWidgets/QTableWidget-setSortingEnabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.setVerticalHeaderItem
        :args:
            int
            :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`
        :description: QtWidgets/QTableWidget-setVerticalHeaderItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.setVerticalHeaderLabels
        :args:
            Iterable[Optional[str]]
        :description: QtWidgets/QTableWidget-setVerticalHeaderLabels-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.sortItems
        :args:
            int
            order: :sip:ref:`~PyQt6.QtCore.Qt.SortOrder` = :sip:ref:`~PyQt6.QtCore.Qt.SortOrder.AscendingOrder`
        :description: QtWidgets/QTableWidget-sortItems-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.supportedDropActions
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.DropAction`
        :description: QtWidgets/QTableWidget-supportedDropActions-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.takeHorizontalHeaderItem
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`
        :description: QtWidgets/QTableWidget-takeHorizontalHeaderItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.takeItem
        :args:
            int
            int
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`
        :description: QtWidgets/QTableWidget-takeItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.takeVerticalHeaderItem
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`
        :description: QtWidgets/QTableWidget-takeVerticalHeaderItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.verticalHeaderItem
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`
        :description: QtWidgets/QTableWidget-verticalHeaderItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.visualColumn
        :args:
            int
        :returns:
            int
        :description: QtWidgets/QTableWidget-visualColumn-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.visualItemRect
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtWidgets/QTableWidget-visualItemRect-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTableWidget.visualRow
        :args:
            int
        :returns:
            int
        :description: QtWidgets/QTableWidget-visualRow-f.rst

    .. sip:signal:: PyQt6.QtWidgets.QTableWidget.cellActivated
        :args:
            int
            int
        :description: QtWidgets/QTableWidget-cellActivated-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QTableWidget.cellChanged
        :args:
            int
            int
        :description: QtWidgets/QTableWidget-cellChanged-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QTableWidget.cellClicked
        :args:
            int
            int
        :description: QtWidgets/QTableWidget-cellClicked-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QTableWidget.cellDoubleClicked
        :args:
            int
            int
        :description: QtWidgets/QTableWidget-cellDoubleClicked-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QTableWidget.cellEntered
        :args:
            int
            int
        :description: QtWidgets/QTableWidget-cellEntered-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QTableWidget.cellPressed
        :args:
            int
            int
        :description: QtWidgets/QTableWidget-cellPressed-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QTableWidget.currentCellChanged
        :args:
            int
            int
            int
            int
        :description: QtWidgets/QTableWidget-currentCellChanged-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QTableWidget.currentItemChanged
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`
            :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`
        :description: QtWidgets/QTableWidget-currentItemChanged-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QTableWidget.itemActivated
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`
        :description: QtWidgets/QTableWidget-itemActivated-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QTableWidget.itemChanged
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`
        :description: QtWidgets/QTableWidget-itemChanged-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QTableWidget.itemClicked
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`
        :description: QtWidgets/QTableWidget-itemClicked-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QTableWidget.itemDoubleClicked
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`
        :description: QtWidgets/QTableWidget-itemDoubleClicked-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QTableWidget.itemEntered
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`
        :description: QtWidgets/QTableWidget-itemEntered-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QTableWidget.itemPressed
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`
        :description: QtWidgets/QTableWidget-itemPressed-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QTableWidget.itemSelectionChanged
        :description: QtWidgets/QTableWidget-itemSelectionChanged-s.rst
