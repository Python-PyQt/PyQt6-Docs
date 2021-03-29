.. sip:method-description::
    :status: todo
    :pysig: 9abaad72cdbc83a19b4f050568cfc758
    :realsig: (QTextDocument::Stacks)
    :digest: c3f2335363ae78d4b18084ddb6ee5fda

Clears the stacks specified by *stacksToClear*.

This method clears any commands on the undo stack, the redo stack, or both (the default). If commands are cleared, the appropriate signals are emitted, :sip:ref:`~PyQt6.QtGui.QTextDocument.undoAvailable` or :sip:ref:`~PyQt6.QtGui.QTextDocument.redoAvailable`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextDocument.undoAvailable`, :sip:ref:`~PyQt6.QtGui.QTextDocument.redoAvailable`.
