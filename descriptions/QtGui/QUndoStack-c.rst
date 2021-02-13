.. sip:class-description::
    :status: todo
    :brief: Stack of QUndoCommand objects
    :digest: c0f0ca5b1c38e5f8b9237043e91fdbfa

The :sip:ref:`~PyQt6.QtGui.QUndoStack` class is a stack of :sip:ref:`~PyQt6.QtGui.QUndoCommand` objects.

For an overview of Qt's Undo Framework, see the overview document.

An undo stack maintains a stack of commands that have been applied to a document.

New commands are pushed on the stack using :sip:ref:`~PyQt6.QtGui.QUndoStack.push`. Commands can be undone and redone using :sip:ref:`~PyQt6.QtGui.QUndoStack.undo` and :sip:ref:`~PyQt6.QtGui.QUndoStack.redo`, or by triggering the actions returned by :sip:ref:`~PyQt6.QtGui.QUndoStack.createUndoAction` and :sip:ref:`~PyQt6.QtGui.QUndoStack.createRedoAction`.

:sip:ref:`~PyQt6.QtGui.QUndoStack` keeps track of the *current* command. This is the command which will be executed by the next call to :sip:ref:`~PyQt6.QtGui.QUndoStack.redo`. The index of this command is returned by :sip:ref:`~PyQt6.QtGui.QUndoStack.index`. The state of the edited object can be rolled forward or back using :sip:ref:`~PyQt6.QtGui.QUndoStack.setIndex`. If the top-most command on the stack has already been redone, :sip:ref:`~PyQt6.QtGui.QUndoStack.index` is equal to :sip:ref:`~PyQt6.QtGui.QUndoStack.count`.

:sip:ref:`~PyQt6.QtGui.QUndoStack` provides support for undo and redo actions, command compression, command macros, and supports the concept of a *clean state*.

.. _qundostack-undo-and-redo-actions:

Undo and Redo Actions
---------------------

:sip:ref:`~PyQt6.QtGui.QUndoStack` provides convenient undo and redo :sip:ref:`~PyQt6.QtGui.QAction` objects, which can be inserted into a menu or a toolbar. When commands are undone or redone, :sip:ref:`~PyQt6.QtGui.QUndoStack` updates the text properties of these actions to reflect what change they will trigger. The actions are also disabled when no command is available for undo or redo. These actions are returned by :sip:ref:`~PyQt6.QtGui.QUndoStack.createUndoAction` and :sip:ref:`~PyQt6.QtGui.QUndoStack.createRedoAction`.

.. _qundostack-command-compression-and-macros:

Command Compression and Macros
------------------------------

Command compression is useful when several commands can be compressed into a single command that can be undone and redone in a single operation. For example, when a user types a character in a text editor, a new command is created. This command inserts the character into the document at the cursor position. However, it is more convenient for the user to be able to undo or redo typing of whole words, sentences, or paragraphs. Command compression allows these single-character commands to be merged into a single command which inserts or deletes sections of text. For more information, see :sip:ref:`~PyQt6.QtGui.QUndoCommand.mergeWith` and :sip:ref:`~PyQt6.QtGui.QUndoStack.push`.

A command macro is a sequence of commands, all of which are undone and redone in one go. Command macros are created by giving a command a list of child commands. Undoing or redoing the parent command will cause the child commands to be undone or redone. Command macros may be created explicitly by specifying a parent in the :sip:ref:`~PyQt6.QtGui.QUndoCommand` constructor, or by using the convenience functions :sip:ref:`~PyQt6.QtGui.QUndoStack.beginMacro` and :sip:ref:`~PyQt6.QtGui.QUndoStack.endMacro`.

Although command compression and macros appear to have the same effect to the user, they often have different uses in an application. Commands that perform small changes to a document may be usefully compressed if there is no need to individually record them, and if only larger changes are relevant to the user. However, for commands that need to be recorded individually, or those that cannot be compressed, it is useful to use macros to provide a more convenient user experience while maintaining a record of each command.

.. _qundostack-clean-state:

Clean State
-----------

:sip:ref:`~PyQt6.QtGui.QUndoStack` supports the concept of a clean state. When the document is saved to disk, the stack can be marked as clean using :sip:ref:`~PyQt6.QtGui.QUndoStack.setClean`. Whenever the stack returns to this state through undoing and redoing commands, it emits the signal :sip:ref:`~PyQt6.QtGui.QUndoStack.cleanChanged`. This signal is also emitted when the stack leaves the clean state. This signal is usually used to enable and disable the save actions in the application, and to update the document's title to reflect that it contains unsaved changes.

.. _qundostack-obsolete-commands:

Obsolete Commands
-----------------

:sip:ref:`~PyQt6.QtGui.QUndoStack` is able to delete commands from the stack if the command is no longer needed. One example may be to delete a command when two commands are merged together in such a way that the merged command has no function. This can be seen with move commands where the user moves their mouse to one part of the screen and then moves it to the original position. The merged command results in a mouse movement of 0. This command can be deleted since it serves no purpose. Another example is with networking commands that fail due to connection issues. In this case, the command is to be removed from the stack because the :sip:ref:`~PyQt6.QtGui.QUndoStack.redo` and :sip:ref:`~PyQt6.QtGui.QUndoStack.undo` functions have no function since there was connection issues.

A command can be marked obsolete with the :sip:ref:`~PyQt6.QtGui.QUndoCommand.setObsolete` function. The :sip:ref:`~PyQt6.QtGui.QUndoCommand.isObsolete` flag is checked in :sip:ref:`~PyQt6.QtGui.QUndoStack.push`, :sip:ref:`~PyQt6.QtGui.QUndoStack.undo`, :sip:ref:`~PyQt6.QtGui.QUndoStack.redo`, and :sip:ref:`~PyQt6.QtGui.QUndoStack.setIndex` after calling :sip:ref:`~PyQt6.QtGui.QUndoCommand.undo`, :sip:ref:`~PyQt6.QtGui.QUndoCommand.redo` and :sip:ref:`~PyQt6.QtGui.QUndoCommand`:mergeWith() where applicable.

If a command is set obsolete and the clean index is greater than or equal to the current command index, then the clean index will be reset when the command is deleted from the stack.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QUndoCommand`.
