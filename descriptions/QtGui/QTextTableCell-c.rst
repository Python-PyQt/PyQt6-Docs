.. sip:class-description::
    :status: todo
    :brief: Represents the properties of a cell in a QTextTable
    :digest: 8b9847318e786c1eef34fb0b0fc58a8c

The :sip:ref:`~PyQt6.QtGui.QTextTableCell` class represents the properties of a cell in a :sip:ref:`~PyQt6.QtGui.QTextTable`.

Table cells are pieces of document structure that belong to a table. The table orders cells into particular rows and columns; cells can also span multiple columns and rows.

Cells are usually created when a table is inserted into a document with :sip:ref:`~PyQt6.QtGui.QTextCursor.insertTable`, but they are also created and destroyed when a table is resized.

Cells contain information about their location in a table; you can obtain the :sip:ref:`~PyQt6.QtGui.QTextTableCell.row` and :sip:ref:`~PyQt6.QtGui.QTextTableCell.column` numbers of a cell, and its :sip:ref:`~PyQt6.QtGui.QTextTableCell.rowSpan` and :sip:ref:`~PyQt6.QtGui.QTextTableCell.columnSpan`.

The :sip:ref:`~PyQt6.QtGui.QTextTableCell.format` of a cell describes the default character format of its contents. The :sip:ref:`~PyQt6.QtGui.QTextTableCell.firstCursorPosition` and :sip:ref:`~PyQt6.QtGui.QTextTableCell.lastCursorPosition` functions are used to obtain the extent of the cell in the document.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextTable`, :sip:ref:`~PyQt6.QtGui.QTextTableFormat`.
