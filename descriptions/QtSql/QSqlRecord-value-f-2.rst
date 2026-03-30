.. sip:method-description::
    :status: todo
    :pysig: 06fe9deac4b7594c254afb27e78e7eca
    :realsig: (QAnyStringView) const
    :digest: faea8467bffc2655f3dcc048fa48caed

Returns the value of the field called *name* in the record. If field *name* does not exist an invalid variant is returned.

**Note:** In Qt versions prior to 6.8, this function took QString, not QAnyStringView.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlRecord.indexOf`, :sip:ref:`~PyQt6.QtSql.QSqlRecord.isNull`.
