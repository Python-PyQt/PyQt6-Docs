.. sip:signal-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: d9e5cfa456fed97646d5f4aae1524277

This signal is emitted whenever a command modifies the state of the document. This happens when a command is undone or redone. When a macro command is undone or redone, or :sip:ref:`~PyQt6.QtGui.QUndoStack.setIndex` is called, this signal is emitted only once.

*idx* specifies the index of the current command, ie. the command which will be executed on the next call to :sip:ref:`~PyQt6.QtGui.QUndoStack.redo`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QUndoStack.index`, :sip:ref:`~PyQt6.QtGui.QUndoStack.setIndex`.
