.. sip:class-description::
    :status: todo
    :brief: The base class of all commands stored on a QUndoStack
    :digest: eaac093d61074dc1f4bc99208371a8f2

The :sip:ref:`~PyQt6.QtGui.QUndoCommand` class is the base class of all commands stored on a :sip:ref:`~PyQt6.QtGui.QUndoStack`.

For an overview of Qt's Undo Framework, see the overview document.

A :sip:ref:`~PyQt6.QtGui.QUndoCommand` represents a single editing action on a document; for example, inserting or deleting a block of text in a text editor. :sip:ref:`~PyQt6.QtGui.QUndoCommand` can apply a change to the document with :sip:ref:`~PyQt6.QtGui.QUndoCommand.redo` and undo the change with :sip:ref:`~PyQt6.QtGui.QUndoCommand.undo`. The implementations for these functions must be provided in a derived class.

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_util_qundostack.py
    :lines: 54-66

A :sip:ref:`~PyQt6.QtGui.QUndoCommand` has an associated :sip:ref:`~PyQt6.QtGui.QUndoCommand.text`. This is a short string describing what the command does. It is used to update the text properties of the stack's undo and redo actions; see :sip:ref:`~PyQt6.QtGui.QUndoStack.createUndoAction` and :sip:ref:`~PyQt6.QtGui.QUndoStack.createRedoAction`.

:sip:ref:`~PyQt6.QtGui.QUndoCommand` objects are owned by the stack they were pushed on. :sip:ref:`~PyQt6.QtGui.QUndoStack` deletes a command if it has been undone and a new command is pushed. For example:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_util_qundostack.py
    :lines: 71-79

In effect, when a command is pushed, it becomes the top-most command on the stack.

To support command compression, :sip:ref:`~PyQt6.QtGui.QUndoCommand` has an :sip:ref:`~PyQt6.QtGui.QUndoCommand.id` and the virtual function :sip:ref:`~PyQt6.QtGui.QUndoCommand.mergeWith`. These functions are used by :sip:ref:`~PyQt6.QtGui.QUndoStack.push`.

To support command macros, a :sip:ref:`~PyQt6.QtGui.QUndoCommand` object can have any number of child commands. Undoing or redoing the parent command will cause the child commands to be undone or redone. A command can be assigned to a parent explicitly in the constructor. In this case, the command will be owned by the parent.

The parent in this case is usually an empty command, in that it doesn't provide its own implementation of :sip:ref:`~PyQt6.QtGui.QUndoCommand.undo` and :sip:ref:`~PyQt6.QtGui.QUndoCommand.redo`. Instead, it uses the base implementations of these functions, which simply call :sip:ref:`~PyQt6.QtGui.QUndoCommand.undo` or :sip:ref:`~PyQt6.QtGui.QUndoCommand.redo` on all its children. The parent should, however, have a meaningful :sip:ref:`~PyQt6.QtGui.QUndoCommand.text`.

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_util_qundostack.py
    :lines: 84-90

Another way to create macros is to use the convenience functions :sip:ref:`~PyQt6.QtGui.QUndoStack.beginMacro` and :sip:ref:`~PyQt6.QtGui.QUndoStack.endMacro`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QUndoStack`.
