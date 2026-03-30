.. sip:signal-description::
    :status: todo
    :pysig: 464116456943d857ef223b2d24ec328b
    :realsig: (const QString&)
    :digest: c4a3b6c739bcbe8e6924c6018af06dd8

This signal is emitted whenever the active stack emits :sip:ref:`~PyQt6.QtGui.QUndoStack.undoTextChanged` or the active stack changes.

*undoText* is the new state, or an empty string if the active stack is 0.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QUndoStack.undoTextChanged`, :sip:ref:`~PyQt6.QtGui.QUndoGroup.setActiveStack`.
