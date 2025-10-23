.. sip:method-description::
    :status: todo
    :pysig: 469c3d5de45760d2e753a158b05ea5cb
    :realsig: (QAnyStringView) const
    :digest: 34b495e42425db20debd721739479545

Returns ``true`` if there is no field with this *name*; otherwise returns :sip:ref:`~PyQt6.QtSql.QSqlQuery.isNull`\ (int index) for the corresponding field index.

This overload is less efficient than :sip:ref:`~PyQt6.QtSql.QSqlQuery.isNull`

**Note:** In Qt versions prior to 6.8, this function took QString, not QAnyStringView.
