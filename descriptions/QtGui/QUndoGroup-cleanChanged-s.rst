.. sip:signal-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: da5f121191e3718d4a2df5e8a17f2bd3

This signal is emitted whenever the active stack emits :sip:ref:`~PyQt6.QtGui.QUndoStack.cleanChanged` or the active stack changes.

*clean* is the new state, or true if the active stack is 0.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QUndoStack.cleanChanged`, :sip:ref:`~PyQt6.QtGui.QUndoGroup.setActiveStack`.
