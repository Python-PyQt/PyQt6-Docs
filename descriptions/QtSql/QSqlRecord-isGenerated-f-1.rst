.. sip:method-description::
    :status: todo
    :pysig: 469c3d5de45760d2e753a158b05ea5cb
    :realsig: (QAnyStringView) const
    :digest: 416ac8d02ec76a881313058a0c980111

Returns ``true`` if the record has a field called *name* and this field is to be generated (the default); otherwise returns ``false``.

**Note:** In Qt versions prior to 6.8, this function took QString, not QAnyStringView.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlRecord.setGenerated`.
