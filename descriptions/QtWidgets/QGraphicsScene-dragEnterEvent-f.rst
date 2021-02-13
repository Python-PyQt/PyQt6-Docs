.. sip:method-description::
    :status: todo
    :pysig: 33e861446b7ae472c03779419970a4fa
    :realsig: (QGraphicsSceneDragDropEvent*)
    :digest: f32bba9d2502ed43a460550f7ce88cce

This event handler, for event *event*, can be reimplemented in a subclass to receive drag enter events for the scene.

The default implementation accepts the event and prepares the scene to accept drag move events.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.dragEnterEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.dragMoveEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.dragLeaveEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.dropEvent`.
