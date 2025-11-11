:orphan:

.. sip:class:: PyQt6.QtCore.QRangeModel
    :inherits: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`
    :description: QtCore/QRangeModel-c.rst

    .. sip:method:: PyQt6.QtCore.QRangeModel.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QPyAbstractRange`
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtCore/QRangeModel-__init__-f-1.rst

    .. sip:method:: PyQt6.QtCore.QRangeModel.buddy
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtCore/QRangeModel-buddy-f.rst

    .. sip:method:: PyQt6.QtCore.QRangeModel.canDropMimeData
        :args:
            :sip:ref:`~PyQt6.QtCore.QMimeData`
            :sip:ref:`~PyQt6.QtCore.Qt.DropAction`
            int
            int
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            bool
        :description: QtCore/QRangeModel-canDropMimeData-f.rst

    .. sip:method:: PyQt6.QtCore.QRangeModel.canFetchMore
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            bool
        :description: QtCore/QRangeModel-canFetchMore-f.rst

    .. sip:method:: PyQt6.QtCore.QRangeModel.clearItemData
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            bool
        :description: QtCore/QRangeModel-clearItemData-f.rst

    .. sip:method:: PyQt6.QtCore.QRangeModel.columnCount
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = {}
        :returns:
            int
        :description: QtCore/QRangeModel-columnCount-f.rst

    .. sip:method:: PyQt6.QtCore.QRangeModel.data
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            role: int = :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DisplayRole`
        :returns:
            Any
        :description: QtCore/QRangeModel-data-f.rst

    .. sip:method:: PyQt6.QtCore.QRangeModel.dropMimeData
        :args:
            :sip:ref:`~PyQt6.QtCore.QMimeData`
            :sip:ref:`~PyQt6.QtCore.Qt.DropAction`
            int
            int
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            bool
        :description: QtCore/QRangeModel-dropMimeData-f.rst

    .. sip:method:: PyQt6.QtCore.QRangeModel.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtCore/QRangeModel-event-f.rst

    .. sip:method:: PyQt6.QtCore.QRangeModel.eventFilter
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtCore/QRangeModel-eventFilter-f.rst

    .. sip:method:: PyQt6.QtCore.QRangeModel.fetchMore
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtCore/QRangeModel-fetchMore-f.rst

    .. sip:method:: PyQt6.QtCore.QRangeModel.flags
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.ItemFlag`
        :description: QtCore/QRangeModel-flags-f.rst

    .. sip:method:: PyQt6.QtCore.QRangeModel.hasChildren
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            bool
        :description: QtCore/QRangeModel-hasChildren-f.rst

    .. sip:method:: PyQt6.QtCore.QRangeModel.headerData
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.Qt.Orientation`
            role: int = :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DisplayRole`
        :returns:
            Any
        :description: QtCore/QRangeModel-headerData-f.rst

    .. sip:method:: PyQt6.QtCore.QRangeModel.index
        :args:
            int
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = {}
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtCore/QRangeModel-index-f.rst

    .. sip:method:: PyQt6.QtCore.QRangeModel.insertColumns
        :args:
            int
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = {}
        :returns:
            bool
        :description: QtCore/QRangeModel-insertColumns-f.rst

    .. sip:method:: PyQt6.QtCore.QRangeModel.insertRows
        :args:
            int
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = {}
        :returns:
            bool
        :description: QtCore/QRangeModel-insertRows-f.rst

    .. sip:method:: PyQt6.QtCore.QRangeModel.itemData
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            dict[int, Any]
        :description: QtCore/QRangeModel-itemData-f.rst

    .. sip:method:: PyQt6.QtCore.QRangeModel.match
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            Any
            int
            :sip:ref:`~PyQt6.QtCore.Qt.MatchFlag`
        :returns:
            list[:sip:ref:`~PyQt6.QtCore.QModelIndex`]
        :description: QtCore/QRangeModel-match-f.rst

    .. sip:method:: PyQt6.QtCore.QRangeModel.mimeData
        :args:
            Iterable[:sip:ref:`~PyQt6.QtCore.QModelIndex`]
        :returns:
            :sip:ref:`~PyQt6.QtCore.QMimeData`
        :description: QtCore/QRangeModel-mimeData-f.rst

    .. sip:method:: PyQt6.QtCore.QRangeModel.mimeTypes
        :returns:
            list[str]
        :description: QtCore/QRangeModel-mimeTypes-f.rst

    .. sip:method:: PyQt6.QtCore.QRangeModel.moveColumns
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            int
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
        :returns:
            bool
        :description: QtCore/QRangeModel-moveColumns-f.rst

    .. sip:method:: PyQt6.QtCore.QRangeModel.moveRows
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            int
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
        :returns:
            bool
        :description: QtCore/QRangeModel-moveRows-f.rst

    .. sip:method:: PyQt6.QtCore.QRangeModel.multiData
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            :sip:ref:`~PyQt6.QtCore.QModelRoleDataSpan`
        :description: QtCore/QRangeModel-multiData-f.rst

    .. sip:method:: PyQt6.QtCore.QRangeModel.parent
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtCore/QRangeModel-parent-f.rst

    .. sip:method:: PyQt6.QtCore.QRangeModel.removeColumns
        :args:
            int
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = {}
        :returns:
            bool
        :description: QtCore/QRangeModel-removeColumns-f.rst

    .. sip:method:: PyQt6.QtCore.QRangeModel.removeRows
        :args:
            int
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = {}
        :returns:
            bool
        :description: QtCore/QRangeModel-removeRows-f.rst

    .. sip:method:: PyQt6.QtCore.QRangeModel.resetInternalData
        :description: QtCore/QRangeModel-resetInternalData-f.rst

    .. sip:method:: PyQt6.QtCore.QRangeModel.resetRoleNames
        :description: QtCore/QRangeModel-resetRoleNames-f.rst

    .. sip:method:: PyQt6.QtCore.QRangeModel.roleNames
        :returns:
            dict[int, :sip:ref:`~PyQt6.QtCore.QByteArray`]
        :description: QtCore/QRangeModel-roleNames-f.rst

    .. sip:method:: PyQt6.QtCore.QRangeModel.rowCount
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = {}
        :returns:
            int
        :description: QtCore/QRangeModel-rowCount-f.rst

    .. sip:method:: PyQt6.QtCore.QRangeModel.setData
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            Any
            role: int = :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.EditRole`
        :returns:
            bool
        :description: QtCore/QRangeModel-setData-f.rst

    .. sip:method:: PyQt6.QtCore.QRangeModel.setHeaderData
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.Qt.Orientation`
            Any
            role: int = :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.EditRole`
        :returns:
            bool
        :description: QtCore/QRangeModel-setHeaderData-f.rst

    .. sip:method:: PyQt6.QtCore.QRangeModel.setItemData
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            dict[int, Any]
        :returns:
            bool
        :description: QtCore/QRangeModel-setItemData-f.rst

    .. sip:method:: PyQt6.QtCore.QRangeModel.setRoleNames
        :args:
            dict[int, Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]]
        :description: QtCore/QRangeModel-setRoleNames-f.rst

    .. sip:method:: PyQt6.QtCore.QRangeModel.sibling
        :args:
            int
            int
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtCore/QRangeModel-sibling-f.rst

    .. sip:method:: PyQt6.QtCore.QRangeModel.sort
        :args:
            int
            order: :sip:ref:`~PyQt6.QtCore.Qt.SortOrder` = :sip:ref:`~PyQt6.QtCore.Qt.SortOrder.AscendingOrder`
        :description: QtCore/QRangeModel-sort-f.rst

    .. sip:method:: PyQt6.QtCore.QRangeModel.span
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtCore/QRangeModel-span-f.rst

    .. sip:method:: PyQt6.QtCore.QRangeModel.supportedDragActions
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.DropAction`
        :description: QtCore/QRangeModel-supportedDragActions-f.rst

    .. sip:method:: PyQt6.QtCore.QRangeModel.supportedDropActions
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.DropAction`
        :description: QtCore/QRangeModel-supportedDropActions-f.rst

    .. sip:signal:: PyQt6.QtCore.QRangeModel.roleNamesChanged
        :description: QtCore/QRangeModel-roleNamesChanged-s.rst
