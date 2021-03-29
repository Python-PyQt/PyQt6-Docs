.. sip:class-description::
    :status: todo
    :brief: Abstract base class for accessing specific SQL databases
    :digest: 6588be2ca5c6b76c495f563797d78f26

The :sip:ref:`~PyQt6.QtSql.QSqlDriver` class is an abstract base class for accessing specific SQL databases.

This class should not be used directly. Use :sip:ref:`~PyQt6.QtSql.QSqlDatabase` instead.

If you want to create your own SQL drivers, you can subclass this class and reimplement its pure virtual functions and those virtual functions that you need. See `How to Write Your Own Database Driver <https://doc.qt.io/qt-6/sql-driver.html#how-to-write-your-own-database-driver>`_ for more information.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlDatabase`, :sip:ref:`~PyQt6.QtSql.QSqlResult`.
