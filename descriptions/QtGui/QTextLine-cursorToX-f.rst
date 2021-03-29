.. sip:method-description::
    :status: todo
    :pysig: 0b95f7bf02cfa179a1f70864a46d7f9d
    :realsig: (int*,QTextLine::Edge) const
    :digest: 50e7ba620b7bfaee47a7d7c22677cc10

Converts the cursor position *cursorPos* to the corresponding x position inside the line, taking account of the *edge*.

If *cursorPos* is not a valid cursor position, the nearest valid cursor position will be used instead, and *cursorPos* will be modified to point to this valid cursor position.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextLine.xToCursor`.
