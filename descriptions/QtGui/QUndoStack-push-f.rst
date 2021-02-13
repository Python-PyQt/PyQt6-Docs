.. sip:method-description::
    :status: todo
    :pysig: 714025b49a3fd5db9d8147afb816769e
    :realsig: (QUndoCommand*)
    :digest: 21b0d65e733385f210a3ff2791e5d729

Pushes *cmd* on the stack or merges it with the most recently executed command. In either case, executes *cmd* by calling its :sip:ref:`~PyQt6.QtGui.QUndoStack.redo` function.

If *cmd*'s id is not -1, and if the id is the same as that of the most recently executed command, :sip:ref:`~PyQt6.QtGui.QUndoStack` will attempt to merge the two commands by calling :sip:ref:`~PyQt6.QtGui.QUndoCommand.mergeWith` on the most recently executed command. If :sip:ref:`~PyQt6.QtGui.QUndoCommand.mergeWith` returns ``true``, *cmd* is deleted.

After calling :sip:ref:`~PyQt6.QtGui.QUndoCommand.redo` and, if applicable, :sip:ref:`~PyQt6.QtGui.QUndoCommand.mergeWith`, :sip:ref:`~PyQt6.QtGui.QUndoCommand.isObsolete` will be called for *cmd* or the merged command. If :sip:ref:`~PyQt6.QtGui.QUndoCommand.isObsolete` returns ``true``, then *cmd* or the merged command will be deleted from the stack.

In all other cases *cmd* is simply pushed on the stack.

If commands were undone before *cmd* was pushed, the current command and all commands above it are deleted. Hence *cmd* always ends up being the top-most on the stack.

Once a command is pushed, the stack takes ownership of it. There are no getters to return the command, since modifying it after it has been executed will almost always lead to corruption of the document's state.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QUndoCommand.id`, :sip:ref:`~PyQt6.QtGui.QUndoCommand.mergeWith`.
