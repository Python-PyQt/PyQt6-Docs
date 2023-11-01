.. sip:method-description::
    :status: todo
    :pysig: ebf9d6002723c0a9e7d254851a551853
    :realsig: (const QSqlDatabase&, const QString&)
    :digest: d2b4a1c4deba69eed40db97ab5d3ad82

Clones the database connection *other* and stores it as *connectionName*. All the settings from the original database, e.g. :sip:ref:`~PyQt6.QtSql.QSqlDatabase.databaseName`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.hostName`, etc., are copied across. Does nothing if *other* is an invalid database. Returns the newly created database connection.

**Note:** The new connection has not been opened. Before using the new connection, you must call :sip:ref:`~PyQt6.QtSql.QSqlDatabase.open`.
