:orphan:

.. sip:class:: PyQt6.QtGui.QStandardItemModel
    :inherits: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`
    :description: QtGui/QStandardItemModel-c.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtGui/QStandardItemModel-__init__-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.__init__
        :args:
            int
            int
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtGui/QStandardItemModel-__init__-f-1.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.appendColumn
        :args:
            Iterable[:sip:ref:`~PyQt6.QtGui.QStandardItem`]
        :description: QtGui/QStandardItemModel-appendColumn-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.appendRow
        :args:
            Iterable[:sip:ref:`~PyQt6.QtGui.QStandardItem`]
        :description: QtGui/QStandardItemModel-appendRow-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.appendRow
        :args:
            :sip:ref:`~PyQt6.QtGui.QStandardItem`
        :description: QtGui/QStandardItemModel-appendRow-f-1.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.clear
        :description: QtGui/QStandardItemModel-clear-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.clearItemData
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            bool
        :description: QtGui/QStandardItemModel-clearItemData-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.columnCount
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            int
        :description: QtGui/QStandardItemModel-columnCount-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.data
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            role: int = :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DisplayRole`
        :returns:
            Any
        :description: QtGui/QStandardItemModel-data-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.dropMimeData
        :args:
            :sip:ref:`~PyQt6.QtCore.QMimeData`
            :sip:ref:`~PyQt6.QtCore.Qt.DropActions`
            int
            int
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            bool
        :description: QtGui/QStandardItemModel-dropMimeData-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.findItems
        :args:
            str
            flags: :sip:ref:`~PyQt6.QtCore.Qt.MatchFlags` = :sip:ref:`~PyQt6.QtCore.Qt.MatchFlags.MatchExactly`
            column: int = 0
        :returns:
            List[:sip:ref:`~PyQt6.QtGui.QStandardItem`]
        :description: QtGui/QStandardItemModel-findItems-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.flags
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.ItemFlags`
        :description: QtGui/QStandardItemModel-flags-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.hasChildren
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            bool
        :description: QtGui/QStandardItemModel-hasChildren-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.headerData
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.Qt.Orientations`
            role: int = :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DisplayRole`
        :returns:
            Any
        :description: QtGui/QStandardItemModel-headerData-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.horizontalHeaderItem
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtGui.QStandardItem`
        :description: QtGui/QStandardItemModel-horizontalHeaderItem-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.index
        :args:
            int
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtGui/QStandardItemModel-index-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.indexFromItem
        :args:
            :sip:ref:`~PyQt6.QtGui.QStandardItem`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtGui/QStandardItemModel-indexFromItem-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.insertColumn
        :args:
            int
            Iterable[:sip:ref:`~PyQt6.QtGui.QStandardItem`]
        :description: QtGui/QStandardItemModel-insertColumn-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.insertColumn
        :args:
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            bool
        :description: QtGui/QStandardItemModel-insertColumn-f-1.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.insertColumns
        :args:
            int
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            bool
        :description: QtGui/QStandardItemModel-insertColumns-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.insertRow
        :args:
            int
            Iterable[:sip:ref:`~PyQt6.QtGui.QStandardItem`]
        :description: QtGui/QStandardItemModel-insertRow-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.insertRow
        :args:
            int
            :sip:ref:`~PyQt6.QtGui.QStandardItem`
        :description: QtGui/QStandardItemModel-insertRow-f-1.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.insertRow
        :args:
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            bool
        :description: QtGui/QStandardItemModel-insertRow-f-2.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.insertRows
        :args:
            int
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            bool
        :description: QtGui/QStandardItemModel-insertRows-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.invisibleRootItem
        :returns:
            :sip:ref:`~PyQt6.QtGui.QStandardItem`
        :description: QtGui/QStandardItemModel-invisibleRootItem-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.item
        :args:
            int
            column: int = 0
        :returns:
            :sip:ref:`~PyQt6.QtGui.QStandardItem`
        :description: QtGui/QStandardItemModel-item-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.itemData
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            Dict[int, Any]
        :description: QtGui/QStandardItemModel-itemData-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.itemFromIndex
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QStandardItem`
        :description: QtGui/QStandardItemModel-itemFromIndex-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.itemPrototype
        :returns:
            :sip:ref:`~PyQt6.QtGui.QStandardItem`
        :description: QtGui/QStandardItemModel-itemPrototype-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.mimeData
        :args:
            Iterable[:sip:ref:`~PyQt6.QtCore.QModelIndex`]
        :returns:
            :sip:ref:`~PyQt6.QtCore.QMimeData`
        :description: QtGui/QStandardItemModel-mimeData-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.mimeTypes
        :returns:
            List[str]
        :description: QtGui/QStandardItemModel-mimeTypes-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.parent
        :returns:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :description: QtGui/QStandardItemModel-parent-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.parent
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtGui/QStandardItemModel-parent-f-1.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.removeColumns
        :args:
            int
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            bool
        :description: QtGui/QStandardItemModel-removeColumns-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.removeRows
        :args:
            int
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            bool
        :description: QtGui/QStandardItemModel-removeRows-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.roleNames
        :returns:
            Dict[int, :sip:ref:`~PyQt6.QtCore.QByteArray`]
        :description: QtGui/QStandardItemModel-roleNames-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.rowCount
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            int
        :description: QtGui/QStandardItemModel-rowCount-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.setColumnCount
        :args:
            int
        :description: QtGui/QStandardItemModel-setColumnCount-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.setData
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            Any
            role: int = :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.EditRole`
        :returns:
            bool
        :description: QtGui/QStandardItemModel-setData-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.setHeaderData
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.Qt.Orientations`
            Any
            role: int = :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.EditRole`
        :returns:
            bool
        :description: QtGui/QStandardItemModel-setHeaderData-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.setHorizontalHeaderItem
        :args:
            int
            :sip:ref:`~PyQt6.QtGui.QStandardItem`
        :description: QtGui/QStandardItemModel-setHorizontalHeaderItem-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.setHorizontalHeaderLabels
        :args:
            Iterable[str]
        :description: QtGui/QStandardItemModel-setHorizontalHeaderLabels-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.setItem
        :args:
            int
            :sip:ref:`~PyQt6.QtGui.QStandardItem`
        :description: QtGui/QStandardItemModel-setItem-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.setItem
        :args:
            int
            int
            :sip:ref:`~PyQt6.QtGui.QStandardItem`
        :description: QtGui/QStandardItemModel-setItem-f-1.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.setItemData
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            Dict[int, Any]
        :returns:
            bool
        :description: QtGui/QStandardItemModel-setItemData-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.setItemPrototype
        :args:
            :sip:ref:`~PyQt6.QtGui.QStandardItem`
        :description: QtGui/QStandardItemModel-setItemPrototype-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.setItemRoleNames
        :args:
            Dict[int, :sip:ref:`~PyQt6.QtCore.QByteArray`]
        :description: QtGui/QStandardItemModel-setItemRoleNames-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.setRowCount
        :args:
            int
        :description: QtGui/QStandardItemModel-setRowCount-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.setSortRole
        :args:
            int
        :description: QtGui/QStandardItemModel-setSortRole-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.setVerticalHeaderItem
        :args:
            int
            :sip:ref:`~PyQt6.QtGui.QStandardItem`
        :description: QtGui/QStandardItemModel-setVerticalHeaderItem-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.setVerticalHeaderLabels
        :args:
            Iterable[str]
        :description: QtGui/QStandardItemModel-setVerticalHeaderLabels-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.sort
        :args:
            int
            order: :sip:ref:`~PyQt6.QtCore.Qt.SortOrder` = :sip:ref:`~PyQt6.QtCore.Qt.SortOrder.AscendingOrder`
        :description: QtGui/QStandardItemModel-sort-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.sortRole
        :returns:
            int
        :description: QtGui/QStandardItemModel-sortRole-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.supportedDropActions
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.DropActions`
        :description: QtGui/QStandardItemModel-supportedDropActions-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.takeColumn
        :args:
            int
        :returns:
            List[:sip:ref:`~PyQt6.QtGui.QStandardItem`]
        :description: QtGui/QStandardItemModel-takeColumn-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.takeHorizontalHeaderItem
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtGui.QStandardItem`
        :description: QtGui/QStandardItemModel-takeHorizontalHeaderItem-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.takeItem
        :args:
            int
            column: int = 0
        :returns:
            :sip:ref:`~PyQt6.QtGui.QStandardItem`
        :description: QtGui/QStandardItemModel-takeItem-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.takeRow
        :args:
            int
        :returns:
            List[:sip:ref:`~PyQt6.QtGui.QStandardItem`]
        :description: QtGui/QStandardItemModel-takeRow-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.takeVerticalHeaderItem
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtGui.QStandardItem`
        :description: QtGui/QStandardItemModel-takeVerticalHeaderItem-f.rst

    .. sip:method:: PyQt6.QtGui.QStandardItemModel.verticalHeaderItem
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtGui.QStandardItem`
        :description: QtGui/QStandardItemModel-verticalHeaderItem-f.rst

    .. sip:signal:: PyQt6.QtGui.QStandardItemModel.itemChanged
        :args:
            :sip:ref:`~PyQt6.QtGui.QStandardItem`
        :description: QtGui/QStandardItemModel-itemChanged-s.rst
