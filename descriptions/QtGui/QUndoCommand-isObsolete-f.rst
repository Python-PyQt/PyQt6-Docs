.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 41e894c792572ead454d18c31032e31b

Returns whether the command is obsolete.

The boolean is used for the automatic removal of commands that are not necessary in the stack anymore. The isObsolete function is checked in the functions :sip:ref:`~PyQt6.QtGui.QUndoStack.push`, :sip:ref:`~PyQt6.QtGui.QUndoStack.undo`, :sip:ref:`~PyQt6.QtGui.QUndoStack.redo`, and :sip:ref:`~PyQt6.QtGui.QUndoStack.setIndex`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QUndoCommand.setObsolete`, :sip:ref:`~PyQt6.QtGui.QUndoCommand.mergeWith`, :sip:ref:`~PyQt6.QtGui.QUndoStack.push`, :sip:ref:`~PyQt6.QtGui.QUndoStack.undo`, :sip:ref:`~PyQt6.QtGui.QUndoStack.redo`.
