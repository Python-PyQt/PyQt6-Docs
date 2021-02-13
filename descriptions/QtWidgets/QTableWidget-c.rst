.. sip:class-description::
    :status: todo
    :brief: Item-based table view with a default model
    :digest: 73a8fd801f0d7faeb5781840e66c0a55

The :sip:ref:`~PyQt6.QtWidgets.QTableWidget` class provides an item-based table view with a default model.

.. image:: ../../../images/windows-tableview.png

Table widgets provide standard table display facilities for applications. The items in a :sip:ref:`~PyQt6.QtWidgets.QTableWidget` are provided by :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`.

If you want a table that uses your own data model you should use :sip:ref:`~PyQt6.QtWidgets.QTableView` rather than this class.

Table widgets can be constructed with the required numbers of rows and columns:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-qtablewidget-using-mainwindow.py
    :lines: 74-74

Alternatively, tables can be constructed without a given size and resized later:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-qtablewidget-resizing-mainwindow.py
    :lines: 73-73

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-qtablewidget-resizing-mainwindow.py
    :lines: 90-91

Items are created outside the table (with no parent widget) and inserted into the table with :sip:ref:`~PyQt6.QtWidgets.QTableWidget.setItem`:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-qtablewidget-resizing-mainwindow.py
    :lines: 97-99

If you want to enable sorting in your table widget, do so after you have populated it with items, otherwise sorting may interfere with the insertion order (see :sip:ref:`~PyQt6.QtWidgets.QTableWidget.setItem` for details).

Tables can be given both horizontal and vertical headers. The simplest way to create the headers is to supply a list of strings to the :sip:ref:`~PyQt6.QtWidgets.QTableWidget.setHorizontalHeaderLabels` and :sip:ref:`~PyQt6.QtWidgets.QTableWidget.setVerticalHeaderLabels` functions. These will provide simple textual headers for the table's columns and rows. More sophisticated headers can be created from existing table items that are usually constructed outside the table. For example, we can construct a table item with an icon and aligned text, and use it as the header for a particular column:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-qtablewidget-using-mainwindow.py
    :lines: 87-89

The number of rows in the table can be found with :sip:ref:`~PyQt6.QtWidgets.QTableWidget.rowCount`, and the number of columns with :sip:ref:`~PyQt6.QtWidgets.QTableWidget.columnCount`. The table can be cleared with the :sip:ref:`~PyQt6.QtWidgets.QTableWidget.clear` function.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTableWidgetItem`, :sip:ref:`~PyQt6.QtWidgets.QTableView`, `Model/View Programming <https://doc.qt.io/qt-6/model-view-programming.html>`_.
