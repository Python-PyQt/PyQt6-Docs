.. sip:method-description::
    :status: todo
    :pysig: 1ab98a4411fb7d10d5134d664f82b37e
    :realsig: (const QString&)
    :digest: 8a27ef60dc3d5e7000c14d7ba82382d9

Prepares the SQL query *query* for execution. Returns ``true`` if the query is prepared successfully; otherwise returns ``false``.

The query may contain placeholders for binding values. Both Oracle style colon-name (e.g., ``:surname``), and ODBC style (``?``) placeholders are supported; but they cannot be mixed in the same query. See the :ref:`Detailed Description<qsqlquery-qsqlquery-examples>` for examples.

Portability notes: Some databases choose to delay preparing a query until it is executed the first time. In this case, preparing a syntactically wrong query succeeds, but every consecutive :sip:ref:`~PyQt6.QtSql.QSqlQuery.exec` will fail. When the database does not support named placeholders directly, the placeholder can only contain characters in the range [a-zA-Z0-9_].

For SQLite, the query string can contain only one statement at a time. If more than one statement is given, the function returns ``false``.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-sql-doc-snippets-sqldatabase-sqldatabase.py
    :lines: 141-147

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlQuery.exec`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.bindValue`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.addBindValue`.
