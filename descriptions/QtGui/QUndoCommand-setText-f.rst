.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: 349bc862999a5baea00a4f6fab03cb5a

Sets the command's text to be the *text* specified.

The specified text should be a short user-readable string describing what this command does.

If you need to have two different strings for :sip:ref:`~PyQt6.QtGui.QUndoCommand.text` and :sip:ref:`~PyQt6.QtGui.QUndoCommand.actionText`, separate them with "\\n" and pass into this function. Even if you do not use this feature for English strings during development, you can still let translators use two different strings in order to match specific languages' needs. The described feature and the function :sip:ref:`~PyQt6.QtGui.QUndoCommand.actionText` are available since Qt 4.8.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QUndoCommand.text`, :sip:ref:`~PyQt6.QtGui.QUndoCommand.actionText`, :sip:ref:`~PyQt6.QtGui.QUndoStack.createUndoAction`, :sip:ref:`~PyQt6.QtGui.QUndoStack.createRedoAction`.
