.. sip:method-description::
    :status: todo
    :pysig: 5c68a2a0b3a3ad0ec9e3325df51e898a
    :realsig: (int,int,const QTextTableFormat&)
    :digest: efb393355b436cb3bbbaeba2314c0870

Creates a new table with the given number of *rows* and *columns* in the specified *format*, inserts it at the current cursor :sip:ref:`~PyQt6.QtGui.QTextCursor.position` in the document, and returns the table object. The cursor is moved to the beginning of the first cell.

There must be at least one row and one column in the table.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextCursor.currentTable`.
