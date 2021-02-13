.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 410451171ff32313935d669de9d0a9de

Marks the stack as clean and emits :sip:ref:`~PyQt6.QtGui.QUndoStack.cleanChanged` if the stack was not already clean.

This is typically called when a document is saved, for example.

Whenever the stack returns to this state through the use of undo/redo commands, it emits the signal :sip:ref:`~PyQt6.QtGui.QUndoStack.cleanChanged`. This signal is also emitted when the stack leaves the clean state.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QUndoStack.isClean`, :sip:ref:`~PyQt6.QtGui.QUndoStack.resetClean`, :sip:ref:`~PyQt6.QtGui.QUndoStack.cleanIndex`.
