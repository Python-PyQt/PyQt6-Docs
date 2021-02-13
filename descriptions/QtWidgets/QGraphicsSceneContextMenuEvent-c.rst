.. sip:class-description::
    :status: todo
    :brief: Context menu events in the graphics view framework
    :digest: e0e5ff64ee67ba8d0e59a75e55408210

The :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneContextMenuEvent` class provides context menu events in the graphics view framework.

A :sip:ref:`~PyQt6.QtGui.QContextMenuEvent` received by a :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` is translated into a :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneContextMenuEvent`. The :sip:ref:`~PyQt6.QtGui.QContextMenuEvent.globalPos` is translated into item, scene, and screen coordinates (\ :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneContextMenuEvent.pos`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneContextMenuEvent.scenePos`, and :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneContextMenuEvent.screenPos`).

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneMouseEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneWheelEvent`, :sip:ref:`~PyQt6.QtGui.QContextMenuEvent`.
