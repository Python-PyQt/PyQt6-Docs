.. sip:method-description::
    :status: todo
    :pysig: a235380dae053a444e232e705dfb65db
    :realsig: (QGraphicsSceneHoverEvent*)
    :digest: 612278a1c89a15f71b5c5f58859d12b2

This event handler, for event *event*, can be reimplemented to receive hover move events for this item. The default implementation does nothing.

Calling :sip:ref:`~PyQt6.QtCore.QEvent.ignore` or :sip:ref:`~PyQt6.QtCore.QEvent.accept` on *event* has no effect.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.hoverEnterEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.hoverLeaveEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.sceneEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setAcceptHoverEvents`.
