.. sip:method-description::
    :status: todo
    :pysig: 3ccfbf74bfd42d69901fa7084cd0dadf
    :realsig: (QObject*,const QString&) const
    :digest: f3e7cbf9aa0797e618312b554c649f1a

Creates an redo :sip:ref:`~PyQt6.QtGui.QAction` object with parent *parent*.

Triggering this action will cause a call to :sip:ref:`~PyQt6.QtGui.QUndoStack.redo` on the active stack. The text of this action will always be the text of the command which will be redone in the next call to :sip:ref:`~PyQt6.QtGui.QUndoGroup.redo`, prefixed by *prefix*. If there is no command available for redo, if the group is empty or if none of the stacks are active, this action will be disabled.

If *prefix* is empty, the default template "Redo %1" is used instead of prefix. Before Qt 4.8, the prefix "Redo" was used by default.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QUndoGroup.createUndoAction`, :sip:ref:`~PyQt6.QtGui.QUndoGroup.canRedo`, :sip:ref:`~PyQt6.QtGui.QUndoCommand.text`.
