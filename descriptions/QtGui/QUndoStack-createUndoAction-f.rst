.. sip:method-description::
    :status: todo
    :pysig: 3ccfbf74bfd42d69901fa7084cd0dadf
    :realsig: (QObject*,const QString&) const
    :digest: 85b541bc38aaa6958a5ae134dafbb1cc

Creates an undo :sip:ref:`~PyQt6.QtGui.QAction` object with the given *parent*.

Triggering this action will cause a call to :sip:ref:`~PyQt6.QtGui.QUndoStack.undo`. The text of this action is the text of the command which will be undone in the next call to :sip:ref:`~PyQt6.QtGui.QUndoStack.undo`, prefixed by the specified *prefix*. If there is no command available for undo, this action will be disabled.

If *prefix* is empty, the default template "Undo %1" is used instead of prefix. Before Qt 4.8, the prefix "Undo" was used by default.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QUndoStack.createRedoAction`, :sip:ref:`~PyQt6.QtGui.QUndoStack.canUndo`, :sip:ref:`~PyQt6.QtGui.QUndoCommand.text`.
