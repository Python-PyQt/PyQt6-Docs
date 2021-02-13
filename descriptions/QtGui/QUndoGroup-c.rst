.. sip:class-description::
    :status: todo
    :brief: Group of QUndoStack objects
    :digest: d2f1bf9d7535f17acca8c4d33777e761

The :sip:ref:`~PyQt6.QtGui.QUndoGroup` class is a group of :sip:ref:`~PyQt6.QtGui.QUndoStack` objects.

For an overview of the Qt's undo framework, see the overview.

An application often has multiple undo stacks, one for each opened document. At the same time, an application usually has one undo action and one redo action, which triggers undo or redo in the active document.

:sip:ref:`~PyQt6.QtGui.QUndoGroup` is a group of :sip:ref:`~PyQt6.QtGui.QUndoStack` objects, one of which may be active. It has an :sip:ref:`~PyQt6.QtGui.QUndoGroup.undo` and :sip:ref:`~PyQt6.QtGui.QUndoGroup.redo` slot, which calls :sip:ref:`~PyQt6.QtGui.QUndoStack.undo` and :sip:ref:`~PyQt6.QtGui.QUndoStack.redo` for the active stack. It also has the functions :sip:ref:`~PyQt6.QtGui.QUndoGroup.createUndoAction` and :sip:ref:`~PyQt6.QtGui.QUndoGroup.createRedoAction`. The actions returned by these functions behave in the same way as those returned by :sip:ref:`~PyQt6.QtGui.QUndoStack.createUndoAction` and :sip:ref:`~PyQt6.QtGui.QUndoStack.createRedoAction` of the active stack.

Stacks are added to a group with :sip:ref:`~PyQt6.QtGui.QUndoGroup.addStack` and removed with :sip:ref:`~PyQt6.QtGui.QUndoGroup.removeStack`. A stack is implicitly added to a group when it is created with the group as its parent :sip:ref:`~PyQt6.QtCore.QObject`.

It is the programmer's responsibility to specify which stack is active by calling :sip:ref:`~PyQt6.QtGui.QUndoStack.setActive`, usually when the associated document window receives focus. The active stack may also be set with :sip:ref:`~PyQt6.QtGui.QUndoGroup.setActiveStack`, and is returned by :sip:ref:`~PyQt6.QtGui.QUndoGroup.activeStack`.

When a stack is added to a group using :sip:ref:`~PyQt6.QtGui.QUndoGroup.addStack`, the group does not take ownership of the stack. This means the stack has to be deleted separately from the group. When a stack is deleted, it is automatically removed from a group. A stack may belong to only one group. Adding it to another group will cause it to be removed from the previous group.

A :sip:ref:`~PyQt6.QtGui.QUndoGroup` is also useful in conjunction with QUndoView. If a QUndoView is set to watch a group using QUndoView::setGroup(), it will update itself to display the active stack.
