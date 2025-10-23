.. sip:method-description::
    :status: todo
    :pysig: 0f6fb60ef827df111b0651fef08e83ee
    :realsig: (QAnyStringView) const
    :digest: f03f9c4193b2f7a86a085ce662b76491

Returns the value of the field called *name* in the current record. If field *name* does not exist an invalid variant is returned.

This overload is less efficient than :sip:ref:`~PyQt6.QtSql.QSqlQuery.value`

**Note:** In Qt versions prior to 6.8, this function took QString, not QAnyStringView.
