.. sip:class-description::
    :status: todo
    :brief: Mouse events in the graphics view framework
    :digest: 12ce9a15ac16d0fb8f884828a145888f

The :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneMouseEvent` class provides mouse events in the graphics view framework.

When a :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` receives a :sip:ref:`~PyQt6.QtGui.QMouseEvent`, it translates it to a :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneMouseEvent`. The event is then forwarded to the :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` associated with the view. If the event is not handled by the scene, the view may use it, e.g., for the :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.DragMode`.

In addition to containing the item, scene, and screen coordinates of the event (as :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneMouseEvent.pos`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneMouseEvent.scenePos`, and :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneMouseEvent.screenPos`), mouse events also contain the coordinates of the previous mouse event received by the view. These can be retrieved with :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneMouseEvent.lastPos`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneMouseEvent.lastScreenPos`, and :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneMouseEvent.lastScenePos`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneContextMenuEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneHoverEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneWheelEvent`, :sip:ref:`~PyQt6.QtGui.QMouseEvent`.
