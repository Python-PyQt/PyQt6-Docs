.. sip:method-description::
    :status: todo
    :pysig: 0a375e310abdbc97200cfcaf02680cd4
    :realsig: (QUndoStack*)
    :digest: 65ae3611a1099ca9a297d11d8569c795

Sets the stack displayed by this view to *stack*. If *stack* is ``nullptr``, the view will be empty.

If the view was previously looking at a :sip:ref:`~PyQt6.QtGui.QUndoGroup`, the group is set to ``nullptr``.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QUndoView.stack`, :sip:ref:`~PyQt6.QtWidgets.QUndoView.setGroup`.
