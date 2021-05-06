:orphan:

.. sip:class:: PyQt6.QtCore.QConcatenateTablesProxyModel
    :inherits: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`
    :description: QtCore/QConcatenateTablesProxyModel-c.rst

    .. sip:method:: PyQt6.QtCore.QConcatenateTablesProxyModel.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtCore/QConcatenateTablesProxyModel-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QConcatenateTablesProxyModel.addSourceModel
        :args:
            :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`
        :description: QtCore/QConcatenateTablesProxyModel-addSourceModel-f.rst

    .. sip:method:: PyQt6.QtCore.QConcatenateTablesProxyModel.canDropMimeData
        :args:
            :sip:ref:`~PyQt6.QtCore.QMimeData`
            :sip:ref:`~PyQt6.QtCore.Qt.DropAction`
            int
            int
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            bool
        :description: QtCore/QConcatenateTablesProxyModel-canDropMimeData-f-1.rst

    .. sip:method:: PyQt6.QtCore.QConcatenateTablesProxyModel.columnCount
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            int
        :description: QtCore/QConcatenateTablesProxyModel-columnCount-f.rst

    .. sip:method:: PyQt6.QtCore.QConcatenateTablesProxyModel.data
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            role: int = :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DisplayRole`
        :returns:
            Any
        :description: QtCore/QConcatenateTablesProxyModel-data-f.rst

    .. sip:method:: PyQt6.QtCore.QConcatenateTablesProxyModel.dropMimeData
        :args:
            :sip:ref:`~PyQt6.QtCore.QMimeData`
            :sip:ref:`~PyQt6.QtCore.Qt.DropAction`
            int
            int
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            bool
        :description: QtCore/QConcatenateTablesProxyModel-dropMimeData-f-1.rst

    .. sip:method:: PyQt6.QtCore.QConcatenateTablesProxyModel.flags
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.ItemFlag`
        :description: QtCore/QConcatenateTablesProxyModel-flags-f-1.rst

    .. sip:method:: PyQt6.QtCore.QConcatenateTablesProxyModel.headerData
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.Qt.Orientation`
            role: int = :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DisplayRole`
        :returns:
            Any
        :description: QtCore/QConcatenateTablesProxyModel-headerData-f-1.rst

    .. sip:method:: PyQt6.QtCore.QConcatenateTablesProxyModel.index
        :args:
            int
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtCore/QConcatenateTablesProxyModel-index-f.rst

    .. sip:method:: PyQt6.QtCore.QConcatenateTablesProxyModel.itemData
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            Dict[int, Any]
        :description: QtCore/QConcatenateTablesProxyModel-itemData-f.rst

    .. sip:method:: PyQt6.QtCore.QConcatenateTablesProxyModel.mapFromSource
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtCore/QConcatenateTablesProxyModel-mapFromSource-f.rst

    .. sip:method:: PyQt6.QtCore.QConcatenateTablesProxyModel.mapToSource
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtCore/QConcatenateTablesProxyModel-mapToSource-f.rst

    .. sip:method:: PyQt6.QtCore.QConcatenateTablesProxyModel.mimeData
        :args:
            Iterable[:sip:ref:`~PyQt6.QtCore.QModelIndex`]
        :returns:
            :sip:ref:`~PyQt6.QtCore.QMimeData`
        :description: QtCore/QConcatenateTablesProxyModel-mimeData-f.rst

    .. sip:method:: PyQt6.QtCore.QConcatenateTablesProxyModel.mimeTypes
        :returns:
            List[str]
        :description: QtCore/QConcatenateTablesProxyModel-mimeTypes-f.rst

    .. sip:method:: PyQt6.QtCore.QConcatenateTablesProxyModel.parent
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtCore/QConcatenateTablesProxyModel-parent-f.rst

    .. sip:method:: PyQt6.QtCore.QConcatenateTablesProxyModel.removeSourceModel
        :args:
            :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`
        :description: QtCore/QConcatenateTablesProxyModel-removeSourceModel-f.rst

    .. sip:method:: PyQt6.QtCore.QConcatenateTablesProxyModel.rowCount
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            int
        :description: QtCore/QConcatenateTablesProxyModel-rowCount-f.rst

    .. sip:method:: PyQt6.QtCore.QConcatenateTablesProxyModel.setData
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            Any
            role: int = :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.EditRole`
        :returns:
            bool
        :description: QtCore/QConcatenateTablesProxyModel-setData-f.rst

    .. sip:method:: PyQt6.QtCore.QConcatenateTablesProxyModel.setItemData
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            Dict[int, Any]
        :returns:
            bool
        :description: QtCore/QConcatenateTablesProxyModel-setItemData-f.rst

    .. sip:method:: PyQt6.QtCore.QConcatenateTablesProxyModel.sourceModels
        :returns:
            List[:sip:ref:`~PyQt6.QtCore.QAbstractItemModel`]
        :description: QtCore/QConcatenateTablesProxyModel-sourceModels-f.rst

    .. sip:method:: PyQt6.QtCore.QConcatenateTablesProxyModel.span
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtCore/QConcatenateTablesProxyModel-span-f.rst
