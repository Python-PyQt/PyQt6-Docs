.. sip:method-description::
    :status: todo
    :pysig: 5f08101561b67f3928153b71960768ab
    :realsig: (int) const
    :digest: c20c898aebff68af81054f18b730ffa9

Returns a :sip:ref:`~PyQt6.QtSql.QSqlTableModel` object for accessing the table for which *column* is a foreign key, or ``nullptr`` if there is no relation for the given *column*.

The returned object is owned by the :sip:ref:`~PyQt6.QtSql.QSqlRelationalTableModel`.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlRelationalTableModel.setRelation`, :sip:ref:`~PyQt6.QtSql.QSqlRelationalTableModel.relation`.
