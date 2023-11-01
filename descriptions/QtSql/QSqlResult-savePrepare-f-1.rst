.. sip:method-description::
    :status: todo
    :pysig: 1ab98a4411fb7d10d5134d664f82b37e
    :realsig: (const QString&)
    :digest: df865f06e1991af72641b57f1b1ab5fc

Prepares the given *query*, using the underlying database functionality where possible. Returns ``true`` if the query is prepared successfully; otherwise returns ``false``.

Note: This method should have been called "safePrepare()".

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlResult.prepare`.
