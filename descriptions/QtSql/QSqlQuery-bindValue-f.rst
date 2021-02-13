.. sip:method-description::
    :status: todo
    :pysig: bd63d4942c857faa20b6d255ec3fed17
    :realsig: (const QString&,const QVariant&,QSql::ParamType)
    :digest: d986f610508d06e15cc880f1d8c62f58

Set the placeholder *placeholder* to be bound to value *val* in the prepared statement. Note that the placeholder mark (e.g ``:``) must be included when specifying the placeholder name. If *paramType* is :sip:ref:`~PyQt6.QtSql.QSql.ParamType.Out` or :sip:ref:`~PyQt6.QtSql.QSql.ParamType.InOut`, the placeholder will be overwritten with data from the database after the :sip:ref:`~PyQt6.QtSql.QSqlQuery.exec` call. In this case, sufficient space must be pre-allocated to store the result into.

To bind a NULL value, use a null `QVariant <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_; for example, use ``QVariant(QMetaType::QString)`` if you are binding a string.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlQuery.addBindValue`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.prepare`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.exec`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.boundValue`, :sip:ref:`~PyQt6.QtSql.QSqlQuery.boundValues`.
