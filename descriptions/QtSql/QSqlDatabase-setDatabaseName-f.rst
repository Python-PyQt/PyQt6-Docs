.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: 02192dc1a5c2a1cce327dce6fd0bb3cb

Sets the connection's database name to *name*. To have effect, the database name must be set *before* the connection is :sip:ref:`~PyQt6.QtSql.QSqlDatabase.open`. Alternatively, you can :sip:ref:`~PyQt6.QtSql.QSqlDatabase.close` the connection, set the database name, and call :sip:ref:`~PyQt6.QtSql.QSqlDatabase.open` again.

**Note:** The *database name* is not the *connection name*. The connection name must be passed to :sip:ref:`~PyQt6.QtSql.QSqlDatabase.addDatabase` at connection object create time.

For the QSQLITE driver, if the database name specified does not exist, then it will create the file for you unless the QSQLITE_OPEN_READONLY option is set.

Additionally, *name* can be set to ``":memory:"`` which will create a temporary database which is only available for the lifetime of the application.

For the QOCI (Oracle) driver, the database name is the TNS Service Name.

For the QODBC driver, the *name* can either be a DSN, a DSN filename (in which case the file must have a ``.dsn`` extension), or a connection string.

For example, Microsoft Access users can use the following connection string to open an ``.mdb`` file directly, instead of having to create a DSN entry in the ODBC manager:

.. literalinclude:: ../../../snippets/qtbase-src-sql-doc-snippets-code-src_sql_kernel_qsqldatabase.py
    :lines: 84-90

There is no default value.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlDatabase.databaseName`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.setUserName`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.setPassword`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.setHostName`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.setPort`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.setConnectOptions`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.open`.
