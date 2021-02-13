.. sip:method-description::
    :status: todo
    :pysig: aebfbedff1f8fdb249d58aab9ea70f51
    :realsig: (const QString&,QSqlDriver::IdentifierType) const
    :digest: 44f4ccc16402ed8120a84b24f651da09

Returns the *identifier* with the leading and trailing delimiters removed, *identifier* can either be a table name or field name, dependent on *type*. If *identifier* does not have leading and trailing delimiter characters, *identifier* is returned without modification.

Reimplement this function if you want to provide your own implementation in your :sip:ref:`~PyQt6.QtSql.QSqlDriver` subclass,

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlDriver.isIdentifierEscaped`.
