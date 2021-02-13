.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 83bd2a376c53d395834211a6db47031a

Returns the clean index. This is the index at which :sip:ref:`~PyQt6.QtGui.QUndoStack.setClean` was called.

A stack may not have a clean index. This happens if a document is saved, some commands are undone, then a new command is pushed. Since :sip:ref:`~PyQt6.QtGui.QUndoStack.push` deletes all the undone commands before pushing the new command, the stack can't return to the clean state again. In this case, this function returns -1. The -1 may also be returned after an explicit call to :sip:ref:`~PyQt6.QtGui.QUndoStack.resetClean`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QUndoStack.isClean`, :sip:ref:`~PyQt6.QtGui.QUndoStack.setClean`.
