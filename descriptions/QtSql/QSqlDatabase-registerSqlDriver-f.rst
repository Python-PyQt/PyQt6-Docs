.. sip:method-description::
    :status: todo
    :pysig: d0a02f58879e6be70f1e7af2f64a0762
    :realsig: (const QString&,QSqlDriverCreatorBase*)
    :digest: 98eb47810c1214524bb03e984c2dd9a8

This function registers a new SQL driver called *name*, within the SQL framework. This is useful if you have a custom SQL driver and don't want to compile it as a plugin.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-sql-doc-snippets-code-src_sql_kernel_qsqldatabase_snippet.py
    :lines: 54-57

:sip:ref:`~PyQt6.QtSql.QSqlDatabase` takes ownership of the *creator* pointer, so you mustn't delete it yourself.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlDatabase.drivers`.
