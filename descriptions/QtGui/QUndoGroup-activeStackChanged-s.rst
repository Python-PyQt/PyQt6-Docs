.. sip:signal-description::
    :status: todo
    :pysig: 0a375e310abdbc97200cfcaf02680cd4
    :realsig: (QUndoStack*)
    :digest: 7421fbd77e21cbd1b87e75f02b65cd2e

This signal is emitted whenever the active stack of the group changes. This can happen when :sip:ref:`~PyQt6.QtGui.QUndoGroup.setActiveStack` or :sip:ref:`~PyQt6.QtGui.QUndoStack.setActive` is called, or when the active stack is removed form the group. *stack* is the new active stack. If no stack is active, *stack* is 0.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QUndoGroup.setActiveStack`, :sip:ref:`~PyQt6.QtGui.QUndoStack.setActive`.
