.. sip:enum-description::
    :status: todo
    :digest: e87f081cc586c8cb33032b7789598cf8

This enum type describes which strategy to choose when editing values in the database.

Note: To prevent inserting only partly initialized rows into the database, ``OnFieldChange`` will behave like ``OnRowChange`` for newly inserted rows.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlTableModel.setEditStrategy`.
