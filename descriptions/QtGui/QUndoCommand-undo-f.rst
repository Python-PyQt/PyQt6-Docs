.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 914dffa175ded0576d70ee599e64748b

Reverts a change to the document. After  is called, the state of the document should be the same as before :sip:ref:`~PyQt6.QtGui.QUndoCommand.redo` was called. This function must be implemented in the derived class. Calling :sip:ref:`~PyQt6.QtGui.QUndoStack.push`, :sip:ref:`~PyQt6.QtGui.QUndoStack.undo` or :sip:ref:`~PyQt6.QtGui.QUndoStack.redo` from this function leads to undefined beahavior.

The default implementation calls  on all child commands in reverse order.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QUndoCommand.redo`.
