.. sip:method-description::
    :status: todo
    :pysig: 49cd6c4846645627c7c8750fdcfb2bfd
    :realsig: (const QString&)
    :digest: 7e41fb829df486bda9a3dab48f8a9080

Removes the database connection *connectionName* from the list of database connections.

**Warning:** There should be no open queries on the database connection when this function is called, otherwise a resource leak will occur.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-sql-doc-snippets-code-src_sql_kernel_qsqldatabase.py
    :lines: 60-65

The correct way to do it:

.. literalinclude:: ../../../snippets/qtbase-src-sql-doc-snippets-code-src_sql_kernel_qsqldatabase.py
    :lines: 72-77

To remove the default connection, which may have been created with a call to :sip:ref:`~PyQt6.QtSql.QSqlDatabase.addDatabase` not specifying a connection name, you can retrieve the default connection name by calling :sip:ref:`~PyQt6.QtSql.QSqlDatabase.connectionName` on the database returned by :sip:ref:`~PyQt6.QtSql.QSqlDatabase.database`. Note that if a default database hasn't been created an invalid database will be returned.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlDatabase.database`, :sip:ref:`~PyQt6.QtSql.QSqlDatabase.connectionName`.
