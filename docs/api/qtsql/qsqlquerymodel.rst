:orphan:

.. sip:class:: PyQt6.QtSql.QSqlQueryModel
    :inherits: :sip:ref:`~PyQt6.QtCore.QAbstractTableModel`
    :description: QtSql/QSqlQueryModel-c.rst

    .. sip:method:: PyQt6.QtSql.QSqlQueryModel.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtSql/QSqlQueryModel-__init__-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQueryModel.beginInsertColumns
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            int
        :description: QtSql/QSqlQueryModel-beginInsertColumns-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQueryModel.beginInsertRows
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            int
        :description: QtSql/QSqlQueryModel-beginInsertRows-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQueryModel.beginRemoveColumns
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            int
        :description: QtSql/QSqlQueryModel-beginRemoveColumns-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQueryModel.beginRemoveRows
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            int
        :description: QtSql/QSqlQueryModel-beginRemoveRows-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQueryModel.beginResetModel
        :description: QtSql/QSqlQueryModel-beginResetModel-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQueryModel.canFetchMore
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            bool
        :description: QtSql/QSqlQueryModel-canFetchMore-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQueryModel.clear
        :description: QtSql/QSqlQueryModel-clear-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQueryModel.columnCount
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            int
        :description: QtSql/QSqlQueryModel-columnCount-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQueryModel.data
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            role: int = :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DisplayRole`
        :returns:
            Any
        :description: QtSql/QSqlQueryModel-data-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQueryModel.endInsertColumns
        :description: QtSql/QSqlQueryModel-endInsertColumns-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQueryModel.endInsertRows
        :description: QtSql/QSqlQueryModel-endInsertRows-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQueryModel.endRemoveColumns
        :description: QtSql/QSqlQueryModel-endRemoveColumns-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQueryModel.endRemoveRows
        :description: QtSql/QSqlQueryModel-endRemoveRows-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQueryModel.endResetModel
        :description: QtSql/QSqlQueryModel-endResetModel-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQueryModel.fetchMore
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :description: QtSql/QSqlQueryModel-fetchMore-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQueryModel.headerData
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.Qt.Orientation`
            role: int = :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DisplayRole`
        :returns:
            Any
        :description: QtSql/QSqlQueryModel-headerData-f-1.rst

    .. sip:method:: PyQt6.QtSql.QSqlQueryModel.indexInQuery
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtSql/QSqlQueryModel-indexInQuery-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQueryModel.insertColumns
        :args:
            int
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            bool
        :description: QtSql/QSqlQueryModel-insertColumns-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQueryModel.lastError
        :returns:
            :sip:ref:`~PyQt6.QtSql.QSqlError`
        :description: QtSql/QSqlQueryModel-lastError-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQueryModel.query
        :returns:
            :sip:ref:`~PyQt6.QtSql.QSqlQuery`
        :description: QtSql/QSqlQueryModel-query-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQueryModel.queryChange
        :description: QtSql/QSqlQueryModel-queryChange-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQueryModel.record
        :returns:
            :sip:ref:`~PyQt6.QtSql.QSqlRecord`
        :description: QtSql/QSqlQueryModel-record-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQueryModel.record
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtSql.QSqlRecord`
        :description: QtSql/QSqlQueryModel-record-f-1.rst

    .. sip:method:: PyQt6.QtSql.QSqlQueryModel.removeColumns
        :args:
            int
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            bool
        :description: QtSql/QSqlQueryModel-removeColumns-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQueryModel.roleNames
        :returns:
            Dict[int, :sip:ref:`~PyQt6.QtCore.QByteArray`]
        :description: QtSql/QSqlQueryModel-roleNames-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQueryModel.rowCount
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            int
        :description: QtSql/QSqlQueryModel-rowCount-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQueryModel.setHeaderData
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.Qt.Orientation`
            Any
            role: int = :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.EditRole`
        :returns:
            bool
        :description: QtSql/QSqlQueryModel-setHeaderData-f-1.rst

    .. sip:method:: PyQt6.QtSql.QSqlQueryModel.setLastError
        :args:
            :sip:ref:`~PyQt6.QtSql.QSqlError`
        :description: QtSql/QSqlQueryModel-setLastError-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQueryModel.setQuery
        :args:
            :sip:ref:`~PyQt6.QtSql.QSqlQuery`
        :description: QtSql/QSqlQueryModel-setQuery-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQueryModel.setQuery
        :args:
            str
            db: :sip:ref:`~PyQt6.QtSql.QSqlDatabase` = QSqlDatabase()
        :description: QtSql/QSqlQueryModel-setQuery-f-1.rst
