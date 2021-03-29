.. sip:method-description::
    :status: todo
    :pysig: 866a819a6f3f8c6a9dbc69d89f487d95
    :realsig: (const QString&) const
    :digest: bd0925002d18c13bb2ff58f284967b75

Returns the primary index for table *tablename*. If no primary index exists, an empty :sip:ref:`~PyQt6.QtSql.QSqlIndex` is returned.

**Note:** Some drivers, such as the `QPSQL <https://doc.qt.io/qt-6/sql-driver.html#qpsql-case-sensitivity>`_ driver, may may require you to pass *tablename* in lower case if the table was not quoted when created. See the `Qt SQL driver <https://doc.qt.io/qt-6/sql-driver.html>`_ documentation for more information.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlDatabase.tables`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.record`.
