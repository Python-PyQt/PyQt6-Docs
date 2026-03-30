.. sip:method-description::
    :status: todo
    :pysig: 008b75715a90e080f14f77384b3a5a04
    :realsig: (const QString&, QSqlDriver::IdentifierType) const
    :digest: 5b421497bd89ba75d49dd288e8c3402f

Returns whether *identifier* is escaped according to the database rules. *identifier* can either be a table name or field name, dependent on *type*.

Reimplement this function if you want to provide your own implementation in your :sip:ref:`~PyQt6.QtSql.QSqlDriver` subclass,

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlDriver.stripDelimiters`, :sip:ref:`~PyQt6.QtSql.QSqlDriver.escapeIdentifier`.
