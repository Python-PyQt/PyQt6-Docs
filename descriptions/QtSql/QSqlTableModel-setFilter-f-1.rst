.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: 7c6c1a878bee8beec7e981131254b2a3

Sets the current filter to *filter*.

The filter is a SQL ``WHERE`` clause without the keyword ``WHERE`` (for example, ``name='Josephine')``.

If the model is already populated with data from a database, the model re-selects it with the new filter. Otherwise, the filter will be applied the next time :sip:ref:`~PyQt6.QtSql.QSqlTableModel.select` is called.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlTableModel.filter`, :sip:ref:`~PyQt6.QtSql.QSqlTableModel.select`, :sip:ref:`~PyQt6.QtSql.QSqlTableModel.selectStatement`, :sip:ref:`~PyQt6.QtSql.QSqlTableModel.orderByClause`.
