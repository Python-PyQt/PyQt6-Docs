.. sip:method-description::
    :status: todo
    :pysig: 775d58fda33845881d451edad2caf0b5
    :realsig: (const QString&, const QString&)
    :digest: b19e93bb16b1e30fddeabd05183bd784

Clones the database connection *other* and stores it as *connectionName*. All the settings from the original database, e.g. :sip:ref:`~PyQt6.QtSql.QSqlDatabase.databaseName`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.hostName`, etc., are copied across. Does nothing if *other* is an invalid database. Returns the newly created database connection.

**Note:** The new connection has not been opened. Before using the new connection, you must call :sip:ref:`~PyQt6.QtSql.QSqlDatabase.open`.

This overload is useful when cloning the database in another thread to the one that is used by the database represented by *other*.
