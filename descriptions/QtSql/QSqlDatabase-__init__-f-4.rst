.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: a9da9249839c1ad7fdfe83804ab4e582

Creates a :sip:ref:`~PyQt6.QtSql.QSqlDatabase` connection that uses the driver referred to by *type*. If the *type* is not recognized, the database connection will have no functionality.

The currently available driver types are:

+-------------+---------------------------------------------+
| Driver Type | Description                                 |
+=============+=============================================+
| QDB2        | IBM DB2                                     |
+-------------+---------------------------------------------+
| QIBASE      | Borland InterBase Driver                    |
+-------------+---------------------------------------------+
| QMYSQL      | MySQL Driver                                |
+-------------+---------------------------------------------+
| QOCI        | Oracle Call Interface Driver                |
+-------------+---------------------------------------------+
| QODBC       | ODBC Driver (includes Microsoft SQL Server) |
+-------------+---------------------------------------------+
| QPSQL       | PostgreSQL Driver                           |
+-------------+---------------------------------------------+
| QSQLITE     | SQLite version 3 or above                   |
+-------------+---------------------------------------------+
| QMIMER      | Mimer SQL 11 or above                       |
+-------------+---------------------------------------------+

Additional third party drivers, including your own custom drivers, can be loaded dynamically.

.. seealso:: `SQL Database Drivers <https://doc.qt.io/qt-6/sql-driver.html>`_, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.registerSqlDriver`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.drivers`.
