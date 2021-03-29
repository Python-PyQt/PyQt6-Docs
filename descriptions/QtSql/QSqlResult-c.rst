.. sip:class-description::
    :status: todo
    :brief: Abstract interface for accessing data from specific SQL databases
    :digest: 2501cf39bc9aea135b781b661a1b79f8

The :sip:ref:`~PyQt6.QtSql.QSqlResult` class provides an abstract interface for accessing data from specific SQL databases.

Normally, you would use `QSqlQuery <https://doc.qt.io/qt-6/qtsql-changes-qt6.html#qsqlquery>`_ instead of :sip:ref:`~PyQt6.QtSql.QSqlResult`, since `QSqlQuery <https://doc.qt.io/qt-6/qtsql-changes-qt6.html#qsqlquery>`_ provides a generic wrapper for database-specific implementations of :sip:ref:`~PyQt6.QtSql.QSqlResult`.

If you are implementing your own SQL driver (by subclassing :sip:ref:`~PyQt6.QtSql.QSqlDriver`), you will need to provide your own :sip:ref:`~PyQt6.QtSql.QSqlResult` subclass that implements all the pure virtual functions and other virtual functions that you need.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlDriver`.
