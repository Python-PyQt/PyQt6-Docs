:orphan:

.. sip:class:: PyQt6.QtSql.QSqlDatabase
    :description: QtSql/QSqlDatabase-c.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.__init__
        :description: QtSql/QSqlDatabase-__init__-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.__init__
        :args:
            :sip:ref:`~PyQt6.QtSql.QSqlDatabase`
        :description: QtSql/QSqlDatabase-__init__-f-1.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.__init__
        :args:
            str
        :description: QtSql/QSqlDatabase-__init__-f-2.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.__init__
        :args:
            :sip:ref:`~PyQt6.QtSql.QSqlDriver`
        :description: QtSql/QSqlDatabase-__init__-f-3.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.addDatabase
        :args:
            str
            connectionName: str = ''
        :returns:
            :sip:ref:`~PyQt6.QtSql.QSqlDatabase`
        :static:
        :description: QtSql/QSqlDatabase-addDatabase-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.addDatabase
        :args:
            :sip:ref:`~PyQt6.QtSql.QSqlDriver`
            connectionName: str = ''
        :returns:
            :sip:ref:`~PyQt6.QtSql.QSqlDatabase`
        :static:
        :description: QtSql/QSqlDatabase-addDatabase-f-1.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.cloneDatabase
        :args:
            :sip:ref:`~PyQt6.QtSql.QSqlDatabase`
            str
        :returns:
            :sip:ref:`~PyQt6.QtSql.QSqlDatabase`
        :static:
        :description: QtSql/QSqlDatabase-cloneDatabase-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.cloneDatabase
        :args:
            str
            str
        :returns:
            :sip:ref:`~PyQt6.QtSql.QSqlDatabase`
        :static:
        :description: QtSql/QSqlDatabase-cloneDatabase-f-1.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.close
        :description: QtSql/QSqlDatabase-close-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.commit
        :returns:
            bool
        :description: QtSql/QSqlDatabase-commit-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.connectionName
        :returns:
            str
        :description: QtSql/QSqlDatabase-connectionName-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.connectionNames
        :returns:
            List[str]
        :static:
        :description: QtSql/QSqlDatabase-connectionNames-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.connectOptions
        :returns:
            str
        :description: QtSql/QSqlDatabase-connectOptions-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.contains
        :args:
            connectionName: str = ''
        :returns:
            bool
        :static:
        :description: QtSql/QSqlDatabase-contains-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.database
        :args:
            connectionName: str = ''
            open: bool = True
        :returns:
            :sip:ref:`~PyQt6.QtSql.QSqlDatabase`
        :static:
        :description: QtSql/QSqlDatabase-database-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.databaseName
        :returns:
            str
        :description: QtSql/QSqlDatabase-databaseName-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.driver
        :returns:
            :sip:ref:`~PyQt6.QtSql.QSqlDriver`
        :description: QtSql/QSqlDatabase-driver-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.driverName
        :returns:
            str
        :description: QtSql/QSqlDatabase-driverName-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.drivers
        :returns:
            List[str]
        :static:
        :description: QtSql/QSqlDatabase-drivers-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.exec
        :args:
            query: str = ''
        :returns:
            :sip:ref:`~PyQt6.QtSql.QSqlQuery`
        :description: QtSql/QSqlDatabase-exec-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.hostName
        :returns:
            str
        :description: QtSql/QSqlDatabase-hostName-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.isDriverAvailable
        :args:
            str
        :returns:
            bool
        :static:
        :description: QtSql/QSqlDatabase-isDriverAvailable-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.isOpen
        :returns:
            bool
        :description: QtSql/QSqlDatabase-isOpen-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.isOpenError
        :returns:
            bool
        :description: QtSql/QSqlDatabase-isOpenError-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.isValid
        :returns:
            bool
        :description: QtSql/QSqlDatabase-isValid-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.lastError
        :returns:
            :sip:ref:`~PyQt6.QtSql.QSqlError`
        :description: QtSql/QSqlDatabase-lastError-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.numericalPrecisionPolicy
        :returns:
            :sip:ref:`~PyQt6.QtSql.QSql.NumericalPrecisionPolicy`
        :description: QtSql/QSqlDatabase-numericalPrecisionPolicy-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.open
        :returns:
            bool
        :description: QtSql/QSqlDatabase-open-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.open
        :args:
            str
            str
        :returns:
            bool
        :description: QtSql/QSqlDatabase-open-f-1.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.password
        :returns:
            str
        :description: QtSql/QSqlDatabase-password-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.port
        :returns:
            int
        :description: QtSql/QSqlDatabase-port-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.primaryIndex
        :args:
            str
        :returns:
            :sip:ref:`~PyQt6.QtSql.QSqlIndex`
        :description: QtSql/QSqlDatabase-primaryIndex-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.record
        :args:
            str
        :returns:
            :sip:ref:`~PyQt6.QtSql.QSqlRecord`
        :description: QtSql/QSqlDatabase-record-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.registerSqlDriver
        :args:
            str
            :sip:ref:`~PyQt6.QtSql.QSqlDriverCreatorBase`
        :static:
        :description: QtSql/QSqlDatabase-registerSqlDriver-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.removeDatabase
        :args:
            str
        :static:
        :description: QtSql/QSqlDatabase-removeDatabase-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.rollback
        :returns:
            bool
        :description: QtSql/QSqlDatabase-rollback-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.setConnectOptions
        :args:
            options: str = ''
        :description: QtSql/QSqlDatabase-setConnectOptions-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.setDatabaseName
        :args:
            str
        :description: QtSql/QSqlDatabase-setDatabaseName-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.setHostName
        :args:
            str
        :description: QtSql/QSqlDatabase-setHostName-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.setNumericalPrecisionPolicy
        :args:
            :sip:ref:`~PyQt6.QtSql.QSql.NumericalPrecisionPolicy`
        :description: QtSql/QSqlDatabase-setNumericalPrecisionPolicy-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.setPassword
        :args:
            str
        :description: QtSql/QSqlDatabase-setPassword-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.setPort
        :args:
            int
        :description: QtSql/QSqlDatabase-setPort-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.setUserName
        :args:
            str
        :description: QtSql/QSqlDatabase-setUserName-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.tables
        :args:
            type: :sip:ref:`~PyQt6.QtSql.QSql.TableType` = :sip:ref:`~PyQt6.QtSql.QSql.TableType.Tables`
        :returns:
            List[str]
        :description: QtSql/QSqlDatabase-tables-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.transaction
        :returns:
            bool
        :description: QtSql/QSqlDatabase-transaction-f.rst

    .. sip:method:: PyQt6.QtSql.QSqlDatabase.userName
        :returns:
            str
        :description: QtSql/QSqlDatabase-userName-f.rst
