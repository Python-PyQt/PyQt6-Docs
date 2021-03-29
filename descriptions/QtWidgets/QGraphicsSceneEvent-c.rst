.. sip:class-description::
    :status: todo
    :brief: Base class for all graphics view related events
    :digest: 87cad3309856202d634a93b3f558c645

The :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneEvent` class provides a base class for all graphics view related events.

When a :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` receives Qt mouse, keyboard, and drag and drop events (\ :sip:ref:`~PyQt6.QtGui.QMouseEvent`, :sip:ref:`~PyQt6.QtGui.QKeyEvent`, QDragEvent, etc.), it translates them into instances of :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneEvent` subclasses and forwards them to the :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` it displays. The scene then forwards the events to the relevant items.

For example, when a :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` receives a :sip:ref:`~PyQt6.QtGui.QMouseEvent` of type MousePress as a response to a user click, the view sends a :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneMouseEvent` of type :sip:ref:`~PyQt6.QtCore.QEvent.Type.GraphicsSceneMousePress` to the underlying :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` through its :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.mousePressEvent` function. The default :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.mousePressEvent` implementation determines which item was clicked and forwards the event to :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.mousePressEvent`.

Subclasses such as :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneMouseEvent` and :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneContextMenuEvent` provide the coordinates from the original :sip:ref:`~PyQt6.QtCore.QEvent` in screen, scene, and item coordinates (see :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneMouseEvent.screenPos`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneMouseEvent.scenePos`, and :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneMouseEvent.pos`). The item coordinates are set by the :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` before it forwards the event to the event to a :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`. The mouse events also add the possibility to retrieve the coordinates from the last event received by the view (see :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneMouseEvent.lastScreenPos`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneMouseEvent.lastScenePos`, and :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneMouseEvent.lastPos`).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QEvent`.
