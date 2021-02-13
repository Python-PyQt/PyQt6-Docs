.. sip:method-description::
    :status: todo
    :pysig: a235380dae053a444e232e705dfb65db
    :realsig: (QGraphicsSceneHoverEvent*)
    :digest: eaacae197ccbbe5646df6c607c7c6885

This event handler, for event *event*, can be reimplemented to receive hover enter events for this item. The default implementation calls :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.update`; otherwise it does nothing.

Calling :sip:ref:`~PyQt6.QtCore.QEvent.ignore` or :sip:ref:`~PyQt6.QtCore.QEvent.accept` on *event* has no effect.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.hoverMoveEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.hoverLeaveEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.sceneEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setAcceptHoverEvents`.
