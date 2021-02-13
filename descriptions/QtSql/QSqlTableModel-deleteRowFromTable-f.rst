.. sip:method-description::
    :status: todo
    :pysig: 47bc384ef78158df7bdc68df0f06aef9
    :realsig: (int)
    :digest: 1bb41219747a449972d19aa3fc102b7e

Deletes the given *row* from the currently active database table.

This is a low-level method that operates directly on the database and should not be called directly. Use removeRow() or :sip:ref:`~PyQt6.QtSql.QSqlTableModel.removeRows` to delete values. The model will decide depending on its edit strategy when to modify the database.

Returns ``true`` if the row was deleted; otherwise returns ``false``.

.. seealso:: removeRow(), :sip:ref:`~PyQt6.QtSql.QSqlTableModel.removeRows`.
