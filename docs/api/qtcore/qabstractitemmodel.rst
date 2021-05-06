:orphan:

.. sip:class:: PyQt6.QtCore.QAbstractItemModel
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtCore/QAbstractItemModel-c.rst

    .. sip:enum:: PyQt6.QtCore.QAbstractItemModel.CheckIndexOption
        :description: QtCore/QAbstractItemModel-CheckIndexOption-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QAbstractItemModel.CheckIndexOption.DoNotUseParent
            :description: QtCore/QAbstractItemModel-CheckIndexOption-DoNotUseParent-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QAbstractItemModel.CheckIndexOption.IndexIsValid
            :description: QtCore/QAbstractItemModel-CheckIndexOption-IndexIsValid-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QAbstractItemModel.CheckIndexOption.NoOption
            :description: QtCore/QAbstractItemModel-CheckIndexOption-NoOption-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QAbstractItemModel.CheckIndexOption.ParentIsInvalid
            :description: QtCore/QAbstractItemModel-CheckIndexOption-ParentIsInvalid-v.rst

    .. sip:enum:: PyQt6.QtCore.QAbstractItemModel.LayoutChangeHint
        :description: QtCore/QAbstractItemModel-LayoutChangeHint-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QAbstractItemModel.LayoutChangeHint.HorizontalSortHint
            :description: QtCore/QAbstractItemModel-LayoutChangeHint-HorizontalSortHint-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QAbstractItemModel.LayoutChangeHint.NoLayoutChangeHint
            :description: QtCore/QAbstractItemModel-LayoutChangeHint-NoLayoutChangeHint-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QAbstractItemModel.LayoutChangeHint.VerticalSortHint
            :description: QtCore/QAbstractItemModel-LayoutChangeHint-VerticalSortHint-v.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtCore/QAbstractItemModel-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.beginInsertColumns
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            int
        :description: QtCore/QAbstractItemModel-beginInsertColumns-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.beginInsertRows
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            int
        :description: QtCore/QAbstractItemModel-beginInsertRows-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.beginMoveColumns
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            int
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
        :returns:
            bool
        :description: QtCore/QAbstractItemModel-beginMoveColumns-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.beginMoveRows
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            int
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
        :returns:
            bool
        :description: QtCore/QAbstractItemModel-beginMoveRows-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.beginRemoveColumns
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            int
        :description: QtCore/QAbstractItemModel-beginRemoveColumns-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.beginRemoveRows
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            int
        :description: QtCore/QAbstractItemModel-beginRemoveRows-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.beginResetModel
        :description: QtCore/QAbstractItemModel-beginResetModel-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.buddy
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtCore/QAbstractItemModel-buddy-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.canDropMimeData
        :args:
            :sip:ref:`~PyQt6.QtCore.QMimeData`
            :sip:ref:`~PyQt6.QtCore.Qt.DropAction`
            int
            int
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            bool
        :description: QtCore/QAbstractItemModel-canDropMimeData-f-1.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.canFetchMore
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            bool
        :description: QtCore/QAbstractItemModel-canFetchMore-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.changePersistentIndex
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtCore/QAbstractItemModel-changePersistentIndex-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.changePersistentIndexList
        :args:
            Iterable[:sip:ref:`~PyQt6.QtCore.QModelIndex`]
            Iterable[:sip:ref:`~PyQt6.QtCore.QModelIndex`]
        :description: QtCore/QAbstractItemModel-changePersistentIndexList-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.checkIndex
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            options: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.CheckIndexOption` = :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.CheckIndexOption.NoOption`
        :returns:
            bool
        :description: QtCore/QAbstractItemModel-checkIndex-f-1.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.clearItemData
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            bool
        :description: QtCore/QAbstractItemModel-clearItemData-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.columnCount
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            int
        :description: QtCore/QAbstractItemModel-columnCount-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.createIndex
        :args:
            int
            int
            object: object = 0
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtCore/QAbstractItemModel-createIndex-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.data
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            role: int = :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DisplayRole`
        :returns:
            Any
        :description: QtCore/QAbstractItemModel-data-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.decodeData
        :args:
            int
            int
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :returns:
            bool
        :description: QtCore/QAbstractItemModel-decodeData-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.dropMimeData
        :args:
            :sip:ref:`~PyQt6.QtCore.QMimeData`
            :sip:ref:`~PyQt6.QtCore.Qt.DropAction`
            int
            int
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            bool
        :description: QtCore/QAbstractItemModel-dropMimeData-f-1.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.encodeData
        :args:
            Iterable[:sip:ref:`~PyQt6.QtCore.QModelIndex`]
            :sip:ref:`~PyQt6.QtCore.QDataStream`
        :description: QtCore/QAbstractItemModel-encodeData-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.endInsertColumns
        :description: QtCore/QAbstractItemModel-endInsertColumns-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.endInsertRows
        :description: QtCore/QAbstractItemModel-endInsertRows-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.endMoveColumns
        :description: QtCore/QAbstractItemModel-endMoveColumns-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.endMoveRows
        :description: QtCore/QAbstractItemModel-endMoveRows-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.endRemoveColumns
        :description: QtCore/QAbstractItemModel-endRemoveColumns-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.endRemoveRows
        :description: QtCore/QAbstractItemModel-endRemoveRows-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.endResetModel
        :description: QtCore/QAbstractItemModel-endResetModel-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.fetchMore
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtCore/QAbstractItemModel-fetchMore-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.flags
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.ItemFlag`
        :description: QtCore/QAbstractItemModel-flags-f-1.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.hasChildren
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            bool
        :description: QtCore/QAbstractItemModel-hasChildren-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.hasIndex
        :args:
            int
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            bool
        :description: QtCore/QAbstractItemModel-hasIndex-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.headerData
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.Qt.Orientation`
            role: int = :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DisplayRole`
        :returns:
            Any
        :description: QtCore/QAbstractItemModel-headerData-f-1.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.index
        :args:
            int
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtCore/QAbstractItemModel-index-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.insertColumn
        :args:
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            bool
        :description: QtCore/QAbstractItemModel-insertColumn-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.insertColumns
        :args:
            int
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            bool
        :description: QtCore/QAbstractItemModel-insertColumns-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.insertRow
        :args:
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            bool
        :description: QtCore/QAbstractItemModel-insertRow-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.insertRows
        :args:
            int
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            bool
        :description: QtCore/QAbstractItemModel-insertRows-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.itemData
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            Dict[int, Any]
        :description: QtCore/QAbstractItemModel-itemData-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.match
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            Any
            hits: int = 1
            flags: :sip:ref:`~PyQt6.QtCore.Qt.MatchFlag` = Qt.MatchFlags(Qt.MatchStartsWith|Qt.MatchWrap)
        :returns:
            List[:sip:ref:`~PyQt6.QtCore.QModelIndex`]
        :description: QtCore/QAbstractItemModel-match-f-1.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.mimeData
        :args:
            Iterable[:sip:ref:`~PyQt6.QtCore.QModelIndex`]
        :returns:
            :sip:ref:`~PyQt6.QtCore.QMimeData`
        :description: QtCore/QAbstractItemModel-mimeData-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.mimeTypes
        :returns:
            List[str]
        :description: QtCore/QAbstractItemModel-mimeTypes-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.moveColumn
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
        :returns:
            bool
        :description: QtCore/QAbstractItemModel-moveColumn-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.moveColumns
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            int
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
        :returns:
            bool
        :description: QtCore/QAbstractItemModel-moveColumns-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.moveRow
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
        :returns:
            bool
        :description: QtCore/QAbstractItemModel-moveRow-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.moveRows
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            int
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
        :returns:
            bool
        :description: QtCore/QAbstractItemModel-moveRows-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.parent
        :returns:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :description: QtCore/QAbstractItemModel-parent-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.parent
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtCore/QAbstractItemModel-parent-f-1.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.persistentIndexList
        :returns:
            List[:sip:ref:`~PyQt6.QtCore.QModelIndex`]
        :description: QtCore/QAbstractItemModel-persistentIndexList-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.removeColumn
        :args:
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            bool
        :description: QtCore/QAbstractItemModel-removeColumn-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.removeColumns
        :args:
            int
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            bool
        :description: QtCore/QAbstractItemModel-removeColumns-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.removeRow
        :args:
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            bool
        :description: QtCore/QAbstractItemModel-removeRow-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.removeRows
        :args:
            int
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            bool
        :description: QtCore/QAbstractItemModel-removeRows-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.resetInternalData
        :description: QtCore/QAbstractItemModel-resetInternalData-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.revert
        :description: QtCore/QAbstractItemModel-revert-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.roleNames
        :returns:
            Dict[int, :sip:ref:`~PyQt6.QtCore.QByteArray`]
        :description: QtCore/QAbstractItemModel-roleNames-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.rowCount
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            int
        :description: QtCore/QAbstractItemModel-rowCount-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.setData
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            Any
            role: int = :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.EditRole`
        :returns:
            bool
        :description: QtCore/QAbstractItemModel-setData-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.setHeaderData
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.Qt.Orientation`
            Any
            role: int = :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.EditRole`
        :returns:
            bool
        :description: QtCore/QAbstractItemModel-setHeaderData-f-1.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.setItemData
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            Dict[int, Any]
        :returns:
            bool
        :description: QtCore/QAbstractItemModel-setItemData-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.sibling
        :args:
            int
            int
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtCore/QAbstractItemModel-sibling-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.sort
        :args:
            int
            order: :sip:ref:`~PyQt6.QtCore.Qt.SortOrder` = :sip:ref:`~PyQt6.QtCore.Qt.SortOrder.AscendingOrder`
        :description: QtCore/QAbstractItemModel-sort-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.span
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtCore/QAbstractItemModel-span-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.submit
        :returns:
            bool
        :description: QtCore/QAbstractItemModel-submit-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.supportedDragActions
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.DropAction`
        :description: QtCore/QAbstractItemModel-supportedDragActions-f-1.rst

    .. sip:method:: PyQt6.QtCore.QAbstractItemModel.supportedDropActions
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.DropAction`
        :description: QtCore/QAbstractItemModel-supportedDropActions-f-1.rst

    .. sip:signal:: PyQt6.QtCore.QAbstractItemModel.columnsAboutToBeInserted
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            int
        :description: QtCore/QAbstractItemModel-columnsAboutToBeInserted-s.rst

    .. sip:signal:: PyQt6.QtCore.QAbstractItemModel.columnsAboutToBeMoved
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            int
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
        :description: QtCore/QAbstractItemModel-columnsAboutToBeMoved-s.rst

    .. sip:signal:: PyQt6.QtCore.QAbstractItemModel.columnsAboutToBeRemoved
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            int
        :description: QtCore/QAbstractItemModel-columnsAboutToBeRemoved-s.rst

    .. sip:signal:: PyQt6.QtCore.QAbstractItemModel.columnsInserted
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            int
        :description: QtCore/QAbstractItemModel-columnsInserted-s.rst

    .. sip:signal:: PyQt6.QtCore.QAbstractItemModel.columnsMoved
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            int
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
        :description: QtCore/QAbstractItemModel-columnsMoved-s.rst

    .. sip:signal:: PyQt6.QtCore.QAbstractItemModel.columnsRemoved
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            int
        :description: QtCore/QAbstractItemModel-columnsRemoved-s.rst

    .. sip:signal:: PyQt6.QtCore.QAbstractItemModel.dataChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            roles: Iterable[int] = []
        :description: QtCore/QAbstractItemModel-dataChanged-s.rst

    .. sip:signal:: PyQt6.QtCore.QAbstractItemModel.headerDataChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.Orientation`
            int
            int
        :description: QtCore/QAbstractItemModel-headerDataChanged-s-1.rst

    .. sip:signal:: PyQt6.QtCore.QAbstractItemModel.layoutAboutToBeChanged
        :args:
            parents: Iterable[:sip:ref:`~PyQt6.QtCore.QPersistentModelIndex`] = []
            hint: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.LayoutChangeHint` = :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.LayoutChangeHint.NoLayoutChangeHint`
        :description: QtCore/QAbstractItemModel-layoutAboutToBeChanged-s.rst

    .. sip:signal:: PyQt6.QtCore.QAbstractItemModel.layoutChanged
        :args:
            parents: Iterable[:sip:ref:`~PyQt6.QtCore.QPersistentModelIndex`] = []
            hint: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.LayoutChangeHint` = :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.LayoutChangeHint.NoLayoutChangeHint`
        :description: QtCore/QAbstractItemModel-layoutChanged-s.rst

    .. sip:signal:: PyQt6.QtCore.QAbstractItemModel.modelAboutToBeReset
        :description: QtCore/QAbstractItemModel-modelAboutToBeReset-s.rst

    .. sip:signal:: PyQt6.QtCore.QAbstractItemModel.modelReset
        :description: QtCore/QAbstractItemModel-modelReset-s.rst

    .. sip:signal:: PyQt6.QtCore.QAbstractItemModel.rowsAboutToBeInserted
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            int
        :description: QtCore/QAbstractItemModel-rowsAboutToBeInserted-s.rst

    .. sip:signal:: PyQt6.QtCore.QAbstractItemModel.rowsAboutToBeMoved
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            int
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
        :description: QtCore/QAbstractItemModel-rowsAboutToBeMoved-s.rst

    .. sip:signal:: PyQt6.QtCore.QAbstractItemModel.rowsAboutToBeRemoved
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            int
        :description: QtCore/QAbstractItemModel-rowsAboutToBeRemoved-s.rst

    .. sip:signal:: PyQt6.QtCore.QAbstractItemModel.rowsInserted
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            int
        :description: QtCore/QAbstractItemModel-rowsInserted-s.rst

    .. sip:signal:: PyQt6.QtCore.QAbstractItemModel.rowsMoved
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            int
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
        :description: QtCore/QAbstractItemModel-rowsMoved-s.rst

    .. sip:signal:: PyQt6.QtCore.QAbstractItemModel.rowsRemoved
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            int
        :description: QtCore/QAbstractItemModel-rowsRemoved-s.rst
