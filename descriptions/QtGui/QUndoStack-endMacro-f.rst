.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 6f8d56b8521fbcf91abfa8dd6566572c

Ends composition of a macro command.

If this is the outermost macro in a set nested macros, this function emits :sip:ref:`~PyQt6.QtGui.QUndoStack.indexChanged` once for the entire macro command.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QUndoStack.beginMacro`.
