.. sip:method-description::
    :status: todo
    :pysig: f4cc248e69b68bdc7c94b43874d7b9bd
    :realsig: (QTextCursor*)
    :digest: 4ff278b7d3adcd5b7a5af65497839406

Undoes the last editing operation on the document if undo is available. The provided *cursor* is positioned at the end of the location where the edition operation was undone.

See the Qt Undo Framework documentation for details.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextDocument.undoAvailable`, :sip:ref:`~PyQt6.QtGui.QTextDocument.isUndoRedoEnabled`.
