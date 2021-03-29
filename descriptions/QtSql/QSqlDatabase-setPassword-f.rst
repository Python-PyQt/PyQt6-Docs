.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: 9a9cf248d9d077d54f29d0f6e41a7a6e

Sets the connection's password to *password*. To have effect, the password must be set *before* the connection is :sip:ref:`~PyQt6.QtSql.QSqlDatabase.open`. Alternatively, you can :sip:ref:`~PyQt6.QtSql.QSqlDatabase.close` the connection, set the password, and call :sip:ref:`~PyQt6.QtSql.QSqlDatabase.open` again.

There is no default value.

**Warning:** This function stores the password in plain text within Qt. Use the :sip:ref:`~PyQt6.QtSql.QSqlDatabase.open` call that takes a password as parameter to avoid this behavior.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlDatabase.password`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.setUserName`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.setDatabaseName`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.setHostName`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.setPort`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.setConnectOptions`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.open`.
