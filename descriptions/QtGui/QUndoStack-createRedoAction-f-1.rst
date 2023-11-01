.. sip:method-description::
    :status: todo
    :pysig: 05541258bf8e6dc08bd067a8d8ee155d
    :realsig: (QObject*, const QString&) const
    :digest: 8545eb95ccfb91dbb56e0bba79fd8760

Creates an redo :sip:ref:`~PyQt6.QtGui.QAction` object with the given *parent*.

Triggering this action will cause a call to :sip:ref:`~PyQt6.QtGui.QUndoStack.redo`. The text of this action is the text of the command which will be redone in the next call to :sip:ref:`~PyQt6.QtGui.QUndoStack.redo`, prefixed by the specified *prefix*. If there is no command available for redo, this action will be disabled.

If *prefix* is empty, the default template "Redo %1" is used instead of prefix. Before Qt 4.8, the prefix "Redo" was used by default.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QUndoStack.createUndoAction`, :sip:ref:`~PyQt6.QtGui.QUndoStack.canRedo`, :sip:ref:`~PyQt6.QtGui.QUndoCommand.text`.
