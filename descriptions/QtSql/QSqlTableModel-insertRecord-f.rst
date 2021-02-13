.. sip:method-description::
    :status: todo
    :pysig: 9ee2dcc90695de556a0ce939db47d1d1
    :realsig: (int,const QSqlRecord&)
    :digest: 8554ea739b9837c69b71af5d54489b01

Inserts the *record* at position *row*. If *row* is negative, the record will be appended to the end. Calls :sip:ref:`~PyQt6.QtSql.QSqlTableModel.insertRows` and :sip:ref:`~PyQt6.QtSql.QSqlTableModel.setRecord` internally.

Returns ``true`` if the record could be inserted, otherwise false.

Changes are submitted immediately for :sip:ref:`~PyQt6.QtSql.QSqlTableModel.EditStrategy.OnFieldChange` and :sip:ref:`~PyQt6.QtSql.QSqlTableModel.EditStrategy.OnRowChange`. Failure does not leave a new row in the model.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlTableModel.insertRows`, :sip:ref:`~PyQt6.QtSql.QSqlTableModel.removeRows`, :sip:ref:`~PyQt6.QtSql.QSqlTableModel.setRecord`.
