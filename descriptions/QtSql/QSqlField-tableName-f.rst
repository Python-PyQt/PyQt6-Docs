.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 94a63b34704c8b22e49037ab746d9859

Returns the  of the field.

**Note:** When using the QPSQL driver, due to limitations in the libpq library, the ``tableName()`` field is not populated in a :sip:ref:`~PyQt6.QtSql.QSqlField` resulting from a :sip:ref:`~PyQt6.QtSql.QSqlRecord` obtained by :sip:ref:`~PyQt6.QtSql.QSqlQuery.record` of a forward-only query.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlField.setTableName`.
