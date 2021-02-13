.. sip:method-description::
    :status: todo
    :pysig: edb3c45e5d6e0ecd4da9b4b877c5546f
    :realsig: (int) const
    :digest: 3fd1295cc5e4b77a251fd1e58de49f7e

Returns the record at *row* in the model.

If *row* is the index of a valid row, the record will be populated with values from that row.

If the model is not initialized, an empty record will be returned.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlRecord.isEmpty`.
