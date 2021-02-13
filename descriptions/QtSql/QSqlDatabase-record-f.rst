.. sip:method-description::
    :status: todo
    :pysig: fba1db770b3fd884298060b163b71369
    :realsig: (const QString&) const
    :digest: 5b489fba5104fe281a1bfcb8b6c0aa15

Returns a :sip:ref:`~PyQt6.QtSql.QSqlRecord` populated with the names of all the fields in the table (or view) called *tablename*. The order in which the fields appear in the record is undefined. If no such table (or view) exists, an empty record is returned.

**Note:** Some drivers, such as the `QPSQL <https://doc.qt.io/qt-6/sql-driver.html#qpsql-case-sensitivity>`_ driver, may may require you to pass *tablename* in lower case if the table was not quoted when created. See the `Qt SQL driver <https://doc.qt.io/qt-6/sql-driver.html>`_ documentation for more information.
