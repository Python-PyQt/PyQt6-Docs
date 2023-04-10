.. sip:method-description::
    :status: todo
    :pysig: 860c3b285abf920f92feb9a465b24643
    :realsig: (const QVariant&,QSql::ParamType)
    :digest: 255e4c44625703168e11e231b5532266

Adds the value *val* to the list of values when using positional value binding. The order of the addBindValue() calls determines which placeholder a value will be bound to in the prepared query. If *paramType* is :sip:ref:`~PyQt6.QtSql.QSql.ParamType.Out` or :sip:ref:`~PyQt6.QtSql.QSql.ParamType.InOut`, the placeholder will be overwritten with data from the database after the :sip:ref:`~PyQt6.QtSql.QSqlQuery.exec` call.

To bind a NULL value, use a null :sip:ref:`~PyQt6.QtCore.QVariant`; for example, use ``QVariant(QMetaType::fromType<QString>())`` if you are binding a string.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlQuery.bindValue`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.prepare`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.exec`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.boundValue`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.boundValues`.
