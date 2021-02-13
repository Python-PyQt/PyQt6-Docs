.. sip:method-description::
    :status: todo
    :pysig: 9ee2dcc90695de556a0ce939db47d1d1
    :realsig: (int,const QSqlRecord&)
    :digest: 9352125a15fdb466694e741e80580d75

Updates the given *row* in the currently active database table with the specified *values*. Returns ``true`` if successful; otherwise returns ``false``.

This is a low-level method that operates directly on the database and should not be called directly. Use :sip:ref:`~PyQt6.QtSql.QSqlTableModel.setData` to update values. The model will decide depending on its edit strategy when to modify the database.

Note that only values that have the generated-flag set are updated. The generated-flag can be set with :sip:ref:`~PyQt6.QtSql.QSqlRecord.setGenerated` and tested with :sip:ref:`~PyQt6.QtSql.QSqlRecord.isGenerated`.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlRecord.isGenerated`, :sip:ref:`~PyQt6.QtSql.QSqlTableModel.setData`.
