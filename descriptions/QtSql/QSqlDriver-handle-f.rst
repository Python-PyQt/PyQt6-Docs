.. sip:method-description::
    :status: todo
    :pysig: ed36a1ef76a59ee3f15180e0441188ad
    :realsig: () const
    :digest: 5b7696cf71092e869404a1ae43d5064e

Returns the low-level database handle wrapped in a :sip:ref:`~PyQt6.QtCore.QVariant` or an invalid variant if there is no handle.

**Warning:** Use this with uttermost care and only if you know what you're doing.

**Warning:** The handle returned here can become a stale pointer if the connection is modified (for example, if you close the connection).

**Warning:** The handle can be NULL if the connection is not open yet.

The handle returned here is database-dependent, you should query the type name of the variant before accessing it.

This example retrieves the handle for a connection to sqlite:

.. literalinclude:: ../../../snippets/qtbase-src-sql-doc-snippets-code-src_sql_kernel_qsqldriver.py
    :lines: 64-72

This snippet returns the handle for PostgreSQL or MySQL:

.. literalinclude:: ../../../snippets/qtbase-src-sql-doc-snippets-code-src_sql_kernel_qsqldriver.py
    :lines: 76-88

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlResult.handle`.
