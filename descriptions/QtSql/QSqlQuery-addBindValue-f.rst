.. sip:method-description::
    :status: todo
    :pysig: 9513162aa75ec5852801a5c2d9c3eedb
    :realsig: (const QVariant&,QSql::ParamType)
    :digest: d26df053956b41c131218075cb57d8e2

Adds the value *val* to the list of values when using positional value binding. The order of the  calls determines which placeholder a value will be bound to in the prepared query. If *paramType* is :sip:ref:`~PyQt6.QtSql.QSql.ParamType.Out` or :sip:ref:`~PyQt6.QtSql.QSql.ParamType.InOut`, the placeholder will be overwritten with data from the database after the :sip:ref:`~PyQt6.QtSql.QSqlQuery.exec` call.

To bind a NULL value, use a null `QVariant <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_; for example, use ``QVariant(QMetaType::QString)`` if you are binding a string.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlQuery.bindValue`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.prepare`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.exec`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.boundValue`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.boundValues`.
