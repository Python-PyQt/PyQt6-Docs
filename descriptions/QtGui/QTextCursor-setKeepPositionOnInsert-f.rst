.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: cf84844f1dde63dd103f0451e045dff4

Defines whether the cursor should keep its current position when text gets inserted at the current position of the cursor.

If *b* is true, the cursor keeps its current position when text gets inserted at the positing of the cursor. If *b* is false, the cursor moves along with the inserted text.

The default is false.

Note that a cursor always moves when text is inserted before the current position of the cursor, and it always keeps its position when text is inserted after the current position of the cursor.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextCursor.keepPositionOnInsert`.
