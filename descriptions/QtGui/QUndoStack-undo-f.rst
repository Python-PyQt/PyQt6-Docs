.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 84052d9a018c86648731360aa7f78905

Undoes the command below the current command by calling :sip:ref:`~PyQt6.QtGui.QUndoCommand.undo`. Decrements the current command index.

If the stack is empty, or if the bottom command on the stack has already been undone, this function does nothing.

After the command is undone, if :sip:ref:`~PyQt6.QtGui.QUndoCommand.isObsolete` returns ``true``, then the command will be deleted from the stack. Additionally, if the clean index is greater than or equal to the current command index, then the clean index is reset.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QUndoStack.redo`, :sip:ref:`~PyQt6.QtGui.QUndoStack.index`.
