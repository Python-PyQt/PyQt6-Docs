.. sip:method-description::
    :status: todo
    :pysig: c2435248c7dc5a666882a323b22b1429
    :realsig: (const QModelIndex&) const
    :digest: cf6a3c9c38d3fda8072be64b6fb4d753

Returns the index of the value in the database result set for the given *item* in the model.

The return value is identical to *item* if no columns or rows have been inserted, removed, or moved around.

Returns an invalid model index if *item* is out of bounds or if *item* does not point to a value in the result set.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlTableModel.indexInQuery`, :sip:ref:`~PyQt6.QtSql.QSqlQueryModel.insertColumns`, :sip:ref:`~PyQt6.QtSql.QSqlQueryModel.removeColumns`.
