.. sip:method-description::
    :status: todo
    :pysig: edb3c45e5d6e0ecd4da9b4b877c5546f
    :realsig: (int) const
    :digest: 78a9f27f442d7fbcace7db84e6342538

Returns the record containing information about the fields of the current query. If *row* is the index of a valid row, the record will be populated with values from that row.

If the model is not initialized, an empty record will be returned.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlRecord.isEmpty`.
