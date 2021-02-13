.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 9cf61f223c1edc8654639c582678e7cd

Redoes the current command by calling :sip:ref:`~PyQt6.QtGui.QUndoCommand.redo`. Increments the current command index.

If the stack is empty, or if the top command on the stack has already been redone, this function does nothing.

If :sip:ref:`~PyQt6.QtGui.QUndoCommand.isObsolete` returns true for the current command, then the command will be deleted from the stack. Additionally, if the clean index is greater than or equal to the current command index, then the clean index is reset.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QUndoStack.undo`, :sip:ref:`~PyQt6.QtGui.QUndoStack.index`.
