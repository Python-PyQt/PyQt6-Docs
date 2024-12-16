:orphan:

.. sip:class:: PyQt6.QtCore.QIdentityProxyModel
    :inherits: :sip:ref:`~PyQt6.QtCore.QAbstractProxyModel`
    :description: QtCore/QIdentityProxyModel-c.rst

    .. sip:method:: PyQt6.QtCore.QIdentityProxyModel.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtCore/QIdentityProxyModel-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QIdentityProxyModel.columnCount
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            int
        :description: QtCore/QIdentityProxyModel-columnCount-f.rst

    .. sip:method:: PyQt6.QtCore.QIdentityProxyModel.dropMimeData
        :args:
            :sip:ref:`~PyQt6.QtCore.QMimeData`
            :sip:ref:`~PyQt6.QtCore.Qt.DropAction`
            int
            int
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            bool
        :description: QtCore/QIdentityProxyModel-dropMimeData-f-1.rst

    .. sip:method:: PyQt6.QtCore.QIdentityProxyModel.handleSourceDataChanges
        :returns:
            bool
        :description: QtCore/QIdentityProxyModel-handleSourceDataChanges-f.rst

    .. sip:method:: PyQt6.QtCore.QIdentityProxyModel.handleSourceLayoutChanges
        :returns:
            bool
        :description: QtCore/QIdentityProxyModel-handleSourceLayoutChanges-f.rst

    .. sip:method:: PyQt6.QtCore.QIdentityProxyModel.headerData
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.Qt.Orientation`
            role: int = :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DisplayRole`
        :returns:
            Any
        :description: QtCore/QIdentityProxyModel-headerData-f-1.rst

    .. sip:method:: PyQt6.QtCore.QIdentityProxyModel.index
        :args:
            int
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtCore/QIdentityProxyModel-index-f.rst

    .. sip:method:: PyQt6.QtCore.QIdentityProxyModel.insertColumns
        :args:
            int
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            bool
        :description: QtCore/QIdentityProxyModel-insertColumns-f.rst

    .. sip:method:: PyQt6.QtCore.QIdentityProxyModel.insertRows
        :args:
            int
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            bool
        :description: QtCore/QIdentityProxyModel-insertRows-f.rst

    .. sip:method:: PyQt6.QtCore.QIdentityProxyModel.mapFromSource
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtCore/QIdentityProxyModel-mapFromSource-f.rst

    .. sip:method:: PyQt6.QtCore.QIdentityProxyModel.mapSelectionFromSource
        :args:
            :sip:ref:`~PyQt6.QtCore.QItemSelection`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QItemSelection`
        :description: QtCore/QIdentityProxyModel-mapSelectionFromSource-f.rst

    .. sip:method:: PyQt6.QtCore.QIdentityProxyModel.mapSelectionToSource
        :args:
            :sip:ref:`~PyQt6.QtCore.QItemSelection`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QItemSelection`
        :description: QtCore/QIdentityProxyModel-mapSelectionToSource-f.rst

    .. sip:method:: PyQt6.QtCore.QIdentityProxyModel.mapToSource
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtCore/QIdentityProxyModel-mapToSource-f.rst

    .. sip:method:: PyQt6.QtCore.QIdentityProxyModel.match
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            Any
            hits: int = 1
            flags: :sip:ref:`~PyQt6.QtCore.Qt.MatchFlag` = Qt.MatchFlags(Qt.MatchStartsWith|Qt.MatchWrap)
        :returns:
            list[:sip:ref:`~PyQt6.QtCore.QModelIndex`]
        :description: QtCore/QIdentityProxyModel-match-f.rst

    .. sip:method:: PyQt6.QtCore.QIdentityProxyModel.moveColumns
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            int
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
        :returns:
            bool
        :description: QtCore/QIdentityProxyModel-moveColumns-f.rst

    .. sip:method:: PyQt6.QtCore.QIdentityProxyModel.moveRows
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            int
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
        :returns:
            bool
        :description: QtCore/QIdentityProxyModel-moveRows-f.rst

    .. sip:method:: PyQt6.QtCore.QIdentityProxyModel.parent
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtCore/QIdentityProxyModel-parent-f.rst

    .. sip:method:: PyQt6.QtCore.QIdentityProxyModel.removeColumns
        :args:
            int
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            bool
        :description: QtCore/QIdentityProxyModel-removeColumns-f.rst

    .. sip:method:: PyQt6.QtCore.QIdentityProxyModel.removeRows
        :args:
            int
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            bool
        :description: QtCore/QIdentityProxyModel-removeRows-f.rst

    .. sip:method:: PyQt6.QtCore.QIdentityProxyModel.rowCount
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            int
        :description: QtCore/QIdentityProxyModel-rowCount-f.rst

    .. sip:method:: PyQt6.QtCore.QIdentityProxyModel.setHandleSourceDataChanges
        :args:
            bool
        :description: QtCore/QIdentityProxyModel-setHandleSourceDataChanges-f.rst

    .. sip:method:: PyQt6.QtCore.QIdentityProxyModel.setHandleSourceLayoutChanges
        :args:
            bool
        :description: QtCore/QIdentityProxyModel-setHandleSourceLayoutChanges-f.rst

    .. sip:method:: PyQt6.QtCore.QIdentityProxyModel.setSourceModel
        :args:
            :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`
        :description: QtCore/QIdentityProxyModel-setSourceModel-f.rst

    .. sip:method:: PyQt6.QtCore.QIdentityProxyModel.sibling
        :args:
            int
            int
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtCore/QIdentityProxyModel-sibling-f.rst
