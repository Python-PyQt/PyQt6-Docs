.. sip:method-description::
    :status: todo
    :pysig: 47bc384ef78158df7bdc68df0f06aef9
    :realsig: (int)
    :digest: 94b3da272804a115c4cf8b1548c5e230

Refreshes *row* in the model with values from the database table row matching on primary key values. Without a primary key, all column values must match. If no matching row is found, the model will show an empty row.

Returns ``true`` if successful; otherwise returns ``false``.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlTableModel.select`.
