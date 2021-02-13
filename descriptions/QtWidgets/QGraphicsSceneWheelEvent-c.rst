.. sip:class-description::
    :status: todo
    :brief: Wheel events in the graphics view framework
    :digest: 9fdbd517b2f28fbaa2e534a161cea200

The :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneWheelEvent` class provides wheel events in the graphics view framework.

The :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneWheelEvent` class provides wheel events in the graphics view framework.

:sip:ref:`~PyQt6.QtGui.QWheelEvent`\ s received by a :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` are translated into QGraphicsSceneWheelEvents; it translates the QWheelEvent::globalPos() into item, scene, and screen coordinates (\ :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneWheelEvent.pos`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneWheelEvent.scenePos`, and :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneWheelEvent.screenPos`).

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneMouseEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneContextMenuEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneHoverEvent`, :sip:ref:`~PyQt6.QtGui.QWheelEvent`.
