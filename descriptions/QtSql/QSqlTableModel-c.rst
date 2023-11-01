.. sip:class-description::
    :status: todo
    :brief: Editable data model for a single database table
    :digest: cf7d548d214c5daaf8fbde12220c3936

The :sip:ref:`~PyQt6.QtSql.QSqlTableModel` class provides an editable data model for a single database table.

:sip:ref:`~PyQt6.QtSql.QSqlTableModel` is a high-level interface for reading and writing database records from a single table. It is built on top of the lower-level :sip:ref:`~PyQt6.QtSql.QSqlQuery` and can be used to provide data to view classes such as :sip:ref:`~PyQt6.QtWidgets.QTableView`. For example:

.. literalinclude:: ../../../snippets/qtbase-src-sql-doc-snippets-sqldatabase-sqldatabase_snippet.py
    :lines: 112-122

We set the SQL table's name and the edit strategy, then we set up the labels displayed in the view header. The edit strategy dictates when the changes done by the user in the view are actually applied to the database. The possible values are :sip:ref:`~PyQt6.QtSql.QSqlTableModel.EditStrategy.OnFieldChange`, :sip:ref:`~PyQt6.QtSql.QSqlTableModel.EditStrategy.OnRowChange`, and :sip:ref:`~PyQt6.QtSql.QSqlTableModel.EditStrategy.OnManualSubmit`.

:sip:ref:`~PyQt6.QtSql.QSqlTableModel` can also be used to access a database programmatically, without binding it to a view:

.. literalinclude:: ../../../snippets/qtbase-src-sql-doc-snippets-sqldatabase-sqldatabase.py
    :lines: 262-265

The code snippet above extracts the ``salary`` field from record 4 in the result set of the query ``SELECT \* from employee``.

It is possible to set filters using :sip:ref:`~PyQt6.QtSql.QSqlTableModel.setFilter`, or modify the sort order using :sip:ref:`~PyQt6.QtSql.QSqlTableModel.setSort`. At the end, you must call :sip:ref:`~PyQt6.QtSql.QSqlTableModel.select` to populate the model with data.

The `tablemodel <https://doc.qt.io/qt-6/qtsql-tablemodel-example.html>`_ example illustrates how to use :sip:ref:`~PyQt6.QtSql.QSqlTableModel` as the data source for a :sip:ref:`~PyQt6.QtWidgets.QTableView`.

:sip:ref:`~PyQt6.QtSql.QSqlTableModel` provides no direct support for foreign keys. Use the :sip:ref:`~PyQt6.QtSql.QSqlRelationalTableModel` and :sip:ref:`~PyQt6.QtSql.QSqlRelationalDelegate` if you want to resolve foreign keys.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlRelationalTableModel`, :sip:ref:`~PyQt6.QtSql.QSqlQuery`, `Model/View Programming <https://doc.qt.io/qt-6/model-view-programming.html>`_, `Table Model Example <https://doc.qt.io/qt-6/qtsql-tablemodel-example.html>`_, `Cached SQL Table <https://doc.qt.io/qt-6/qtsql-cachedtable-example.html>`_.
