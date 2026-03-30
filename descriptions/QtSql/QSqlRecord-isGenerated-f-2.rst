.. sip:method-description::
    :status: todo
    :pysig: 29cd72a210a37398779f60306fe01ac7
    :realsig: (QAnyStringView) const
    :digest: 416ac8d02ec76a881313058a0c980111

Returns ``true`` if the record has a field called *name* and this field is to be generated (the default); otherwise returns ``false``.

**Note:** In Qt versions prior to 6.8, this function took QString, not QAnyStringView.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlRecord.setGenerated`.
