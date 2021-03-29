.. sip:method-description::
    :status: todo
    :pysig: 0a375e310abdbc97200cfcaf02680cd4
    :realsig: (QUndoStack*)
    :digest: 64bb1d64ed995cf68a391f885a32481e

Adds *stack* to this group. The group does not take ownership of the stack. Another way of adding a stack to a group is by specifying the group as the stack's parent :sip:ref:`~PyQt6.QtCore.QObject` in :sip:ref:`~PyQt6.QtGui.QUndoStack.__init__`. In this case, the stack is deleted when the group is deleted, in the usual manner of QObjects.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QUndoGroup.removeStack`, :sip:ref:`~PyQt6.QtGui.QUndoGroup.stacks`, :sip:ref:`~PyQt6.QtGui.QUndoStack.__init__`.
