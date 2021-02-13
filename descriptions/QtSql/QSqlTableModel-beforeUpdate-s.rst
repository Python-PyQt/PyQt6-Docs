.. sip:signal-description::
    :status: todo
    :pysig: edb3c45e5d6e0ecd4da9b4b877c5546f
    :realsig: (int,QSqlRecord&)
    :digest: a326c67c2c44ff79d3b3d3bfcdbb320a

This signal is emitted by :sip:ref:`~PyQt6.QtSql.QSqlTableModel.updateRowInTable` before the *row* is updated in the currently active database table with the values from *record*.

Note that only values that are marked as generated will be updated. The generated flag can be set with :sip:ref:`~PyQt6.QtSql.QSqlRecord.setGenerated` and checked with :sip:ref:`~PyQt6.QtSql.QSqlRecord.isGenerated`.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlRecord.isGenerated`.
