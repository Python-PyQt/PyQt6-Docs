:orphan:

.. sip:class:: PyQt6.QtSql.QSqlDriver
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtSql/QSqlDriver-c.rst

    .. sip:enum:: PyQt6.QtSql.QSqlDriver.DbmsType
        :description: QtSql/QSqlDriver-DbmsType-e.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlDriver.DbmsType.DB2
            :description: QtSql/QSqlDriver-DbmsType-DB2-v.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlDriver.DbmsType.Interbase
            :description: QtSql/QSqlDriver-DbmsType-Interbase-v.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlDriver.DbmsType.MSSqlServer
            :description: QtSql/QSqlDriver-DbmsType-MSSqlServer-v.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlDriver.DbmsType.MySqlServer
            :description: QtSql/QSqlDriver-DbmsType-MySqlServer-v.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlDriver.DbmsType.Oracle
            :description: QtSql/QSqlDriver-DbmsType-Oracle-v.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlDriver.DbmsType.PostgreSQL
            :description: QtSql/QSqlDriver-DbmsType-PostgreSQL-v.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlDriver.DbmsType.SQLite
            :description: QtSql/QSqlDriver-DbmsType-SQLite-v.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlDriver.DbmsType.Sybase
            :description: QtSql/QSqlDriver-DbmsType-Sybase-v.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlDriver.DbmsType.UnknownDbms
            :description: QtSql/QSqlDriver-DbmsType-UnknownDbms-v.rst

    .. sip:enum:: PyQt6.QtSql.QSqlDriver.DriverFeature
        :description: QtSql/QSqlDriver-DriverFeature-e.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlDriver.DriverFeature.BatchOperations
            :description: QtSql/QSqlDriver-DriverFeature-BatchOperations-v.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlDriver.DriverFeature.BLOB
            :description: QtSql/QSqlDriver-DriverFeature-BLOB-v.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlDriver.DriverFeature.EventNotifications
            :description: QtSql/QSqlDriver-DriverFeature-EventNotifications-v.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlDriver.DriverFeature.FinishQuery
            :description: QtSql/QSqlDriver-DriverFeature-FinishQuery-v.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlDriver.DriverFeature.LastInsertId
            :description: QtSql/QSqlDriver-DriverFeature-LastInsertId-v.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlDriver.DriverFeature.LowPrecisionNumbers
            :description: QtSql/QSqlDriver-DriverFeature-LowPrecisionNumbers-v.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlDriver.DriverFeature.MultipleResultSets
            :description: QtSql/QSqlDriver-DriverFeature-MultipleResultSets-v.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlDriver.DriverFeature.NamedPlaceholders
            :description: QtSql/QSqlDriver-DriverFeature-NamedPlaceholders-v.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlDriver.DriverFeature.PositionalPlaceholders
            :description: QtSql/QSqlDriver-DriverFeature-PositionalPlaceholders-v.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlDriver.DriverFeature.PreparedQueries
            :description: QtSql/QSqlDriver-DriverFeature-PreparedQueries-v.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlDriver.DriverFeature.QuerySize
            :description: QtSql/QSqlDriver-DriverFeature-QuerySize-v.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlDriver.DriverFeature.SimpleLocking
            :description: QtSql/QSqlDriver-DriverFeature-SimpleLocking-v.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlDriver.DriverFeature.Transactions
            :description: QtSql/QSqlDriver-DriverFeature-Transactions-v.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlDriver.DriverFeature.Unicode
            :description: QtSql/QSqlDriver-DriverFeature-Unicode-v.rst

    .. sip:enum:: PyQt6.QtSql.QSqlDriver.IdentifierType
        :description: QtSql/QSqlDriver-IdentifierType-e.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlDriver.IdentifierType.FieldName
            :description: QtSql/QSqlDriver-IdentifierType-FieldName-v.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlDriver.IdentifierType.TableName
            :description: QtSql/QSqlDriver-IdentifierType-TableName-v.rst

    .. sip:enum:: PyQt6.QtSql.QSqlDriver.NotificationSource
        :description: QtSql/QSqlDriver-NotificationSource-e.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlDriver.NotificationSource.OtherSource
            :description: QtSql/QSqlDriver-NotificationSource-OtherSource-v.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlDriver.NotificationSource.SelfSource
            :description: QtSql/QSqlDriver-NotificationSource-SelfSource-v.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlDriver.NotificationSource.UnknownSource
            :description: QtSql/QSqlDriver-NotificationSource-UnknownSource-v.rst

    .. sip:enum:: PyQt6.QtSql.QSqlDriver.StatementType
        :description: QtSql/QSqlDriver-StatementType-e.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlDriver.StatementType.DeleteStatement
            :description: QtSql/QSqlDriver-StatementType-DeleteStatement-v.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlDriver.StatementType.InsertStatement
            :description: QtSql/QSqlDriver-StatementType-InsertStatement-v.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlDriver.StatementType.SelectStatement
            :description: QtSql/QSqlDriver-StatementType-SelectStatement-v.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlDriver.StatementType.UpdateStatement
            :description: QtSql/QSqlDriver-StatementType-UpdateStatement-v.rst

        .. sip:enum-member:: PyQt6.QtSql.QSqlDriver.StatementType.WhereStatement
            :description: QtSql/QSqlDriver-StatementType-WhereStatement-v.rst

    .. sip:method:: PyQt6.QtSql.QSqlDriver.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtSql/QSqlDriver-__init__-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDriver.beginTransaction
        :returns:
            bool
        :description: QtSql/QSqlDriver-beginTransaction-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDriver.close
        :description: QtSql/QSqlDriver-close-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDriver.commitTransaction
        :returns:
            bool
        :description: QtSql/QSqlDriver-commitTransaction-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDriver.createResult
        :returns:
            :sip:ref:`~PyQt6.QtSql.QSqlResult`
        :description: QtSql/QSqlDriver-createResult-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDriver.dbmsType
        :returns:
            :sip:ref:`~PyQt6.QtSql.QSqlDriver.DbmsType`
        :description: QtSql/QSqlDriver-dbmsType-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDriver.escapeIdentifier
        :args:
            str
            :sip:ref:`~PyQt6.QtSql.QSqlDriver.IdentifierType`
        :returns:
            str
        :description: QtSql/QSqlDriver-escapeIdentifier-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDriver.formatValue
        :args:
            :sip:ref:`~PyQt6.QtSql.QSqlField`
            trimStrings: bool = False
        :returns:
            str
        :description: QtSql/QSqlDriver-formatValue-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDriver.handle
        :returns:
            Any
        :description: QtSql/QSqlDriver-handle-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDriver.hasFeature
        :args:
            :sip:ref:`~PyQt6.QtSql.QSqlDriver.DriverFeature`
        :returns:
            bool
        :description: QtSql/QSqlDriver-hasFeature-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDriver.isIdentifierEscaped
        :args:
            str
            :sip:ref:`~PyQt6.QtSql.QSqlDriver.IdentifierType`
        :returns:
            bool
        :description: QtSql/QSqlDriver-isIdentifierEscaped-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDriver.isOpen
        :returns:
            bool
        :description: QtSql/QSqlDriver-isOpen-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDriver.isOpenError
        :returns:
            bool
        :description: QtSql/QSqlDriver-isOpenError-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDriver.lastError
        :returns:
            :sip:ref:`~PyQt6.QtSql.QSqlError`
        :description: QtSql/QSqlDriver-lastError-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDriver.maximumIdentifierLength
        :args:
            :sip:ref:`~PyQt6.QtSql.QSqlDriver.IdentifierType`
        :returns:
            int
        :description: QtSql/QSqlDriver-maximumIdentifierLength-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDriver.numericalPrecisionPolicy
        :returns:
            :sip:ref:`~PyQt6.QtSql.QSql.NumericalPrecisionPolicy`
        :description: QtSql/QSqlDriver-numericalPrecisionPolicy-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDriver.open
        :args:
            str
            user: str = ''
            password: str = ''
            host: str = ''
            port: int = -1
            options: str = ''
        :returns:
            bool
        :description: QtSql/QSqlDriver-open-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDriver.primaryIndex
        :args:
            str
        :returns:
            :sip:ref:`~PyQt6.QtSql.QSqlIndex`
        :description: QtSql/QSqlDriver-primaryIndex-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDriver.record
        :args:
            str
        :returns:
            :sip:ref:`~PyQt6.QtSql.QSqlRecord`
        :description: QtSql/QSqlDriver-record-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDriver.rollbackTransaction
        :returns:
            bool
        :description: QtSql/QSqlDriver-rollbackTransaction-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDriver.setLastError
        :args:
            :sip:ref:`~PyQt6.QtSql.QSqlError`
        :description: QtSql/QSqlDriver-setLastError-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDriver.setNumericalPrecisionPolicy
        :args:
            :sip:ref:`~PyQt6.QtSql.QSql.NumericalPrecisionPolicy`
        :description: QtSql/QSqlDriver-setNumericalPrecisionPolicy-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDriver.setOpen
        :args:
            bool
        :description: QtSql/QSqlDriver-setOpen-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDriver.setOpenError
        :args:
            bool
        :description: QtSql/QSqlDriver-setOpenError-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDriver.sqlStatement
        :args:
            :sip:ref:`~PyQt6.QtSql.QSqlDriver.StatementType`
            str
            :sip:ref:`~PyQt6.QtSql.QSqlRecord`
            bool
        :returns:
            str
        :description: QtSql/QSqlDriver-sqlStatement-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDriver.stripDelimiters
        :args:
            str
            :sip:ref:`~PyQt6.QtSql.QSqlDriver.IdentifierType`
        :returns:
            str
        :description: QtSql/QSqlDriver-stripDelimiters-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDriver.subscribedToNotifications
        :returns:
            List[str]
        :description: QtSql/QSqlDriver-subscribedToNotifications-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDriver.subscribeToNotification
        :args:
            str
        :returns:
            bool
        :description: QtSql/QSqlDriver-subscribeToNotification-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDriver.tables
        :args:
            :sip:ref:`~PyQt6.QtSql.QSql.TableType`
        :returns:
            List[str]
        :description: QtSql/QSqlDriver-tables-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDriver.unsubscribeFromNotification
        :args:
            str
        :returns:
            bool
        :description: QtSql/QSqlDriver-unsubscribeFromNotification-f.rst

    .. sip:signal:: PyQt6.QtSql.QSqlDriver.notification
        :args:
            str
            :sip:ref:`~PyQt6.QtSql.QSqlDriver.NotificationSource`
            Any
        :description: QtSql/QSqlDriver-notification-s.rst
