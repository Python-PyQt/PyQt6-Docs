.. sip:method-description::
    :status: todo
    :pysig: ee9355a52a69d0feaed1d2d1a5be1e56
    :realsig: () const
    :digest: 467bcdc5c37b6758d0ae4ffd2f1ddafa

Returns a :sip:ref:`~PyQt6.QtSql.QSqlRecord` containing the field information for the current query. If the query points to a valid row (\ :sip:ref:`~PyQt6.QtSql.QSqlQuery.isValid` returns true), the record is populated with the row's values. An empty record is returned when there is no active query (\ :sip:ref:`~PyQt6.QtSql.QSqlQuery.isActive` returns false).

To retrieve values from a query, :sip:ref:`~PyQt6.QtSql.QSqlQuery.value` should be used since its index-based lookup is faster.

In the following example, a ``SELECT \* FROM`` query is executed. Since the order of the columns is not defined, :sip:ref:`~PyQt6.QtSql.QSqlRecord.indexOf` is used to obtain the index of a column.

.. literalinclude:: ../../../snippets/qtbase-src-sql-doc-snippets-code-src_sql_kernel_qsqlquery.py
    :lines: 60-67

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlQuery.value`.
