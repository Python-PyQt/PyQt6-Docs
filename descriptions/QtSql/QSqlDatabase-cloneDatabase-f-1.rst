.. sip:method-description::
    :status: todo
    :pysig: 14458cfdec914be5ae59f1f124d430f1
    :realsig: (const QString&,const QString&)
    :digest: ece363649177c8553cb7b5dd09f35719

This is an overloaded function.

Clones the database connection *other* and stores it as *connectionName*. All the settings from the original database, e.g. :sip:ref:`~PyQt6.QtSql.QSqlDatabase.databaseName`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.hostName`, etc., are copied across. Does nothing if *other* is an invalid database. Returns the newly created database connection.

**Note:** The new connection has not been opened. Before using the new connection, you must call :sip:ref:`~PyQt6.QtSql.QSqlDatabase.open`.

This overload is useful when cloning the database in another thread to the one that is used by the database represented by *other*.
