.. sip:class-description::
    :status: todo
    :brief: Handles a connection to a database
    :digest: 85b3ff4c2facb6c5a877ef69b9e2a25d

The :sip:ref:`~PyQt6.QtSql.QSqlDatabase` class handles a connection to a database.

The :sip:ref:`~PyQt6.QtSql.QSqlDatabase` class provides an interface for accessing a database through a connection. An instance of :sip:ref:`~PyQt6.QtSql.QSqlDatabase` represents the connection. The connection provides access to the database via one of the `supported database drivers <https://doc.qt.io/qt-6/sql-driver.html#supported-databases>`_, which are derived from :sip:ref:`~PyQt6.QtSql.QSqlDriver`. Alternatively, you can subclass your own database driver from :sip:ref:`~PyQt6.QtSql.QSqlDriver`. See `How to Write Your Own Database Driver <https://doc.qt.io/qt-6/sql-driver.html#how-to-write-your-own-database-driver>`_ for more information. A :sip:ref:`~PyQt6.QtSql.QSqlDatabase` instance must only be accessed by the thread it was created in. Therefore you have to make sure to create them in the correct context. Alternatively you can change the context with :sip:ref:`~PyQt6.QtSql.QSqlDatabase.moveToThread`.

Create a connection (i.e., an instance of :sip:ref:`~PyQt6.QtSql.QSqlDatabase`) by calling one of the static :sip:ref:`~PyQt6.QtSql.QSqlDatabase.addDatabase` functions, where you specify `the driver or type of driver <https://doc.qt.io/qt-6/sql-driver.html#supported-databases>`_ to use (depending on the type of database) and a connection name. A connection is known by its own name, *not* by the name of the database it connects to. You can have multiple connections to one database. :sip:ref:`~PyQt6.QtSql.QSqlDatabase` also supports the concept of a *default* connection, which is the unnamed connection. To create the default connection, don't pass the connection name argument when you call :sip:ref:`~PyQt6.QtSql.QSqlDatabase.addDatabase`. Subsequently, the default connection will be assumed if you call any static member function without specifying the connection name. The following snippet shows how to create and open a default connection to a PostgreSQL database:

.. literalinclude:: ../../../snippets/qtbase-src-sql-doc-snippets-sqldatabase-sqldatabase.py
    :lines: 63-68

Once the :sip:ref:`~PyQt6.QtSql.QSqlDatabase` object has been created, set the connection parameters with :sip:ref:`~PyQt6.QtSql.QSqlDatabase.setDatabaseName`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.setUserName`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.setPassword`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.setHostName`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.setPort`, and :sip:ref:`~PyQt6.QtSql.QSqlDatabase.setConnectOptions`. Then call :sip:ref:`~PyQt6.QtSql.QSqlDatabase.open` to activate the physical connection to the database. The connection is not usable until you open it.

The connection defined above will be the *default* connection, because we didn't give a connection name to :sip:ref:`~PyQt6.QtSql.QSqlDatabase.addDatabase`. Subsequently, you can get the default connection by calling :sip:ref:`~PyQt6.QtSql.QSqlDatabase.database` without the connection name argument:

.. literalinclude:: ../../../snippets/qtbase-src-sql-doc-snippets-sqldatabase-sqldatabase.py
    :lines: 75-75

:sip:ref:`~PyQt6.QtSql.QSqlDatabase` is a value class. Changes made to a database connection via one instance of :sip:ref:`~PyQt6.QtSql.QSqlDatabase` will affect other instances of :sip:ref:`~PyQt6.QtSql.QSqlDatabase` that represent the same connection. Use :sip:ref:`~PyQt6.QtSql.QSqlDatabase.cloneDatabase` to create an independent database connection based on an existing one.

**Warning:** It is highly recommended that you do not keep a copy of the :sip:ref:`~PyQt6.QtSql.QSqlDatabase` around as a member of a class, as this will prevent the instance from being correctly cleaned up on shutdown. If you need to access an existing :sip:ref:`~PyQt6.QtSql.QSqlDatabase`, it should be accessed with :sip:ref:`~PyQt6.QtSql.QSqlDatabase.database`. If you chose to have a :sip:ref:`~PyQt6.QtSql.QSqlDatabase` member variable, this needs to be deleted before the :sip:ref:`~PyQt6.QtCore.QCoreApplication` instance is deleted, otherwise it may lead to undefined behavior.

If you create multiple database connections, specify a unique connection name for each one, when you call :sip:ref:`~PyQt6.QtSql.QSqlDatabase.addDatabase`. Use :sip:ref:`~PyQt6.QtSql.QSqlDatabase.database` with a connection name to get that connection. Use :sip:ref:`~PyQt6.QtSql.QSqlDatabase.removeDatabase` with a connection name to remove a connection. :sip:ref:`~PyQt6.QtSql.QSqlDatabase` outputs a warning if you try to remove a connection referenced by other :sip:ref:`~PyQt6.QtSql.QSqlDatabase` objects. Use :sip:ref:`~PyQt6.QtSql.QSqlDatabase.contains` to see if a given connection name is in the list of connections.

+--------------------------------------------------------+-------------------------------------------------+
| Some utility methods:                                  |                                                 |
+========================================================+=================================================+
| :sip:ref:`~PyQt6.QtSql.QSqlDatabase.tables`            | returns the list of tables                      |
+--------------------------------------------------------+-------------------------------------------------+
| :sip:ref:`~PyQt6.QtSql.QSqlDatabase.primaryIndex`      | returns a table's primary index                 |
+--------------------------------------------------------+-------------------------------------------------+
| :sip:ref:`~PyQt6.QtSql.QSqlDatabase.record`            | returns meta-information about a table's fields |
+--------------------------------------------------------+-------------------------------------------------+
| :sip:ref:`~PyQt6.QtSql.QSqlDatabase.transaction`       | starts a transaction                            |
+--------------------------------------------------------+-------------------------------------------------+
| :sip:ref:`~PyQt6.QtSql.QSqlDatabase.commit`            | saves and completes a transaction               |
+--------------------------------------------------------+-------------------------------------------------+
| :sip:ref:`~PyQt6.QtSql.QSqlDatabase.rollback`          | cancels a transaction                           |
+--------------------------------------------------------+-------------------------------------------------+
| hasFeature()                                           | checks if a driver supports transactions        |
+--------------------------------------------------------+-------------------------------------------------+
| :sip:ref:`~PyQt6.QtSql.QSqlDatabase.lastError`         | returns information about the last error        |
+--------------------------------------------------------+-------------------------------------------------+
| :sip:ref:`~PyQt6.QtSql.QSqlDatabase.drivers`           | returns the names of the available SQL drivers  |
+--------------------------------------------------------+-------------------------------------------------+
| :sip:ref:`~PyQt6.QtSql.QSqlDatabase.isDriverAvailable` | checks if a particular driver is available      |
+--------------------------------------------------------+-------------------------------------------------+
| :sip:ref:`~PyQt6.QtSql.QSqlDatabase.registerSqlDriver` | registers a custom-made driver                  |
+--------------------------------------------------------+-------------------------------------------------+

**Note:** When using transactions, you must start the transaction before you create your query.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlDriver`, :sip:ref:`~PyQt6.QtSql.QSqlQuery`, `Qt SQL <https://doc.qt.io/qt-6/qtsql-index.html>`_.
