.. sip:method-description::
    :status: todo
    :pysig: a90dc4e368a15f80c8425544effa3f09
    :realsig: (int,int)
    :digest: cf04377f928f3a3428582f418a2e2aed

Creates a new table with the given number of *rows* and *columns*, inserts it at the current cursor :sip:ref:`~PyQt6.QtGui.QTextCursor.position` in the document, and returns the table object. The cursor is moved to the beginning of the first cell.

There must be at least one row and one column in the table.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextCursor.currentTable`.
