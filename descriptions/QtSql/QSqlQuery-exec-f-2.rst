.. sip:method-description::
    :status: todo
    :pysig: 1ab98a4411fb7d10d5134d664f82b37e
    :realsig: (const QString&)
    :digest: b1107fc0557ac9d90dc138f13cc369ff

Executes the SQL in *query*. Returns ``true`` and sets the query state to :sip:ref:`~PyQt6.QtSql.QSqlQuery.isActive` if the query was successful; otherwise returns ``false``. The *query* string must use syntax appropriate for the SQL database being queried (for example, standard SQL).

After the query is executed, the query is positioned on an *invalid* record and must be navigated to a valid record before data values can be retrieved (for example, using :sip:ref:`~PyQt6.QtSql.QSqlQuery.next`).

Note that the last error for this query is reset when :sip:ref:`~PyQt6.QtSql.QSqlQuery.exec` is called.

For SQLite, the query string can contain only one statement at a time. If more than one statement is given, the function returns ``false``.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-sql-doc-snippets-sqldatabase-sqldatabase.py
    :lines: 340-342

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlQuery.isActive`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.isValid`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.next`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.previous`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.first`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.last`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.seek`.
