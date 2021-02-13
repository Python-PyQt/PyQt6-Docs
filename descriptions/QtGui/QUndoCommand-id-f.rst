.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: fb9f9440b0d33029e0fff57dc705f230

Returns the ID of this command.

A command ID is used in command compression. It must be an integer unique to this command's class, or -1 if the command doesn't support compression.

If the command supports compression this function must be overridden in the derived class to return the correct ID. The base implementation returns -1.

:sip:ref:`~PyQt6.QtGui.QUndoStack.push` will only try to merge two commands if they have the same ID, and the ID is not -1.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QUndoCommand.mergeWith`, :sip:ref:`~PyQt6.QtGui.QUndoStack.push`.
