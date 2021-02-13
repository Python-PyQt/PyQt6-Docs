.. sip:class-description::
    :status: todo
    :brief: Events for widget moving in the graphics view framework
    :digest: 65c9a609efac16b0834f95a8fcf3927d

The :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneMoveEvent` class provides events for widget moving in the graphics view framework.

A `QGraphicsWidget <https://doc.qt.io/qt-6/graphicsview.html#qgraphicswidget>`_ sends itself a :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneMoveEvent` immediately when its local position changes. The delivery is implemented as part of :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.itemChange`.

It's similar to :sip:ref:`~PyQt6.QtGui.QMoveEvent`, but its positions, :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneMoveEvent.oldPos` and :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneMoveEvent.newPos`, use :sip:ref:`~PyQt6.QtCore.QPointF` instead of :sip:ref:`~PyQt6.QtCore.QPoint`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setPos`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemPositionChange`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemPositionHasChanged`.
