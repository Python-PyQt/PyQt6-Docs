.. sip:signal-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: b21a461b5ff132e7abe892e984bd0a5c

This signal is emitted whenever the active stack emits :sip:ref:`~PyQt6.QtGui.QUndoStack.canUndoChanged` or the active stack changes.

*canUndo* is the new state, or false if the active stack is 0.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QUndoStack.canUndoChanged`, :sip:ref:`~PyQt6.QtGui.QUndoGroup.setActiveStack`.
