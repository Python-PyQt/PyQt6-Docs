.. sip:method-description::
    :status: todo
    :pysig: 11fc3dda62331e301ed1f7355e6771b8
    :realsig: (const QString&, const QVariant&, QSql::ParamType)
    :digest: bd694b94e8a7eb42e5dea10359de2e03

Binds the value *val* of parameter type *paramType* to the *placeholder* name in the current record (row).

**Note:** Binding an undefined placeholder will result in undefined behavior.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlQuery.bindValue`.
