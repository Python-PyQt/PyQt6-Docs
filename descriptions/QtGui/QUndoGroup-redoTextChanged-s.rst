.. sip:signal-description::
    :status: todo
    :pysig: 464116456943d857ef223b2d24ec328b
    :realsig: (const QString&)
    :digest: 1c0b40031a532a65c235219c759ed0a0

This signal is emitted whenever the active stack emits :sip:ref:`~PyQt6.QtGui.QUndoStack.redoTextChanged` or the active stack changes.

*redoText* is the new state, or an empty string if the active stack is 0.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QUndoStack.redoTextChanged`, :sip:ref:`~PyQt6.QtGui.QUndoGroup.setActiveStack`.
