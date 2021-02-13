.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 83fc1b6df3f2d7abfc837ea300157e8d

Returns whether the command is obsolete.

The boolean is used for the automatic removal of commands that are not necessary in the stack anymore. The  function is checked in the functions :sip:ref:`~PyQt6.QtGui.QUndoStack.push`, :sip:ref:`~PyQt6.QtGui.QUndoStack.undo`, :sip:ref:`~PyQt6.QtGui.QUndoStack.redo`, and :sip:ref:`~PyQt6.QtGui.QUndoStack.setIndex`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QUndoCommand.setObsolete`, :sip:ref:`~PyQt6.QtGui.QUndoCommand.mergeWith`, :sip:ref:`~PyQt6.QtGui.QUndoStack.push`, :sip:ref:`~PyQt6.QtGui.QUndoStack.undo`, :sip:ref:`~PyQt6.QtGui.QUndoStack.redo`.
