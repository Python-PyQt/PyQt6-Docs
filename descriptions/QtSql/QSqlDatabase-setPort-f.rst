.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: ddad2e0b3cacb0fa48c6ee155c1b8523

Sets the connection's port number to *port*. To have effect, the port number must be set *before* the connection is :sip:ref:`~PyQt6.QtSql.QSqlDatabase.open`. Alternatively, you can :sip:ref:`~PyQt6.QtSql.QSqlDatabase.close` the connection, set the port number, and call :sip:ref:`~PyQt6.QtSql.QSqlDatabase.open` again..

There is no default value.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlDatabase.port`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.setUserName`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.setPassword`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.setHostName`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.setDatabaseName`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.setConnectOptions`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.open`.
