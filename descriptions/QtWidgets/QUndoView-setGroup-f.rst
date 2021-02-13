.. sip:method-description::
    :status: todo
    :pysig: 8c98c94bb0306aea6ad7a366d878dfb3
    :realsig: (QUndoGroup*)
    :digest: 90005dd668cff812153be77a86620a3b

Sets the group displayed by this view to *group*. If *group* is ``nullptr``, the view will be empty.

The view will update itself automatically whenever the active stack of the group changes.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QUndoView.group`, :sip:ref:`~PyQt6.QtWidgets.QUndoView.setStack`.
