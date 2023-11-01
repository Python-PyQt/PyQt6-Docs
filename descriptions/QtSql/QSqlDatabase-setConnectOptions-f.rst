.. sip:method-description::
    :status: todo
    :pysig: 930c02c5381eddceb4765781e6c6366f
    :realsig: (const QString&)
    :digest: 563d6e97bfdfb936e56d093c5ba3898a

Sets database-specific *options*. This must be done before the connection is opened, otherwise it has no effect. Another possibility is to close the connection, call QSqlDatabase::setConnectOptions(), and :sip:ref:`~PyQt6.QtSql.QSqlDatabase.open` the connection again.

The format of the *options* string is a semicolon separated list of option names or option=value pairs. The options depend on the database client used and are described for each plugin in the `SQL Database Drivers <https://doc.qt.io/qt-6/sql-driver.html>`_ page.

Examples:

.. literalinclude:: ../../../snippets/qtbase-src-sql-doc-snippets-code-src_sql_kernel_qsqldatabase.py
    :lines: 100-119

Refer to the client library documentation for more information about the different options.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlDatabase.connectOptions`.
