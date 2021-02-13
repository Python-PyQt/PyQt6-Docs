.. sip:method-description::
    :status: todo
    :pysig: be511a50f809d32bef8692df1f6d4389
    :realsig: (const QSqlRecord&)
    :digest: 26727895b9b1354328fb35d438a7fc38

Inserts the values *values* into the currently active database table.

This is a low-level method that operates directly on the database and should not be called directly. Use insertRow() and :sip:ref:`~PyQt6.QtSql.QSqlTableModel.setData` to insert values. The model will decide depending on its edit strategy when to modify the database.

Returns ``true`` if the values could be inserted, otherwise false. Error information can be retrieved with lastError().

.. seealso:: lastError(), insertRow(), :sip:ref:`~PyQt6.QtSql.QSqlTableModel.insertRows`.
