.. sip:method-description::
    :status: todo
    :pysig: c520bd063dfa9328e959ab7dfba9d621
    :realsig: (const QString&,const QString&)
    :digest: b53278591676f389abe480e535faec10

Adds a database to the list of database connections using the driver *type* and the connection name *connectionName*. If there already exists a database connection called *connectionName*, that connection is removed.

The database connection is referred to by *connectionName*. The newly added database connection is returned.

If *type* is not available or could not be loaded, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.isValid` returns ``false``.

If *connectionName* is not specified, the new connection becomes the default connection for the application, and subsequent calls to :sip:ref:`~PyQt6.QtSql.QSqlDatabase.database` without the connection name argument will return the default connection. If a *connectionName* is provided here, use database(\ *connectionName*) to retrieve the connection.

**Warning:** If you add a connection with the same name as an existing connection, the new connection replaces the old one. If you call this function more than once without specifying *connectionName*, the default connection will be the one replaced.

Before using the connection, it must be initialized. e.g., call some or all of :sip:ref:`~PyQt6.QtSql.QSqlDatabase.setDatabaseName`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.setUserName`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.setPassword`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.setHostName`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.setPort`, and :sip:ref:`~PyQt6.QtSql.QSqlDatabase.setConnectOptions`, and, finally, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.open`.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlDatabase.database`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.removeDatabase`.
