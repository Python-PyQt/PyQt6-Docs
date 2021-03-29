.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 2e275fee7b6558e8f37fd7c38cc00e37

Returns ``true`` if there is a command available for redo; otherwise returns ``false``.

This function returns ``false`` if the stack is empty or if the top command on the stack has already been redone.

Synonymous with :sip:ref:`~PyQt6.QtGui.QUndoStack.index` == :sip:ref:`~PyQt6.QtGui.QUndoStack.count`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QUndoStack.index`, :sip:ref:`~PyQt6.QtGui.QUndoStack.canUndo`.
