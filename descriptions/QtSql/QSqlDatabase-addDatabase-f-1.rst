.. sip:method-description::
    :status: todo
    :pysig: ff39a9d51b85425010207dfd9c26154b
    :realsig: (QSqlDriver*,const QString&)
    :digest: 1fc3fe2349a26a4de4d15557e7c7c302

This overload is useful when you want to create a database connection with a :sip:ref:`~PyQt6.QtSql.QSqlDriver` you instantiated yourself. It might be your own database driver, or you might just need to instantiate one of the Qt drivers yourself. If you do this, it is recommended that you include the driver code in your application. For example, you can create a PostgreSQL connection with your own QPSQL driver like this:

.. literalinclude:: ../../../snippets/qtbase-src-sql-doc-snippets-code-src_sql_kernel_qsqldatabase_snippet.py
    :lines: 60-64

The above code sets up a PostgreSQL connection and instantiates a QPSQLDriver object. Next, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.addDatabase` is called to add the connection to the known connections so that it can be used by the Qt SQL classes. When a driver is instantiated with a connection handle (or set of handles), Qt assumes that you have already opened the database connection.

**Note:** We assume that ``qtdir`` is the directory where Qt is installed. This will pull in the code that is needed to use the PostgreSQL client library and to instantiate a QPSQLDriver object, assuming that you have the PostgreSQL headers somewhere in your include search path.

Remember that you must link your application against the database client library. Make sure the client library is in your linker's search path, and add lines like these to your ``.pro`` file:

.. literalinclude:: ../../../snippets/qtbase-src-sql-doc-snippets-code-src_sql_kernel_qsqldatabase_snippet.py
    :lines: 68-69

The method described works for all the supplied drivers. The only difference will be in the driver constructor arguments. Here is a table of the drivers included with Qt, their source code files, and their constructor arguments:

+---------+---------------+--------------------------------------------------+---------------------+
| Driver  | Class name    | Constructor arguments                            | File to include     |
+=========+===============+==================================================+=====================+
| QPSQL   | QPSQLDriver   | PGconn \*connection                              | ``qsql_psql.cpp``   |
+---------+---------------+--------------------------------------------------+---------------------+
| QMYSQL  | QMYSQLDriver  | MYSQL \*connection                               | ``qsql_mysql.cpp``  |
+---------+---------------+--------------------------------------------------+---------------------+
| QOCI    | QOCIDriver    | OCIEnv \*environment, OCISvcCtx \*serviceContext | ``qsql_oci.cpp``    |
+---------+---------------+--------------------------------------------------+---------------------+
| QODBC   | QODBCDriver   | SQLHANDLE environment, SQLHANDLE connection      | ``qsql_odbc.cpp``   |
+---------+---------------+--------------------------------------------------+---------------------+
| QDB2    | QDB2          | SQLHANDLE environment, SQLHANDLE connection      | ``qsql_db2.cpp``    |
+---------+---------------+--------------------------------------------------+---------------------+
| QSQLITE | QSQLiteDriver | sqlite \*connection                              | ``qsql_sqlite.cpp`` |
+---------+---------------+--------------------------------------------------+---------------------+
| QIBASE  | QIBaseDriver  | isc_db_handle connection                         | ``qsql_ibase.cpp``  |
+---------+---------------+--------------------------------------------------+---------------------+

**Warning:** Adding a database connection with the same connection name as an existing connection, causes the existing connection to be replaced by the new one.

**Warning:** The SQL framework takes ownership of the *driver*. It must not be deleted. To remove the connection, use :sip:ref:`~PyQt6.QtSql.QSqlDatabase.removeDatabase`.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlDatabase.drivers`.
