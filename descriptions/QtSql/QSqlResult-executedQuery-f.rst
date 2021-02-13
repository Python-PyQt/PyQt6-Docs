.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 1823a708b57dce645ef4fd093fd44133

Returns the query that was actually executed. This may differ from the query that was passed, for example if bound values were used with a prepared query and the underlying database doesn't support prepared queries.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlResult.exec`, :sip:ref:`~PyQt6.QtSql.QSqlResult.setQuery`.
