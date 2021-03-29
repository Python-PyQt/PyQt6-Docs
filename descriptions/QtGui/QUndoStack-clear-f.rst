.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 10bba72570b0a27eb61bf5eaeb430e45

Clears the command stack by deleting all commands on it, and returns the stack to the clean state.

Commands are not undone or redone; the state of the edited object remains unchanged.

This function is usually used when the contents of the document are abandoned.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QUndoStack`.
