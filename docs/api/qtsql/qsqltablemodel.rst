:orphan:

.. sip:class:: PyQt6.QtSql.QSqlTableModel
    :inherits: :sip:ref:`~PyQt6.QtSql.QSqlQueryModel`
    :description: QtSql/QSqlTableModel-c.rst

    .. sip:enum:: PyQt6.QtSql.QSqlTableModel.EditStrategy
        :description: QtSql/QSqlTableModel-EditStrategy-e.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlTableModel.EditStrategy.OnFieldChange
            :description: QtSql/QSqlTableModel-EditStrategy-OnFieldChange-v.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlTableModel.EditStrategy.OnManualSubmit
            :description: QtSql/QSqlTableModel-EditStrategy-OnManualSubmit-v.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlTableModel.EditStrategy.OnRowChange
            :description: QtSql/QSqlTableModel-EditStrategy-OnRowChange-v.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
            db: :sip:ref:`~PyQt6.QtSql.QSqlDatabase` = QSqlDatabase()
        :description: QtSql/QSqlTableModel-__init__-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.clear
        :description: QtSql/QSqlTableModel-clear-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.clearItemData
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            bool
        :description: QtSql/QSqlTableModel-clearItemData-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.data
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            role: int = :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DisplayRole`
        :returns:
            Any
        :description: QtSql/QSqlTableModel-data-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.database
        :returns:
            :sip:ref:`~PyQt6.QtSql.QSqlDatabase`
        :description: QtSql/QSqlTableModel-database-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.deleteRowFromTable
        :args:
            int
        :returns:
            bool
        :description: QtSql/QSqlTableModel-deleteRowFromTable-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.editStrategy
        :returns:
            :sip:ref:`~PyQt6.QtSql.QSqlTableModel.EditStrategy`
        :description: QtSql/QSqlTableModel-editStrategy-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.fieldIndex
        :args:
            str
        :returns:
            int
        :description: QtSql/QSqlTableModel-fieldIndex-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.filter
        :returns:
            str
        :description: QtSql/QSqlTableModel-filter-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.flags
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.ItemFlag`
        :description: QtSql/QSqlTableModel-flags-f-1.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.headerData
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.Qt.Orientation`
            role: int = :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DisplayRole`
        :returns:
            Any
        :description: QtSql/QSqlTableModel-headerData-f-1.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.indexInQuery
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtSql/QSqlTableModel-indexInQuery-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.insertRecord
        :args:
            int
            :sip:ref:`~PyQt6.QtSql.QSqlRecord`
        :returns:
            bool
        :description: QtSql/QSqlTableModel-insertRecord-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.insertRowIntoTable
        :args:
            :sip:ref:`~PyQt6.QtSql.QSqlRecord`
        :returns:
            bool
        :description: QtSql/QSqlTableModel-insertRowIntoTable-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.insertRows
        :args:
            int
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            bool
        :description: QtSql/QSqlTableModel-insertRows-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.isDirty
        :returns:
            bool
        :description: QtSql/QSqlTableModel-isDirty-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.isDirty
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            bool
        :description: QtSql/QSqlTableModel-isDirty-f-1.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.orderByClause
        :returns:
            str
        :description: QtSql/QSqlTableModel-orderByClause-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.primaryKey
        :returns:
            :sip:ref:`~PyQt6.QtSql.QSqlIndex`
        :description: QtSql/QSqlTableModel-primaryKey-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.primaryValues
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtSql.QSqlRecord`
        :description: QtSql/QSqlTableModel-primaryValues-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.record
        :returns:
            :sip:ref:`~PyQt6.QtSql.QSqlRecord`
        :description: QtSql/QSqlTableModel-record-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.record
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtSql.QSqlRecord`
        :description: QtSql/QSqlTableModel-record-f-1.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.removeColumns
        :args:
            int
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            bool
        :description: QtSql/QSqlTableModel-removeColumns-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.removeRows
        :args:
            int
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            bool
        :description: QtSql/QSqlTableModel-removeRows-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.revert
        :description: QtSql/QSqlTableModel-revert-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.revertAll
        :description: QtSql/QSqlTableModel-revertAll-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.revertRow
        :args:
            int
        :description: QtSql/QSqlTableModel-revertRow-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.rowCount
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            int
        :description: QtSql/QSqlTableModel-rowCount-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.select
        :returns:
            bool
        :description: QtSql/QSqlTableModel-select-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.selectRow
        :args:
            int
        :returns:
            bool
        :description: QtSql/QSqlTableModel-selectRow-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.selectStatement
        :returns:
            str
        :description: QtSql/QSqlTableModel-selectStatement-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.setData
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            Any
            role: int = :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.EditRole`
        :returns:
            bool
        :description: QtSql/QSqlTableModel-setData-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.setEditStrategy
        :args:
            :sip:ref:`~PyQt6.QtSql.QSqlTableModel.EditStrategy`
        :description: QtSql/QSqlTableModel-setEditStrategy-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.setFilter
        :args:
            str
        :description: QtSql/QSqlTableModel-setFilter-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.setPrimaryKey
        :args:
            :sip:ref:`~PyQt6.QtSql.QSqlIndex`
        :description: QtSql/QSqlTableModel-setPrimaryKey-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.setQuery
        :args:
            :sip:ref:`~PyQt6.QtSql.QSqlQuery`
        :description: QtSql/QSqlTableModel-setQuery-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.setRecord
        :args:
            int
            :sip:ref:`~PyQt6.QtSql.QSqlRecord`
        :returns:
            bool
        :description: QtSql/QSqlTableModel-setRecord-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.setSort
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.Qt.SortOrder`
        :description: QtSql/QSqlTableModel-setSort-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.setTable
        :args:
            str
        :description: QtSql/QSqlTableModel-setTable-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.sort
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.Qt.SortOrder`
        :description: QtSql/QSqlTableModel-sort-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.submit
        :returns:
            bool
        :description: QtSql/QSqlTableModel-submit-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.submitAll
        :returns:
            bool
        :description: QtSql/QSqlTableModel-submitAll-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.tableName
        :returns:
            str
        :description: QtSql/QSqlTableModel-tableName-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlTableModel.updateRowInTable
        :args:
            int
            :sip:ref:`~PyQt6.QtSql.QSqlRecord`
        :returns:
            bool
        :description: QtSql/QSqlTableModel-updateRowInTable-f.rst

    .. sip:signal:: PyQt6.QtSql.QSqlTableModel.beforeDelete
        :args:
            int
        :description: QtSql/QSqlTableModel-beforeDelete-s.rst

    .. sip:signal:: PyQt6.QtSql.QSqlTableModel.beforeInsert
        :args:
            :sip:ref:`~PyQt6.QtSql.QSqlRecord`
        :description: QtSql/QSqlTableModel-beforeInsert-s.rst

    .. sip:signal:: PyQt6.QtSql.QSqlTableModel.beforeUpdate
        :args:
            int
            :sip:ref:`~PyQt6.QtSql.QSqlRecord`
        :description: QtSql/QSqlTableModel-beforeUpdate-s.rst

    .. sip:signal:: PyQt6.QtSql.QSqlTableModel.primeInsert
        :args:
            int
            :sip:ref:`~PyQt6.QtSql.QSqlRecord`
        :description: QtSql/QSqlTableModel-primeInsert-s.rst
