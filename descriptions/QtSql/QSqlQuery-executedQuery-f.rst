.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 7f1f9de6c0357bb1507fe7512e753a98

Returns the last query that was successfully executed.

In most cases this function returns the same string as :sip:ref:`~PyQt6.QtSql.QSqlQuery.lastQuery`. If a prepared query with placeholders is executed on a DBMS that does not support it, the preparation of this query is emulated. The placeholders in the original query are replaced with their bound values to form a new query. This function returns the modified query. It is mostly useful for debugging purposes.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlQuery.lastQuery`.
