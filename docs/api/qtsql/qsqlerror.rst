:orphan:

.. sip:class:: PyQt6.QtSql.QSqlError
    :description: QtSql/QSqlError-c.rst

    .. sip:enum:: PyQt6.QtSql.QSqlError.ErrorType
        :description: QtSql/QSqlError-ErrorType-e.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlError.ErrorType.ConnectionError
            :description: QtSql/QSqlError-ErrorType-ConnectionError-v.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlError.ErrorType.NoError
            :description: QtSql/QSqlError-ErrorType-NoError-v.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlError.ErrorType.StatementError
            :description: QtSql/QSqlError-ErrorType-StatementError-v.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlError.ErrorType.TransactionError
            :description: QtSql/QSqlError-ErrorType-TransactionError-v.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlError.ErrorType.UnknownError
            :description: QtSql/QSqlError-ErrorType-UnknownError-v.rst

    .. sip:method:: PyQt6.QtSql.QSqlError.__init__
        :args:
            :sip:ref:`~PyQt6.QtSql.QSqlError`
        :description: QtSql/QSqlError-__init__-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlError.__init__
        :args:
            driverText: Optional[str] = ''
            databaseText: Optional[str] = ''
            type: :sip:ref:`~PyQt6.QtSql.QSqlError.ErrorType` = :sip:ref:`~PyQt6.QtSql.QSqlError.ErrorType.NoError`
            errorCode: Optional[str] = ''
        :description: QtSql/QSqlError-__init__-f-2.rst

    .. sip:method:: PyQt6.QtSql.QSqlError.databaseText
        :returns:
            str
        :description: QtSql/QSqlError-databaseText-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlError.driverText
        :returns:
            str
        :description: QtSql/QSqlError-driverText-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlError.__eq__
        :args:
            :sip:ref:`~PyQt6.QtSql.QSqlError`
        :returns:
            bool
        :description: QtSql/QSqlError-__eq__-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlError.isValid
        :returns:
            bool
        :description: QtSql/QSqlError-isValid-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlError.nativeErrorCode
        :returns:
            str
        :description: QtSql/QSqlError-nativeErrorCode-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlError.__ne__
        :args:
            :sip:ref:`~PyQt6.QtSql.QSqlError`
        :returns:
            bool
        :description: QtSql/QSqlError-__ne__-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlError.swap
        :args:
            :sip:ref:`~PyQt6.QtSql.QSqlError`
        :description: QtSql/QSqlError-swap-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlError.text
        :returns:
            str
        :description: QtSql/QSqlError-text-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlError.type
        :returns:
            :sip:ref:`~PyQt6.QtSql.QSqlError.ErrorType`
        :description: QtSql/QSqlError-type-f.rst
