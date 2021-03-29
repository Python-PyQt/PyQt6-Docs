.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 3f35e6e725df65831e253323d65139e3

Closes the database connection, freeing any resources acquired, and invalidating any existing `QSqlQuery <https://doc.qt.io/qt-6/qtsql-changes-qt6.html#qsqlquery>`_ objects that are used with the database.

This will also affect copies of this :sip:ref:`~PyQt6.QtSql.QSqlDatabase` object.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlDatabase.removeDatabase`.
