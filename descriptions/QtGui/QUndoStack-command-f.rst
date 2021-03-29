.. sip:method-description::
    :status: todo
    :pysig: 1b2a91103fa6befe8ec4e043fc45524c
    :realsig: (int) const
    :digest: 97e162122e01843bed2467ceba7f40c1

Returns a const pointer to the command at *index*.

This function returns a const pointer, because modifying a command, once it has been pushed onto the stack and executed, almost always causes corruption of the state of the document, if the command is later undone or redone.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QUndoCommand.child`.
