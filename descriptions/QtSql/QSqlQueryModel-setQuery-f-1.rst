.. sip:method-description::
    :status: todo
    :pysig: 6b7172ce47f777fc024cc31ea53776e1
    :realsig: (const QString&, const QSqlDatabase&)
    :digest: a0b8cb8de42aaf8d894f13e26fa42255

Executes the query *query* for the given database connection *db*. If no database (or an invalid database) is specified, the default connection is used.

:sip:ref:`~PyQt6.QtSql.QSqlQueryModel.lastError` can be used to retrieve verbose information if there was an error setting the query.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-sql-doc-snippets-code-src_sql_models_qsqlquerymodel.py
    :lines: 67-70

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlQueryModel.query`, :sip:ref:`~PyQt6.QtSql.QSqlQueryModel.queryChange`, :sip:ref:`~PyQt6.QtSql.QSqlQueryModel.lastError`.
