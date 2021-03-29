.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 93e619b0968c61631c0c7d994d60b960

Returns the index of the current command. This is the command that will be executed on the next call to :sip:ref:`~PyQt6.QtGui.QUndoStack.redo`. It is not always the top-most command on the stack, since a number of commands may have been undone.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QUndoStack.setIndex`, :sip:ref:`~PyQt6.QtGui.QUndoStack.undo`, :sip:ref:`~PyQt6.QtGui.QUndoStack.redo`, :sip:ref:`~PyQt6.QtGui.QUndoStack.count`.
