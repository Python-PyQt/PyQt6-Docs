.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: ccc39beeb73371a86b4312eb76d72658

Returns ``true`` if there is a command available for undo; otherwise returns ``false``.

This function returns ``false`` if the stack is empty, or if the bottom command on the stack has already been undone.

Synonymous with :sip:ref:`~PyQt6.QtGui.QUndoStack.index` == 0.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QUndoStack.index`, :sip:ref:`~PyQt6.QtGui.QUndoStack.canRedo`.
