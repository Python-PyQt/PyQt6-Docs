.. sip:signal-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 380e953478f23adb82cb22d0d9769e1d

This signal is emitted whenever the active stack emits :sip:ref:`~PyQt6.QtGui.QUndoStack.indexChanged` or the active stack changes.

*idx* is the new current index, or 0 if the active stack is 0.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QUndoStack.indexChanged`, :sip:ref:`~PyQt6.QtGui.QUndoGroup.setActiveStack`.
