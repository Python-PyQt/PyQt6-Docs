.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: 462433e430feb703e81ab48046b24f86

Sets the database table on which the model operates to *tableName*. Does not select data from the table, but fetches its field information.

To populate the model with the table's data, call :sip:ref:`~PyQt6.QtSql.QSqlTableModel.select`.

Error information can be retrieved with lastError().

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlTableModel.select`, :sip:ref:`~PyQt6.QtSql.QSqlTableModel.setFilter`, lastError().
