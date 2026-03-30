.. sip:method-description::
    :status: todo
    :pysig: 16d47f3bd006fb027e504ae458c4049d
    :realsig: (const QString&, const QVariant&, QSql::ParamType)
    :digest: 1fe562ef74b70d0c02e26c0900f7e7be

Set the placeholder *placeholder* to be bound to value *val* in the prepared statement. Note that the placeholder mark (e.g ``:``) must be included when specifying the placeholder name. If *paramType* is :sip:ref:`~PyQt6.QtSql.QSql.ParamTypeFlag.Out` or :sip:ref:`~PyQt6.QtSql.QSql.ParamTypeFlag.InOut`, the placeholder will be overwritten with data from the database after the :sip:ref:`~PyQt6.QtSql.QSqlQuery.exec` call. In this case, sufficient space must be pre-allocated to store the result into.

To bind a NULL value, use a null :sip:ref:`~PyQt6.QtCore.QVariant`; for example, use ``QVariant(QMetaType::fromType<QString>())`` if you are binding a string.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlQuery.addBindValue`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.prepare`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.exec`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.boundValue`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.boundValues`.
