.. sip:method-description::
    :status: todo
    :pysig: d4e4feedb68d2ec2d77985b5a70b5661
    :realsig: (QAnyStringView) const
    :digest: 16ff466a04edec93a7489ec4365d5d82

Returns the position of the field called *name* within the record, or -1 if it cannot be found. Field names are not case-sensitive. If more than one field matches, the first one is returned.

**Note:** In Qt versions prior to 6.8, this function took QString, not QAnyStringView.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlRecord.fieldName`.
