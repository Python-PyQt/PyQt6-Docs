.. sip:method-description::
    :status: todo
    :pysig: 18a38c923401f2d3ae141c5195548375
    :realsig: (const QString&, bool)
    :digest: f02efc9546c073fdab358c1bccc70082

Returns the database connection called *connectionName*. The database connection must have been previously added with :sip:ref:`~PyQt6.QtSql.QSqlDatabase.addDatabase`. If *open* is true (the default) and the database connection is not already open it is opened now. If no *connectionName* is specified the default connection is used. If *connectionName* does not exist in the list of databases, an invalid connection is returned.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlDatabase.isOpen`.
