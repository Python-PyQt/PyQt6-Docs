.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: b617c13689d09a29fda10da40592e708

Applies a change to the document. This function must be implemented in the derived class. Calling :sip:ref:`~PyQt6.QtGui.QUndoStack.push`, :sip:ref:`~PyQt6.QtGui.QUndoStack.undo` or :sip:ref:`~PyQt6.QtGui.QUndoStack.redo` from this function leads to undefined beahavior.

The default implementation calls  on all child commands.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QUndoCommand.undo`.
