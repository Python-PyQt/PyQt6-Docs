.. sip:method-description::
    :status: todo
    :pysig: 4316489c6107eb8c9163ab5b74c92f33
    :realsig: (const QString&) const
    :digest: 44a11425053e9818e0cc44ad3fba45b4

Executes a SQL statement on the database and returns a :sip:ref:`~PyQt6.QtSql.QSqlQuery` object. Use :sip:ref:`~PyQt6.QtSql.QSqlDatabase.lastError` to retrieve error information. If *query* is empty, an empty, invalid query is returned and :sip:ref:`~PyQt6.QtSql.QSqlDatabase.lastError` is not affected.

Use :sip:ref:`~PyQt6.QtSql.QSqlQuery.exec` instead.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlQuery`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.lastError`.
