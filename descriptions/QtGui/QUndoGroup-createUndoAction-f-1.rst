.. sip:method-description::
    :status: todo
    :pysig: 05541258bf8e6dc08bd067a8d8ee155d
    :realsig: (QObject*, const QString&) const
    :digest: 975a8f9caaae41ae2076949362f9dfcc

Creates an undo :sip:ref:`~PyQt6.QtGui.QAction` object with parent *parent*.

Triggering this action will cause a call to :sip:ref:`~PyQt6.QtGui.QUndoStack.undo` on the active stack. The text of this action will always be the text of the command which will be undone in the next call to :sip:ref:`~PyQt6.QtGui.QUndoGroup.undo`, prefixed by *prefix*. If there is no command available for undo, if the group is empty or if none of the stacks are active, this action will be disabled.

If *prefix* is empty, the default template "Undo %1" is used instead of prefix. Before Qt 4.8, the prefix "Undo" was used by default.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QUndoGroup.createRedoAction`, :sip:ref:`~PyQt6.QtGui.QUndoGroup.canUndo`, :sip:ref:`~PyQt6.QtGui.QUndoCommand.text`.
