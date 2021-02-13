.. sip:method-description::
    :status: todo
    :pysig: 4316489c6107eb8c9163ab5b74c92f33
    :realsig: (const QString&) const
    :digest: 52e3a2b0b2334b76a412617895b2bb92

Executes a SQL statement on the database and returns a `QSqlQuery <https://doc.qt.io/qt-6/qtsql-changes-qt6.html#qsqlquery>`_ object. Use :sip:ref:`~PyQt6.QtSql.QSqlDatabase.lastError` to retrieve error information. If *query* is empty, an empty, invalid query is returned and :sip:ref:`~PyQt6.QtSql.QSqlDatabase.lastError` is not affected.

.. seealso:: `QSqlQuery <https://doc.qt.io/qt-6/qtsql-changes-qt6.html#qsqlquery>`_, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.lastError`.
