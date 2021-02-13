.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: 2b5777478433de16bcb71a1b3d8f38e2

Sets the connection's host name to *host*. To have effect, the host name must be set *before* the connection is :sip:ref:`~PyQt6.QtSql.QSqlDatabase.open`. Alternatively, you can :sip:ref:`~PyQt6.QtSql.QSqlDatabase.close` the connection, set the host name, and call :sip:ref:`~PyQt6.QtSql.QSqlDatabase.open` again.

There is no default value.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlDatabase.hostName`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.setUserName`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.setPassword`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.setDatabaseName`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.setPort`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.setConnectOptions`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.open`.
