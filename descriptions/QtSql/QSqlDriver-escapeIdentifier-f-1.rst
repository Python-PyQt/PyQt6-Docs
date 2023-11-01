.. sip:method-description::
    :status: todo
    :pysig: 68ce74552395919a6d56830369c2e0c0
    :realsig: (const QString&, QSqlDriver::IdentifierType) const
    :digest: 7274f9ac4622441fb67ae361d2d07c7e

Returns the *identifier* escaped according to the database rules. *identifier* can either be a table name or field name, dependent on *type*.

The default implementation does nothing.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlDriver.isIdentifierEscaped`.
