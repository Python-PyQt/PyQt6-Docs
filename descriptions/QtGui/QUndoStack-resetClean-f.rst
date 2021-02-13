.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: e2a26fa011ce9adee52be5e9c6b0fab5

Leaves the clean state and emits :sip:ref:`~PyQt6.QtGui.QUndoStack.cleanChanged` if the stack was clean. This method resets the clean index to -1.

This is typically called in the following cases, when a document has been:

* created basing on some template and has not been saved, so no filename has been associated with the document yet.

* restored from a backup file.

* changed outside of the editor and the user did not reload it.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QUndoStack.isClean`, :sip:ref:`~PyQt6.QtGui.QUndoStack.setClean`, :sip:ref:`~PyQt6.QtGui.QUndoStack.cleanIndex`.
