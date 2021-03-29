.. sip:method-description::
    :status: todo
    :pysig: ed36a1ef76a59ee3f15180e0441188ad
    :realsig: (const QVariant&)
    :digest: cdbfe005b0a0fcd960c4713ba68d4f3f

Sets the value of the field to *value*. If the field is read-only (\ :sip:ref:`~PyQt6.QtSql.QSqlField.isReadOnly` returns ``true``), nothing happens.

If the data type of *value* differs from the field's current data type, an attempt is made to cast it to the proper type. This preserves the data type of the field in the case of assignment, e.g. a QString to an integer data type.

To set the value to NULL, use :sip:ref:`~PyQt6.QtSql.QSqlField.clear`.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlField.value`, :sip:ref:`~PyQt6.QtSql.QSqlField.isReadOnly`, :sip:ref:`~PyQt6.QtSql.QSqlField.defaultValue`.
