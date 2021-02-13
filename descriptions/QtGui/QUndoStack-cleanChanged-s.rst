.. sip:signal-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: d2656c7f24747762422bee878d3d5dda

This signal is emitted whenever the stack enters or leaves the clean state. If *clean* is true, the stack is in a clean state; otherwise this signal indicates that it has left the clean state.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QUndoStack.isClean`, :sip:ref:`~PyQt6.QtGui.QUndoStack.setClean`.
