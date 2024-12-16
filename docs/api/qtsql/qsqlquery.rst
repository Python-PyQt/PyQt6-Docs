:orphan:

.. sip:class:: PyQt6.QtSql.QSqlQuery
    :description: QtSql/QSqlQuery-c.rst

    .. sip:enum:: PyQt6.QtSql.QSqlQuery.BatchExecutionMode
        :description: QtSql/QSqlQuery-BatchExecutionMode-e.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlQuery.BatchExecutionMode.ValuesAsColumns
            :description: QtSql/QSqlQuery-BatchExecutionMode-ValuesAsColumns-v.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlQuery.BatchExecutionMode.ValuesAsRows
            :description: QtSql/QSqlQuery-BatchExecutionMode-ValuesAsRows-v.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.__init__
        :args:
            :sip:ref:`~PyQt6.QtSql.QSqlDatabase`
        :description: QtSql/QSqlQuery-__init__-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.__init__
        :args:
            :sip:ref:`~PyQt6.QtSql.QSqlResult`
        :description: QtSql/QSqlQuery-__init__-f-1.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.__init__
        :args:
            :sip:ref:`~PyQt6.QtSql.QSqlQuery`
        :description: QtSql/QSqlQuery-__init__-f-2.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.__init__
        :args:
            query: Optional[str] = ''
            db: :sip:ref:`~PyQt6.QtSql.QSqlDatabase` = QSqlDatabase()
        :description: QtSql/QSqlQuery-__init__-f-4.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.addBindValue
        :args:
            Any
            type: :sip:ref:`~PyQt6.QtSql.QSql.ParamTypeFlag` = :sip:ref:`~PyQt6.QtSql.QSql.ParamTypeFlag.In`
        :description: QtSql/QSqlQuery-addBindValue-f-1.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.at
        :returns:
            int
        :description: QtSql/QSqlQuery-at-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.bindValue
        :args:
            Optional[str]
            Any
            type: :sip:ref:`~PyQt6.QtSql.QSql.ParamTypeFlag` = :sip:ref:`~PyQt6.QtSql.QSql.ParamTypeFlag.In`
        :description: QtSql/QSqlQuery-bindValue-f-4.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.bindValue
        :args:
            int
            Any
            type: :sip:ref:`~PyQt6.QtSql.QSql.ParamTypeFlag` = :sip:ref:`~PyQt6.QtSql.QSql.ParamTypeFlag.In`
        :description: QtSql/QSqlQuery-bindValue-f-3.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.boundValue
        :args:
            Optional[str]
        :returns:
            Any
        :description: QtSql/QSqlQuery-boundValue-f-2.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.boundValue
        :args:
            int
        :returns:
            Any
        :description: QtSql/QSqlQuery-boundValue-f-1.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.boundValueName
        :args:
            int
        :returns:
            str
        :description: QtSql/QSqlQuery-boundValueName-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.boundValueNames
        :returns:
            list[str]
        :description: QtSql/QSqlQuery-boundValueNames-f-1.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.boundValues
        :returns:
            list[Any]
        :description: QtSql/QSqlQuery-boundValues-f-1.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.clear
        :description: QtSql/QSqlQuery-clear-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.driver
        :returns:
            :sip:ref:`~PyQt6.QtSql.QSqlDriver`
        :description: QtSql/QSqlQuery-driver-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.exec
        :returns:
            bool
        :description: QtSql/QSqlQuery-exec-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.exec
        :args:
            Optional[str]
        :returns:
            bool
        :description: QtSql/QSqlQuery-exec-f-2.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.execBatch
        :args:
            mode: :sip:ref:`~PyQt6.QtSql.QSqlQuery.BatchExecutionMode` = :sip:ref:`~PyQt6.QtSql.QSqlQuery.BatchExecutionMode.ValuesAsRows`
        :returns:
            bool
        :description: QtSql/QSqlQuery-execBatch-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.executedQuery
        :returns:
            str
        :description: QtSql/QSqlQuery-executedQuery-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.finish
        :description: QtSql/QSqlQuery-finish-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.first
        :returns:
            bool
        :description: QtSql/QSqlQuery-first-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.isActive
        :returns:
            bool
        :description: QtSql/QSqlQuery-isActive-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.isForwardOnly
        :returns:
            bool
        :description: QtSql/QSqlQuery-isForwardOnly-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.isNull
        :args:
            int
        :returns:
            bool
        :description: QtSql/QSqlQuery-isNull-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.isNull
        :args:
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
        :returns:
            bool
        :description: QtSql/QSqlQuery-isNull-f-1.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.isPositionalBindingEnabled
        :returns:
            bool
        :description: QtSql/QSqlQuery-isPositionalBindingEnabled-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.isSelect
        :returns:
            bool
        :description: QtSql/QSqlQuery-isSelect-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.isValid
        :returns:
            bool
        :description: QtSql/QSqlQuery-isValid-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.last
        :returns:
            bool
        :description: QtSql/QSqlQuery-last-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.lastError
        :returns:
            :sip:ref:`~PyQt6.QtSql.QSqlError`
        :description: QtSql/QSqlQuery-lastError-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.lastInsertId
        :returns:
            Any
        :description: QtSql/QSqlQuery-lastInsertId-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.lastQuery
        :returns:
            str
        :description: QtSql/QSqlQuery-lastQuery-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.next
        :returns:
            bool
        :description: QtSql/QSqlQuery-next-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.nextResult
        :returns:
            bool
        :description: QtSql/QSqlQuery-nextResult-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.numericalPrecisionPolicy
        :returns:
            :sip:ref:`~PyQt6.QtSql.QSql.NumericalPrecisionPolicy`
        :description: QtSql/QSqlQuery-numericalPrecisionPolicy-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.numRowsAffected
        :returns:
            int
        :description: QtSql/QSqlQuery-numRowsAffected-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.prepare
        :args:
            Optional[str]
        :returns:
            bool
        :description: QtSql/QSqlQuery-prepare-f-1.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.previous
        :returns:
            bool
        :description: QtSql/QSqlQuery-previous-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.record
        :returns:
            :sip:ref:`~PyQt6.QtSql.QSqlRecord`
        :description: QtSql/QSqlQuery-record-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.result
        :returns:
            :sip:ref:`~PyQt6.QtSql.QSqlResult`
        :description: QtSql/QSqlQuery-result-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.seek
        :args:
            int
            relative: bool = False
        :returns:
            bool
        :description: QtSql/QSqlQuery-seek-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.setForwardOnly
        :args:
            bool
        :description: QtSql/QSqlQuery-setForwardOnly-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.setNumericalPrecisionPolicy
        :args:
            :sip:ref:`~PyQt6.QtSql.QSql.NumericalPrecisionPolicy`
        :description: QtSql/QSqlQuery-setNumericalPrecisionPolicy-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.setPositionalBindingEnabled
        :args:
            bool
        :description: QtSql/QSqlQuery-setPositionalBindingEnabled-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.size
        :returns:
            int
        :description: QtSql/QSqlQuery-size-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.swap
        :args:
            :sip:ref:`~PyQt6.QtSql.QSqlQuery`
        :description: QtSql/QSqlQuery-swap-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.value
        :args:
            int
        :returns:
            Any
        :description: QtSql/QSqlQuery-value-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlQuery.value
        :args:
            Union[Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview], Optional[str]]
        :returns:
            Any
        :description: QtSql/QSqlQuery-value-f-1.rst
