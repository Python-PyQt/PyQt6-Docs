.. sip:method-description::
    :status: todo
    :pysig: 8bf118a1d075182fcf054b0a246e123f
    :realsig: (QGraphicsSceneMouseEvent*)
    :digest: 715897ceffa782c2a0e10fae394a7742

This event handler, for event *mouseEvent*, can be reimplemented in a subclass to receive mouse doubleclick events for the scene.

If someone doubleclicks on the scene, the scene will first receive a mouse press event, followed by a release event (i.e., a click), then a doubleclick event, and finally a release event. If the doubleclick event is delivered to a different item than the one that received the first press and release, it will be delivered as a press event. However, tripleclick events are not delivered as doubleclick events in this case.

The default implementation is similar to :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.mousePressEvent`.

Note: See :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.items` for a definition of which items are considered visible by this function.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mousePressEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mouseMoveEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mouseReleaseEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setAcceptedMouseButtons`.
