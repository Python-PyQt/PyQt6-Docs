.. sip:method-description::
    :status: todo
    :pysig: 9ee2dcc90695de556a0ce939db47d1d1
    :realsig: (int,const QSqlRecord&)
    :digest: eb941e7eb4bc754ad6719e36dcb6317a

Applies *values* to the *row* in the model. The source and target fields are mapped by field name, not by position in the record.

Note that the generated flags in *values* are preserved to determine whether the corresponding fields are used when changes are submitted to the database. By default, it is set to ``true`` for all fields in a :sip:ref:`~PyQt6.QtSql.QSqlRecord`. You must set the flag to ``false`` using :sip:ref:`~PyQt6.QtSql.QSqlRecord.setGenerated`\ (false) for any value in *values*, to save changes back to the database.

For edit strategies :sip:ref:`~PyQt6.QtSql.QSqlTableModel.EditStrategy.OnFieldChange` and :sip:ref:`~PyQt6.QtSql.QSqlTableModel.EditStrategy.OnRowChange`, a row may receive a change only if no other row has a cached change. Changes are submitted immediately. Submitted changes are not reverted upon failure.

Returns ``true`` if all the values could be set; otherwise returns false.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlTableModel.record`, :sip:ref:`~PyQt6.QtSql.QSqlTableModel.editStrategy`.
