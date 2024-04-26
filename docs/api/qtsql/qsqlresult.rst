:orphan:

.. sip:class:: PyQt6.QtSql.QSqlResult
    :description: QtSql/QSqlResult-c.rst

    .. sip:enum:: PyQt6.QtSql.QSqlResult.BindingSyntax
        :description: QtSql/QSqlResult-BindingSyntax-e.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlResult.BindingSyntax.NamedBinding
            :description: QtSql/QSqlResult-BindingSyntax-NamedBinding-v.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlResult.BindingSyntax.PositionalBinding
            :description: QtSql/QSqlResult-BindingSyntax-PositionalBinding-v.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.__init__
        :args:
            :sip:ref:`~PyQt6.QtSql.QSqlDriver`
        :description: QtSql/QSqlResult-__init__-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.addBindValue
        :args:
            Any
            :sip:ref:`~PyQt6.QtSql.QSql.ParamTypeFlag`
        :description: QtSql/QSqlResult-addBindValue-f-1.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.at
        :returns:
            int
        :description: QtSql/QSqlResult-at-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.bindingSyntax
        :returns:
            :sip:ref:`~PyQt6.QtSql.QSqlResult.BindingSyntax`
        :description: QtSql/QSqlResult-bindingSyntax-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.bindValue
        :args:
            int
            Any
            :sip:ref:`~PyQt6.QtSql.QSql.ParamTypeFlag`
        :description: QtSql/QSqlResult-bindValue-f-2.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.bindValue
        :args:
            Optional[str]
            Any
            :sip:ref:`~PyQt6.QtSql.QSql.ParamTypeFlag`
        :description: QtSql/QSqlResult-bindValue-f-4.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.bindValueType
        :args:
            Optional[str]
        :returns:
            :sip:ref:`~PyQt6.QtSql.QSql.ParamTypeFlag`
        :description: QtSql/QSqlResult-bindValueType-f-4.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.bindValueType
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtSql.QSql.ParamTypeFlag`
        :description: QtSql/QSqlResult-bindValueType-f-3.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.boundValue
        :args:
            Optional[str]
        :returns:
            Any
        :description: QtSql/QSqlResult-boundValue-f-2.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.boundValue
        :args:
            int
        :returns:
            Any
        :description: QtSql/QSqlResult-boundValue-f-1.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.boundValueCount
        :returns:
            int
        :description: QtSql/QSqlResult-boundValueCount-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.boundValueName
        :args:
            int
        :returns:
            str
        :description: QtSql/QSqlResult-boundValueName-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.boundValueNames
        :returns:
            List[str]
        :description: QtSql/QSqlResult-boundValueNames-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.boundValues
        :returns:
            List[Any]
        :description: QtSql/QSqlResult-boundValues-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.clear
        :description: QtSql/QSqlResult-clear-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.data
        :args:
            int
        :returns:
            Any
        :description: QtSql/QSqlResult-data-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.driver
        :returns:
            :sip:ref:`~PyQt6.QtSql.QSqlDriver`
        :description: QtSql/QSqlResult-driver-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.exec
        :returns:
            bool
        :description: QtSql/QSqlResult-exec-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.executedQuery
        :returns:
            str
        :description: QtSql/QSqlResult-executedQuery-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.fetch
        :args:
            int
        :returns:
            bool
        :description: QtSql/QSqlResult-fetch-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.fetchFirst
        :returns:
            bool
        :description: QtSql/QSqlResult-fetchFirst-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.fetchLast
        :returns:
            bool
        :description: QtSql/QSqlResult-fetchLast-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.fetchNext
        :returns:
            bool
        :description: QtSql/QSqlResult-fetchNext-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.fetchPrevious
        :returns:
            bool
        :description: QtSql/QSqlResult-fetchPrevious-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.handle
        :returns:
            Any
        :description: QtSql/QSqlResult-handle-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.hasOutValues
        :returns:
            bool
        :description: QtSql/QSqlResult-hasOutValues-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.isActive
        :returns:
            bool
        :description: QtSql/QSqlResult-isActive-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.isForwardOnly
        :returns:
            bool
        :description: QtSql/QSqlResult-isForwardOnly-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.isNull
        :args:
            int
        :returns:
            bool
        :description: QtSql/QSqlResult-isNull-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.isPositionalBindingEnabled
        :returns:
            bool
        :description: QtSql/QSqlResult-isPositionalBindingEnabled-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.isSelect
        :returns:
            bool
        :description: QtSql/QSqlResult-isSelect-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.isValid
        :returns:
            bool
        :description: QtSql/QSqlResult-isValid-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.lastError
        :returns:
            :sip:ref:`~PyQt6.QtSql.QSqlError`
        :description: QtSql/QSqlResult-lastError-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.lastInsertId
        :returns:
            Any
        :description: QtSql/QSqlResult-lastInsertId-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.lastQuery
        :returns:
            str
        :description: QtSql/QSqlResult-lastQuery-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.numRowsAffected
        :returns:
            int
        :description: QtSql/QSqlResult-numRowsAffected-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.prepare
        :args:
            Optional[str]
        :returns:
            bool
        :description: QtSql/QSqlResult-prepare-f-1.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.record
        :returns:
            :sip:ref:`~PyQt6.QtSql.QSqlRecord`
        :description: QtSql/QSqlResult-record-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.reset
        :args:
            Optional[str]
        :returns:
            bool
        :description: QtSql/QSqlResult-reset-f-1.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.savePrepare
        :args:
            Optional[str]
        :returns:
            bool
        :description: QtSql/QSqlResult-savePrepare-f-1.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.setActive
        :args:
            bool
        :description: QtSql/QSqlResult-setActive-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.setAt
        :args:
            int
        :description: QtSql/QSqlResult-setAt-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.setForwardOnly
        :args:
            bool
        :description: QtSql/QSqlResult-setForwardOnly-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.setLastError
        :args:
            :sip:ref:`~PyQt6.QtSql.QSqlError`
        :description: QtSql/QSqlResult-setLastError-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.setPositionalBindingEnabled
        :args:
            bool
        :description: QtSql/QSqlResult-setPositionalBindingEnabled-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.setQuery
        :args:
            Optional[str]
        :description: QtSql/QSqlResult-setQuery-f-1.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.setSelect
        :args:
            bool
        :description: QtSql/QSqlResult-setSelect-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlResult.size
        :returns:
            int
        :description: QtSql/QSqlResult-size-f.rst
