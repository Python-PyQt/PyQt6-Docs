.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: 5fe4f3202b1ea1a51cbfa233486f1430

Begins composition of a macro command with the given *text* description.

An empty command described by the specified *text* is pushed on the stack. Any subsequent commands pushed on the stack will be appended to the empty command's children until :sip:ref:`~PyQt6.QtGui.QUndoStack.endMacro` is called.

Calls to  and :sip:ref:`~PyQt6.QtGui.QUndoStack.endMacro` may be nested, but every call to  must have a matching call to :sip:ref:`~PyQt6.QtGui.QUndoStack.endMacro`.

While a macro is being composed, the stack is disabled. This means that:

* :sip:ref:`~PyQt6.QtGui.QUndoStack.indexChanged` and :sip:ref:`~PyQt6.QtGui.QUndoStack.cleanChanged` are not emitted,

* :sip:ref:`~PyQt6.QtGui.QUndoStack.canUndo` and :sip:ref:`~PyQt6.QtGui.QUndoStack.canRedo` return false,

* calling :sip:ref:`~PyQt6.QtGui.QUndoStack.undo` or :sip:ref:`~PyQt6.QtGui.QUndoStack.redo` has no effect,

* the undo/redo actions are disabled.

The stack becomes enabled and appropriate signals are emitted when :sip:ref:`~PyQt6.QtGui.QUndoStack.endMacro` is called for the outermost macro.

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_util_qundostack.py
    :lines: 106-109

This code is equivalent to:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_util_qundostack.py
    :lines: 114-120

.. seealso:: :sip:ref:`~PyQt6.QtGui.QUndoStack.endMacro`.
