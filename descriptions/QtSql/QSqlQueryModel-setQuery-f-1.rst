.. sip:method-description::
    :status: todo
    :pysig: a593fd89e269888efa85281b3709c02a
    :realsig: (const QString&,const QSqlDatabase&)
    :digest: 382059f673164533c1ed17cbef2311c0

This is an overloaded function.

Executes the query *query* for the given database connection *db*. If no database (or an invalid database) is specified, the default connection is used.

:sip:ref:`~PyQt6.QtSql.QSqlQueryModel.lastError` can be used to retrieve verbose information if there was an error setting the query.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-sql-doc-snippets-code-src_sql_models_qsqlquerymodel.py
    :lines: 67-70

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlQueryModel.query`, :sip:ref:`~PyQt6.QtSql.QSqlQueryModel.queryChange`, :sip:ref:`~PyQt6.QtSql.QSqlQueryModel.lastError`.
