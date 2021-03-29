.. sip:signal-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: 1c0b40031a532a65c235219c759ed0a0

This signal is emitted whenever the active stack emits :sip:ref:`~PyQt6.QtGui.QUndoStack.redoTextChanged` or the active stack changes.

*redoText* is the new state, or an empty string if the active stack is 0.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QUndoStack.redoTextChanged`, :sip:ref:`~PyQt6.QtGui.QUndoGroup.setActiveStack`.
