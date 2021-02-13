.. sip:class-description::
    :status: todo
    :brief: Read-only data model for SQL result sets
    :digest: ca27dae5e740b5796934a34b9bbf04ff

The :sip:ref:`~PyQt6.QtSql.QSqlQueryModel` class provides a read-only data model for SQL result sets.

:sip:ref:`~PyQt6.QtSql.QSqlQueryModel` is a high-level interface for executing SQL statements and traversing the result set. It is built on top of the lower-level `QSqlQuery <https://doc.qt.io/qt-6/qtsql-changes-qt6.html#qsqlquery>`_ and can be used to provide data to view classes such as :sip:ref:`~PyQt6.QtWidgets.QTableView`. For example:

.. literalinclude:: ../../../snippets/qtbase-src-sql-doc-snippets-sqldatabase-sqldatabase_snippet.py
    :lines: 54-63

We set the model's query, then we set up the labels displayed in the view header.

:sip:ref:`~PyQt6.QtSql.QSqlQueryModel` can also be used to access a database programmatically, without binding it to a view:

.. literalinclude:: ../../../snippets/qtbase-src-sql-doc-snippets-sqldatabase-sqldatabase.py
    :lines: 219-221

The code snippet above extracts the ``salary`` field from record 4 in the result set of the ``SELECT`` query. Since ``salary`` is the 2nd column (or column index 1), we can rewrite the last line as follows:

.. literalinclude:: ../../../snippets/qtbase-src-sql-doc-snippets-sqldatabase-sqldatabase.py
    :lines: 227-227

The model is read-only by default. To make it read-write, you must subclass it and reimplement setData() and flags(). Another option is to use :sip:ref:`~PyQt6.QtSql.QSqlTableModel`, which provides a read-write model based on a single database table.

The `querymodel <https://doc.qt.io/qt-6/qtsql-querymodel-example.html>`_ example illustrates how to use :sip:ref:`~PyQt6.QtSql.QSqlQueryModel` to display the result of a query. It also shows how to subclass :sip:ref:`~PyQt6.QtSql.QSqlQueryModel` to customize the contents of the data before showing it to the user, and how to create a read-write model based on :sip:ref:`~PyQt6.QtSql.QSqlQueryModel`.

If the database doesn't return the number of selected rows in a query, the model will fetch rows incrementally. See :sip:ref:`~PyQt6.QtSql.QSqlQueryModel.fetchMore` for more information.

.. seealso:: :sip:ref:`~PyQt6.QtSql.QSqlTableModel`, :sip:ref:`~PyQt6.QtSql.QSqlRelationalTableModel`, `QSqlQuery <https://doc.qt.io/qt-6/qtsql-changes-qt6.html#qsqlquery>`_, `Model/View Programming <https://doc.qt.io/qt-6/model-view-programming.html>`_, `Query Model Example <https://doc.qt.io/qt-6/qtsql-querymodel-example.html>`_.
