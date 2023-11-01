.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: 4b1db4f9eec234060609650139c6c0d1

Sets the connection's user name to *name*. To have effect, the user name must be set *before* the connection is :sip:ref:`~PyQt6.QtSql.QSqlDatabase.open`. Alternatively, you can :sip:ref:`~PyQt6.QtSql.QSqlDatabase.close` the connection, set the user name, and call :sip:ref:`~PyQt6.QtSql.QSqlDatabase.open` again.

There is no default value.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlDatabase.userName`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.setDatabaseName`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.setPassword`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.setHostName`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.setPort`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.setConnectOptions`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.open`.
