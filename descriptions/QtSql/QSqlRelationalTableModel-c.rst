.. sip:class-description::
    :status: todo
    :brief: Editable data model for a single database table, with foreign key support
    :digest: 49c3fadc1e1c9576e8bc68d63f768538

The :sip:ref:`~PyQt6.QtSql.QSqlRelationalTableModel` class provides an editable data model for a single database table, with foreign key support.

:sip:ref:`~PyQt6.QtSql.QSqlRelationalTableModel` acts like :sip:ref:`~PyQt6.QtSql.QSqlTableModel`, but allows columns to be set as foreign keys into other database tables.

+---------------------------+-------------------------+
| |image-noforeignkeys-png| | |image-foreignkeys-png| |
+---------------------------+-------------------------+

The screenshot on the left shows a plain :sip:ref:`~PyQt6.QtSql.QSqlTableModel` in a :sip:ref:`~PyQt6.QtWidgets.QTableView`. Foreign keys (``city`` and ``country``) aren't resolved to human-readable values. The screenshot on the right shows a :sip:ref:`~PyQt6.QtSql.QSqlRelationalTableModel`, with foreign keys resolved into human-readable text strings.

The following code snippet shows how the :sip:ref:`~PyQt6.QtSql.QSqlRelationalTableModel` was set up:

.. literalinclude:: ../../../snippets/qtbase-examples-sql-relationaltablemodel-relationaltablemodel.py
    :lines: 63-63

.. literalinclude:: ../../../snippets/qtbase-examples-sql-relationaltablemodel-relationaltablemodel.py
    :lines: 68-68

.. literalinclude:: ../../../snippets/qtbase-examples-sql-relationaltablemodel-relationaltablemodel.py
    :lines: 70-70

The :sip:ref:`~PyQt6.QtSql.QSqlRelationalTableModel.setRelation` function calls establish a relationship between two tables. The first call specifies that column 2 in table ``employee`` is a foreign key that maps with field ``id`` of table ``city``, and that the view should present the ``city``'s ``name`` field to the user. The second call does something similar with column 3.

If you use a read-write :sip:ref:`~PyQt6.QtSql.QSqlRelationalTableModel`, you probably want to use :sip:ref:`~PyQt6.QtSql.QSqlRelationalDelegate` on the view. Unlike the default delegate, :sip:ref:`~PyQt6.QtSql.QSqlRelationalDelegate` provides a combobox for fields that are foreign keys into other tables. To use the class, simply call :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.setItemDelegate` on the view with an instance of :sip:ref:`~PyQt6.QtSql.QSqlRelationalDelegate`:

.. literalinclude:: ../../../snippets/qtbase-examples-sql-relationaltablemodel-relationaltablemodel.py
    :lines: 86-88

The `relationaltablemodel <https://doc.qt.io/qt-6/qtsql-relationaltablemodel-example.html>`_ example illustrates how to use :sip:ref:`~PyQt6.QtSql.QSqlRelationalTableModel` in conjunction with :sip:ref:`~PyQt6.QtSql.QSqlRelationalDelegate` to provide tables with foreign key support.

.. image:: ../../../images/relationaltable.png

Notes:

* The table must have a primary key declared.

* The table's primary key may not contain a relation to another table.

* If a relational table contains keys that refer to non-existent rows in the referenced table, the rows containing the invalid keys will not be exposed through the model. The user or the database is responsible for keeping referential integrity.

* If a relation's display column name is also used as a column name in the relational table, or if it is used as display column name in more than one relation it will be aliased. The alias is the relation's table name, display column name and a unique id joined by an underscore (e.g. tablename_columnname_id). :sip:ref:`~PyQt6.QtSql.QSqlRecord.fieldName` will return the aliased column name. All occurrences of the duplicate display column name are aliased when duplication is detected, but no aliasing is done to the column names in the main table. The aliasing doesn't affect :sip:ref:`~PyQt6.QtSql.QSqlRelation`, so :sip:ref:`~PyQt6.QtSql.QSqlRelation.displayColumn` will return the original display column name.

* The reference table name is aliased. The alias is the word "relTblAl" and the relationed column index joined by an underscore (e.g. relTblAl_2). The alias can be used to filter the table (For example, setFilter("relTblAl_2='Oslo' OR relTblAl_3='USA'")).

* When using :sip:ref:`~PyQt6.QtSql.QSqlRelationalTableModel.setData` the role should always be :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.EditRole`, and when using :sip:ref:`~PyQt6.QtSql.QSqlRelationalTableModel.data` the role should always be :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DisplayRole`.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlRelation`, :sip:ref:`~PyQt6.QtSql.QSqlRelationalDelegate`, `Relational Table Model Example <https://doc.qt.io/qt-6/qtsql-relationaltablemodel-example.html>`_.

.. |image-noforeignkeys-png| image:: ../../../images/noforeignkeys.png
.. |image-foreignkeys-png| image:: ../../../images/foreignkeys.png
