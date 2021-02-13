.. sip:class-description::
    :status: todo
    :brief: Represents a table in a QTextDocument
    :digest: 23618fea0ff0b24b6d10d7b1dd3482fa

The :sip:ref:`~PyQt6.QtGui.QTextTable` class represents a table in a :sip:ref:`~PyQt6.QtGui.QTextDocument`.

A table is a group of cells ordered into rows and columns. Each table contains at least one row and one column. Each cell contains a block, and is surrounded by a frame.

Tables are usually created and inserted into a document with the :sip:ref:`~PyQt6.QtGui.QTextCursor.insertTable` function. For example, we can insert a table with three rows and two columns at the current cursor position in an editor using the following lines of code:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-textdocument-tables-mainwindow.py
    :lines: 76-78

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-textdocument-tables-mainwindow.py
    :lines: 94-94

The table format is either defined when the table is created or changed later with :sip:ref:`~PyQt6.QtGui.QTextTable.setFormat`.

The table currently being edited by the cursor is found with :sip:ref:`~PyQt6.QtGui.QTextCursor.currentTable`. This allows its format or dimensions to be changed after it has been inserted into a document.

A table's size can be changed with :sip:ref:`~PyQt6.QtGui.QTextTable.resize`, or by using :sip:ref:`~PyQt6.QtGui.QTextTable.insertRows`, :sip:ref:`~PyQt6.QtGui.QTextTable.insertColumns`, :sip:ref:`~PyQt6.QtGui.QTextTable.removeRows`, or :sip:ref:`~PyQt6.QtGui.QTextTable.removeColumns`. Use :sip:ref:`~PyQt6.QtGui.QTextTable.cellAt` to retrieve table cells.

The starting and ending positions of table rows can be found by moving a cursor within a table, and using the :sip:ref:`~PyQt6.QtGui.QTextTable.rowStart` and :sip:ref:`~PyQt6.QtGui.QTextTable.rowEnd` functions to obtain cursors at the start and end of each row.

Rows and columns within a :sip:ref:`~PyQt6.QtGui.QTextTable` can be merged and split using the :sip:ref:`~PyQt6.QtGui.QTextTable.mergeCells` and :sip:ref:`~PyQt6.QtGui.QTextTable.splitCell` functions. However, only cells that span multiple rows or columns can be split. (Merging or splitting does not increase or decrease the number of rows and columns.)

Note that if you have merged multiple columns and rows into one cell, you will not be able to split the merged cell into new cells spanning over more than one row or column. To be able to split cells spanning over several rows and columns you need to do this over several iterations.

+-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |image-texttable-split-png| | Suppose we have a 2x3 table of names and addresses. To merge both columns in the first row we invoke :sip:ref:`~PyQt6.QtGui.QTextTable.mergeCells` with *row* = 0, *column* = 0, *numRows* = 1 and *numColumns* = 2. |
|                             |                                                                                                                                                                                                                      |
|                             | .. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-textdocument-texttable-main.py                                                                                                                     |
|                             |     :lines: 90-90                                                                                                                                                                                                    |
+-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |image-texttable-merge-png| | This gives us the following table. To split the first row of the table back into two cells, we invoke the :sip:ref:`~PyQt6.QtGui.QTextTable.splitCell` function with *numRows* and *numCols* = 1.                    |
|                             |                                                                                                                                                                                                                      |
|                             | .. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-textdocument-texttable-main.py                                                                                                                     |
|                             |     :lines: 92-92                                                                                                                                                                                                    |
+-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |image-texttable-split-png| | This results in the original table.                                                                                                                                                                                  |
+-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextTableFormat`.

.. |image-texttable-split-png| image:: ../../../images/texttable-split.png
.. |image-texttable-merge-png| image:: ../../../images/texttable-merge.png
