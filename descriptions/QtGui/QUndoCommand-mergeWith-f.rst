.. sip:method-description::
    :status: todo
    :pysig: 97c3589bbd6c9e72759dc65d1a2528c2
    :realsig: (const QUndoCommand*)
    :digest: aa32d5b0a654c0e1c937642b5bd19ba3

Attempts to merge this command with *command*. Returns ``true`` on success; otherwise returns ``false``.

If this function returns ``true``, calling this command's :sip:ref:`~PyQt6.QtGui.QUndoCommand.redo` must have the same effect as redoing both this command and *command*. Similarly, calling this command's :sip:ref:`~PyQt6.QtGui.QUndoCommand.undo` must have the same effect as undoing *command* and this command.

:sip:ref:`~PyQt6.QtGui.QUndoStack` will only try to merge two commands if they have the same id, and the id is not -1.

The default implementation returns ``false``.

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_util_qundostack.py
    :lines: 95-101

.. seealso:: :sip:ref:`~PyQt6.QtGui.QUndoCommand.id`, :sip:ref:`~PyQt6.QtGui.QUndoStack.push`.
