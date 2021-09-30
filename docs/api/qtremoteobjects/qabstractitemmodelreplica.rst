:orphan:

.. sip:class:: PyQt6.QtRemoteObjects.QAbstractItemModelReplica
    :inherits: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`
    :description: QtRemoteObjects/QAbstractItemModelReplica-c.rst

    .. sip:method:: PyQt6.QtRemoteObjects.QAbstractItemModelReplica.availableRoles
        :returns:
            List[int]
        :description: QtRemoteObjects/QAbstractItemModelReplica-availableRoles-f.rst

    .. sip:method:: PyQt6.QtRemoteObjects.QAbstractItemModelReplica.columnCount
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            int
        :description: QtRemoteObjects/QAbstractItemModelReplica-columnCount-f.rst

    .. sip:method:: PyQt6.QtRemoteObjects.QAbstractItemModelReplica.data
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            role: int = :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DisplayRole`
        :returns:
            Any
        :description: QtRemoteObjects/QAbstractItemModelReplica-data-f.rst

    .. sip:method:: PyQt6.QtRemoteObjects.QAbstractItemModelReplica.flags
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.ItemFlag`
        :description: QtRemoteObjects/QAbstractItemModelReplica-flags-f.rst

    .. sip:method:: PyQt6.QtRemoteObjects.QAbstractItemModelReplica.hasChildren
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            bool
        :description: QtRemoteObjects/QAbstractItemModelReplica-hasChildren-f.rst

    .. sip:method:: PyQt6.QtRemoteObjects.QAbstractItemModelReplica.hasData
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
        :returns:
            bool
        :description: QtRemoteObjects/QAbstractItemModelReplica-hasData-f.rst

    .. sip:method:: PyQt6.QtRemoteObjects.QAbstractItemModelReplica.headerData
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.Qt.Orientation`
            int
        :returns:
            Any
        :description: QtRemoteObjects/QAbstractItemModelReplica-headerData-f.rst

    .. sip:method:: PyQt6.QtRemoteObjects.QAbstractItemModelReplica.index
        :args:
            int
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtRemoteObjects/QAbstractItemModelReplica-index-f.rst

    .. sip:method:: PyQt6.QtRemoteObjects.QAbstractItemModelReplica.isInitialized
        :returns:
            bool
        :description: QtRemoteObjects/QAbstractItemModelReplica-isInitialized-f.rst

    .. sip:method:: PyQt6.QtRemoteObjects.QAbstractItemModelReplica.parent
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtRemoteObjects/QAbstractItemModelReplica-parent-f.rst

    .. sip:method:: PyQt6.QtRemoteObjects.QAbstractItemModelReplica.roleNames
        :returns:
            Dict[int, :sip:ref:`~PyQt6.QtCore.QByteArray`]
        :description: QtRemoteObjects/QAbstractItemModelReplica-roleNames-f.rst

    .. sip:method:: PyQt6.QtRemoteObjects.QAbstractItemModelReplica.rootCacheSize
        :returns:
            int
        :description: QtRemoteObjects/QAbstractItemModelReplica-rootCacheSize-f.rst

    .. sip:method:: PyQt6.QtRemoteObjects.QAbstractItemModelReplica.rowCount
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            int
        :description: QtRemoteObjects/QAbstractItemModelReplica-rowCount-f.rst

    .. sip:method:: PyQt6.QtRemoteObjects.QAbstractItemModelReplica.selectionModel
        :returns:
            :sip:ref:`~PyQt6.QtCore.QItemSelectionModel`
        :description: QtRemoteObjects/QAbstractItemModelReplica-selectionModel-f.rst

    .. sip:method:: PyQt6.QtRemoteObjects.QAbstractItemModelReplica.setData
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            Any
            role: int = :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.EditRole`
        :returns:
            bool
        :description: QtRemoteObjects/QAbstractItemModelReplica-setData-f.rst

    .. sip:method:: PyQt6.QtRemoteObjects.QAbstractItemModelReplica.setRootCacheSize
        :args:
            int
        :description: QtRemoteObjects/QAbstractItemModelReplica-setRootCacheSize-f.rst

    .. sip:signal:: PyQt6.QtRemoteObjects.QAbstractItemModelReplica.initialized
        :description: QtRemoteObjects/QAbstractItemModelReplica-initialized-s.rst
