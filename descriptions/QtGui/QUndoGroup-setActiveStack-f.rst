.. sip:method-description::
    :status: todo
    :pysig: 0a375e310abdbc97200cfcaf02680cd4
    :realsig: (QUndoStack*)
    :digest: a8ea81d0135011f529126de70dca5d3a

Sets the active stack of this group to *stack*.

If the stack is not a member of this group, this function does nothing.

Synonymous with calling :sip:ref:`~PyQt6.QtGui.QUndoStack.setActive` on *stack*.

The actions returned by :sip:ref:`~PyQt6.QtGui.QUndoGroup.createUndoAction` and :sip:ref:`~PyQt6.QtGui.QUndoGroup.createRedoAction` will now behave in the same way as those returned by *stack*'s :sip:ref:`~PyQt6.QtGui.QUndoStack.createUndoAction` and :sip:ref:`~PyQt6.QtGui.QUndoStack.createRedoAction`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QUndoStack.setActive`, :sip:ref:`~PyQt6.QtGui.QUndoGroup.activeStack`.
