.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 05462b3012f19dc13b49ee99df8f6952

Returns the tableName of the field.

**Note:** When using the QPSQL driver, due to limitations in the libpq library, the ``tableName()`` field is not populated in a :sip:ref:`~PyQt6.QtSql.QSqlField` resulting from a :sip:ref:`~PyQt6.QtSql.QSqlRecord` obtained by :sip:ref:`~PyQt6.QtSql.QSqlQuery.record` of a forward-only query.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlField.setTableName`.
