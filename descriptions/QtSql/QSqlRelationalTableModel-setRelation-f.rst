.. sip:method-description::
    :status: todo
    :pysig: fc3e361139971a3c5e3e7f02ff7bc95a
    :realsig: (int,const QSqlRelation&)
    :digest: a5c452f6839097254c35e82e1a82305b

Lets the specified *column* be a foreign index specified by *relation*.

Example:

.. literalinclude:: ../../../snippets/qtbase-examples-sql-relationaltablemodel-relationaltablemodel.py
    :lines: 63-63

.. literalinclude:: ../../../snippets/qtbase-examples-sql-relationaltablemodel-relationaltablemodel.py
    :lines: 68-68

The setRelation() call specifies that column 2 in table ``employee`` is a foreign key that maps with field ``id`` of table ``city``, and that the view should present the ``city``'s ``name`` field to the user.

Note: The table's primary key may not contain a relation to another table.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlRelationalTableModel.relation`.
