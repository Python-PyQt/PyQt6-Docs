.. sip:method-description::
    :status: todo
    :pysig: eee57cba5cb389e07ffc94c30d492eed
    :realsig: (const QString&, const QVariant&, QSql::ParamType)
    :digest: bd694b94e8a7eb42e5dea10359de2e03

Binds the value *val* of parameter type *paramType* to the *placeholder* name in the current record (row).

**Note:** Binding an undefined placeholder will result in undefined behavior.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlQuery.bindValue`.
