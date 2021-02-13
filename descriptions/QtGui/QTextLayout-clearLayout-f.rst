.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 8494d1bf88021865d76b7f0dfb386af9

Clears the line information in the layout. After having called this function, :sip:ref:`~PyQt6.QtGui.QTextLayout.lineCount` returns 0.

**Warning:** This will invalidate the layout, so all existing :sip:ref:`~PyQt6.QtGui.QTextLine` objects that refer to the previous contents should now be discarded.
