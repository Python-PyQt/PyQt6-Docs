.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: a340e26587f6c19167f675adc4ed0824

Repeatedly calls :sip:ref:`~PyQt6.QtGui.QUndoStack.undo` or :sip:ref:`~PyQt6.QtGui.QUndoStack.redo` until the current command index reaches *idx*. This function can be used to roll the state of the document forwards of backwards. :sip:ref:`~PyQt6.QtGui.QUndoStack.indexChanged` is emitted only once.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QUndoStack.index`, :sip:ref:`~PyQt6.QtGui.QUndoStack.count`, :sip:ref:`~PyQt6.QtGui.QUndoStack.undo`, :sip:ref:`~PyQt6.QtGui.QUndoStack.redo`.
