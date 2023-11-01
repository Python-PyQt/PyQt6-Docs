:orphan:

.. sip:class:: PyQt6.QtCore.QSortFilterProxyModel
    :inherits: :sip:ref:`~PyQt6.QtCore.QAbstractProxyModel`
    :description: QtCore/QSortFilterProxyModel-c.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtCore/QSortFilterProxyModel-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.autoAcceptChildRows
        :returns:
            bool
        :description: QtCore/QSortFilterProxyModel-autoAcceptChildRows-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.buddy
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtCore/QSortFilterProxyModel-buddy-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.canFetchMore
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            bool
        :description: QtCore/QSortFilterProxyModel-canFetchMore-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.columnCount
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            int
        :description: QtCore/QSortFilterProxyModel-columnCount-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.data
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            role: int = :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DisplayRole`
        :returns:
            Any
        :description: QtCore/QSortFilterProxyModel-data-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.dropMimeData
        :args:
            :sip:ref:`~PyQt6.QtCore.QMimeData`
            :sip:ref:`~PyQt6.QtCore.Qt.DropAction`
            int
            int
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            bool
        :description: QtCore/QSortFilterProxyModel-dropMimeData-f-1.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.dynamicSortFilter
        :returns:
            bool
        :description: QtCore/QSortFilterProxyModel-dynamicSortFilter-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.fetchMore
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtCore/QSortFilterProxyModel-fetchMore-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.filterAcceptsColumn
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            bool
        :description: QtCore/QSortFilterProxyModel-filterAcceptsColumn-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.filterAcceptsRow
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            bool
        :description: QtCore/QSortFilterProxyModel-filterAcceptsRow-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.filterCaseSensitivity
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.CaseSensitivity`
        :description: QtCore/QSortFilterProxyModel-filterCaseSensitivity-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.filterKeyColumn
        :returns:
            int
        :description: QtCore/QSortFilterProxyModel-filterKeyColumn-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.filterRegularExpression
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRegularExpression`
        :description: QtCore/QSortFilterProxyModel-filterRegularExpression-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.filterRole
        :returns:
            int
        :description: QtCore/QSortFilterProxyModel-filterRole-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.flags
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.ItemFlag`
        :description: QtCore/QSortFilterProxyModel-flags-f-1.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.hasChildren
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            bool
        :description: QtCore/QSortFilterProxyModel-hasChildren-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.headerData
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.Qt.Orientation`
            role: int = :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DisplayRole`
        :returns:
            Any
        :description: QtCore/QSortFilterProxyModel-headerData-f-1.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.index
        :args:
            int
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtCore/QSortFilterProxyModel-index-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.insertColumns
        :args:
            int
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            bool
        :description: QtCore/QSortFilterProxyModel-insertColumns-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.insertRows
        :args:
            int
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            bool
        :description: QtCore/QSortFilterProxyModel-insertRows-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.invalidate
        :description: QtCore/QSortFilterProxyModel-invalidate-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.invalidateColumnsFilter
        :description: QtCore/QSortFilterProxyModel-invalidateColumnsFilter-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.invalidateFilter
        :description: QtCore/QSortFilterProxyModel-invalidateFilter-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.invalidateRowsFilter
        :description: QtCore/QSortFilterProxyModel-invalidateRowsFilter-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.isRecursiveFilteringEnabled
        :returns:
            bool
        :description: QtCore/QSortFilterProxyModel-isRecursiveFilteringEnabled-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.isSortLocaleAware
        :returns:
            bool
        :description: QtCore/QSortFilterProxyModel-isSortLocaleAware-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.lessThan
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            bool
        :description: QtCore/QSortFilterProxyModel-lessThan-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.mapFromSource
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtCore/QSortFilterProxyModel-mapFromSource-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.mapSelectionFromSource
        :args:
            :sip:ref:`~PyQt6.QtCore.QItemSelection`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QItemSelection`
        :description: QtCore/QSortFilterProxyModel-mapSelectionFromSource-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.mapSelectionToSource
        :args:
            :sip:ref:`~PyQt6.QtCore.QItemSelection`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QItemSelection`
        :description: QtCore/QSortFilterProxyModel-mapSelectionToSource-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.mapToSource
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtCore/QSortFilterProxyModel-mapToSource-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.match
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            Any
            hits: int = 1
            flags: :sip:ref:`~PyQt6.QtCore.Qt.MatchFlag` = Qt.MatchFlags(Qt.MatchStartsWith|Qt.MatchWrap)
        :returns:
            List[:sip:ref:`~PyQt6.QtCore.QModelIndex`]
        :description: QtCore/QSortFilterProxyModel-match-f-1.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.mimeData
        :args:
            Iterable[:sip:ref:`~PyQt6.QtCore.QModelIndex`]
        :returns:
            :sip:ref:`~PyQt6.QtCore.QMimeData`
        :description: QtCore/QSortFilterProxyModel-mimeData-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.mimeTypes
        :returns:
            List[str]
        :description: QtCore/QSortFilterProxyModel-mimeTypes-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.parent
        :returns:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :description: QtCore/QSortFilterProxyModel-parent-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.parent
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtCore/QSortFilterProxyModel-parent-f-1.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.removeColumns
        :args:
            int
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            bool
        :description: QtCore/QSortFilterProxyModel-removeColumns-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.removeRows
        :args:
            int
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            bool
        :description: QtCore/QSortFilterProxyModel-removeRows-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.rowCount
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            int
        :description: QtCore/QSortFilterProxyModel-rowCount-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.setAutoAcceptChildRows
        :args:
            bool
        :description: QtCore/QSortFilterProxyModel-setAutoAcceptChildRows-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.setData
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            Any
            role: int = :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.EditRole`
        :returns:
            bool
        :description: QtCore/QSortFilterProxyModel-setData-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.setDynamicSortFilter
        :args:
            bool
        :description: QtCore/QSortFilterProxyModel-setDynamicSortFilter-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.setFilterCaseSensitivity
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.CaseSensitivity`
        :description: QtCore/QSortFilterProxyModel-setFilterCaseSensitivity-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.setFilterFixedString
        :args:
            Optional[str]
        :description: QtCore/QSortFilterProxyModel-setFilterFixedString-f-1.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.setFilterKeyColumn
        :args:
            int
        :description: QtCore/QSortFilterProxyModel-setFilterKeyColumn-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.setFilterRegularExpression
        :args:
            :sip:ref:`~PyQt6.QtCore.QRegularExpression`
        :description: QtCore/QSortFilterProxyModel-setFilterRegularExpression-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.setFilterRegularExpression
        :args:
            Optional[str]
        :description: QtCore/QSortFilterProxyModel-setFilterRegularExpression-f-2.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.setFilterRole
        :args:
            int
        :description: QtCore/QSortFilterProxyModel-setFilterRole-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.setFilterWildcard
        :args:
            Optional[str]
        :description: QtCore/QSortFilterProxyModel-setFilterWildcard-f-1.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.setHeaderData
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.Qt.Orientation`
            Any
            role: int = :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.EditRole`
        :returns:
            bool
        :description: QtCore/QSortFilterProxyModel-setHeaderData-f-1.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.setRecursiveFilteringEnabled
        :args:
            bool
        :description: QtCore/QSortFilterProxyModel-setRecursiveFilteringEnabled-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.setSortCaseSensitivity
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.CaseSensitivity`
        :description: QtCore/QSortFilterProxyModel-setSortCaseSensitivity-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.setSortLocaleAware
        :args:
            bool
        :description: QtCore/QSortFilterProxyModel-setSortLocaleAware-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.setSortRole
        :args:
            int
        :description: QtCore/QSortFilterProxyModel-setSortRole-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.setSourceModel
        :args:
            :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`
        :description: QtCore/QSortFilterProxyModel-setSourceModel-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.sibling
        :args:
            int
            int
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtCore/QSortFilterProxyModel-sibling-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.sort
        :args:
            int
            order: :sip:ref:`~PyQt6.QtCore.Qt.SortOrder` = :sip:ref:`~PyQt6.QtCore.Qt.SortOrder.AscendingOrder`
        :description: QtCore/QSortFilterProxyModel-sort-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.sortCaseSensitivity
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.CaseSensitivity`
        :description: QtCore/QSortFilterProxyModel-sortCaseSensitivity-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.sortColumn
        :returns:
            int
        :description: QtCore/QSortFilterProxyModel-sortColumn-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.sortOrder
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.SortOrder`
        :description: QtCore/QSortFilterProxyModel-sortOrder-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.sortRole
        :returns:
            int
        :description: QtCore/QSortFilterProxyModel-sortRole-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.span
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtCore/QSortFilterProxyModel-span-f.rst

    .. sip:method:: PyQt6.QtCore.QSortFilterProxyModel.supportedDropActions
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.DropAction`
        :description: QtCore/QSortFilterProxyModel-supportedDropActions-f-1.rst

    .. sip:signal:: PyQt6.QtCore.QSortFilterProxyModel.autoAcceptChildRowsChanged
        :args:
            bool
        :description: QtCore/QSortFilterProxyModel-autoAcceptChildRowsChanged-s.rst

    .. sip:signal:: PyQt6.QtCore.QSortFilterProxyModel.dynamicSortFilterChanged
        :args:
            bool
        :description: QtCore/QSortFilterProxyModel-dynamicSortFilterChanged-s.rst

    .. sip:signal:: PyQt6.QtCore.QSortFilterProxyModel.filterCaseSensitivityChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.CaseSensitivity`
        :description: QtCore/QSortFilterProxyModel-filterCaseSensitivityChanged-s.rst

    .. sip:signal:: PyQt6.QtCore.QSortFilterProxyModel.filterRoleChanged
        :args:
            int
        :description: QtCore/QSortFilterProxyModel-filterRoleChanged-s.rst

    .. sip:signal:: PyQt6.QtCore.QSortFilterProxyModel.recursiveFilteringEnabledChanged
        :args:
            bool
        :description: QtCore/QSortFilterProxyModel-recursiveFilteringEnabledChanged-s.rst

    .. sip:signal:: PyQt6.QtCore.QSortFilterProxyModel.sortCaseSensitivityChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.CaseSensitivity`
        :description: QtCore/QSortFilterProxyModel-sortCaseSensitivityChanged-s.rst

    .. sip:signal:: PyQt6.QtCore.QSortFilterProxyModel.sortLocaleAwareChanged
        :args:
            bool
        :description: QtCore/QSortFilterProxyModel-sortLocaleAwareChanged-s.rst

    .. sip:signal:: PyQt6.QtCore.QSortFilterProxyModel.sortRoleChanged
        :args:
            int
        :description: QtCore/QSortFilterProxyModel-sortRoleChanged-s.rst
