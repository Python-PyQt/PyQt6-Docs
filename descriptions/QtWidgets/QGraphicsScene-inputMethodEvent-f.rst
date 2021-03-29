.. sip:method-description::
    :status: todo
    :pysig: 1892efa11dcd6bbbb9a3c11f9e2fe516
    :realsig: (QInputMethodEvent*)
    :digest: 9bde03c133c5ed710030eb98becd5e7e

This event handler, for event *event*, can be reimplemented in a subclass to receive input method events for the scene.

The default implementation forwards the event to the :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.focusItem`. If no item currently has focus or the current focus item does not accept input methods, this function does nothing.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.inputMethodEvent`.
