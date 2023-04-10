.. sip:method-description::
    :status: todo
    :pysig: 930c02c5381eddceb4765781e6c6366f
    :realsig: (const QString&)
    :digest: 47bdf919941c8426676e37ce334febcf

Sets database-specific *options*. This must be done before the connection is opened, otherwise it has no effect. Another possibility is to close the connection, call QSqlDatabase::setConnectOptions(), and :sip:ref:`~PyQt6.QtSql.QSqlDatabase.open` the connection again.

The format of the *options* string is a semicolon separated list of option names or option=value pairs. The options depend on the database client used:

+-------------------------------+-----------------------------------------------------+-------------------+
| ODBC                          | MySQL                                               | PostgreSQL        |
+===============================+=====================================================+===================+
| * SQL_ATTR_ACCESS_MODE        | * CLIENT_COMPRESS                                   | * connect_timeout |
|                               |                                                     |                   |
| * SQL_ATTR_LOGIN_TIMEOUT      | * CLIENT_FOUND_ROWS                                 | * options         |
|                               |                                                     |                   |
| * SQL_ATTR_CONNECTION_TIMEOUT | * CLIENT_IGNORE_SPACE                               | * tty             |
|                               |                                                     |                   |
| * SQL_ATTR_CURRENT_CATALOG    | * CLIENT_ODBC                                       | * requiressl      |
|                               |                                                     |                   |
| * SQL_ATTR_METADATA_ID        | * CLIENT_NO_SCHEMA                                  | * service         |
|                               |                                                     |                   |
| * SQL_ATTR_PACKET_SIZE        | * CLIENT_INTERACTIVE                                |                   |
|                               |                                                     |                   |
| * SQL_ATTR_TRACEFILE          | * UNIX_SOCKET                                       |                   |
|                               |                                                     |                   |
| * SQL_ATTR_TRACE              | * MYSQL_OPT_RECONNECT                               |                   |
|                               |                                                     |                   |
| * SQL_ATTR_CONNECTION_POOLING | * MYSQL_OPT_CONNECT_TIMEOUT                         |                   |
|                               |                                                     |                   |
| * SQL_ATTR_ODBC_VERSION       | * MYSQL_OPT_READ_TIMEOUT                            |                   |
|                               |                                                     |                   |
|                               | * MYSQL_OPT_WRITE_TIMEOUT                           |                   |
|                               |                                                     |                   |
|                               | * MYSQL_OPT_LOCAL_INFILE                            |                   |
|                               |                                                     |                   |
|                               | * MYSQL_OPT_SSL_KEY                                 |                   |
|                               |                                                     |                   |
|                               | * MYSQL_OPT_SSL_CERT                                |                   |
|                               |                                                     |                   |
|                               | * MYSQL_OPT_SSL_CA                                  |                   |
|                               |                                                     |                   |
|                               | * MYSQL_OPT_SSL_CAPATH                              |                   |
|                               |                                                     |                   |
|                               | * MYSQL_OPT_SSL_CIPHER                              |                   |
|                               |                                                     |                   |
|                               | * MYSQL_OPT_SSL_CRL                                 |                   |
|                               |                                                     |                   |
|                               | * MYSQL_OPT_SSL_CRLPATH                             |                   |
|                               |                                                     |                   |
|                               | * SSL_KEY (deprecated, use MYSQL_OPT_SSL_KEY)       |                   |
|                               |                                                     |                   |
|                               | * SSL_CERT (deprecated, use MYSQL_OPT_SSL_CERT)     |                   |
|                               |                                                     |                   |
|                               | * SSL_CA (deprecated, use MYSQL_OPT_SSL_CA)         |                   |
|                               |                                                     |                   |
|                               | * SSL_CAPATH (deprecated, use MYSQL_OPT_SSL_CAPATH) |                   |
|                               |                                                     |                   |
|                               | * SSL_CIPHER (deprecated, use MYSQL_OPT_SSL_CIPHER) |                   |
+-------------------------------+-----------------------------------------------------+-------------------+

+--------------------------+----------------------------+
| DB2                      | OCI                        |
+==========================+============================+
| * SQL_ATTR_ACCESS_MODE   | * OCI_ATTR_PREFETCH_ROWS   |
|                          |                            |
| * SQL_ATTR_LOGIN_TIMEOUT | * OCI_ATTR_PREFETCH_MEMORY |
+--------------------------+----------------------------+

+----------------------------------------+-------------------------+
| SQLite                                 | Interbase               |
+========================================+=========================+
| * QSQLITE_BUSY_TIMEOUT                 | * ISC_DPB_LC_CTYPE      |
|                                        |                         |
| * QSQLITE_OPEN_READONLY                | * ISC_DPB_SQL_ROLE_NAME |
|                                        |                         |
| * QSQLITE_OPEN_URI                     |                         |
|                                        |                         |
| * QSQLITE_ENABLE_SHARED_CACHE          |                         |
|                                        |                         |
| * QSQLITE_ENABLE_REGEXP                |                         |
|                                        |                         |
| * QSQLITE_NO_USE_EXTENDED_RESULT_CODES |                         |
+----------------------------------------+-------------------------+

Examples:

.. literalinclude:: ../../../snippets/qtbase-src-sql-doc-snippets-code-src_sql_kernel_qsqldatabase.py
    :lines: 100-119

Refer to the client library documentation for more information about the different options.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlDatabase.connectOptions`.
