.. sip:signal-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: d352bbf66b74ce5a4dec5e3df4913c9a

This signal is emitted whenever the active stack emits :sip:ref:`~PyQt6.QtGui.QUndoStack.canRedoChanged` or the active stack changes.

*canRedo* is the new state, or false if the active stack is 0.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QUndoStack.canRedoChanged`, :sip:ref:`~PyQt6.QtGui.QUndoGroup.setActiveStack`.
