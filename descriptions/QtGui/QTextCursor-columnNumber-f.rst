.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: e09423ac40fae73b80067137b2e5953a

Returns the position of the cursor within its containing line.

Note that this is the column number relative to a wrapped line, not relative to the block (i.e. the paragraph).

You probably want to call :sip:ref:`~PyQt6.QtGui.QTextCursor.positionInBlock` instead.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextCursor.positionInBlock`.
