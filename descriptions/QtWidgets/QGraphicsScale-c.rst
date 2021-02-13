.. sip:class-description::
    :status: todo
    :brief: Scale transformation
    :digest: 20bdc21d04a66fe97488c353fea54cde

The :sip:ref:`~PyQt6.QtWidgets.QGraphicsScale` class provides a scale transformation.

:sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` provides certain parameters to help control how the scale should be applied.

The origin is the point that the item is scaled from (i.e., it stays fixed relative to the parent as the rest of the item grows). By default the origin is :sip:ref:`~PyQt6.QtCore.QPointF`\ (0, 0).

The parameters :sip:ref:`~PyQt6.QtWidgets.QGraphicsScale.xScale`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScale.yScale`, and :sip:ref:`~PyQt6.QtWidgets.QGraphicsScale.zScale` describe the scale factors to apply in horizontal, vertical, and depth directions. They can take on any value, including 0 (to collapse the item to a point) or negative value. A negative :sip:ref:`~PyQt6.QtWidgets.QGraphicsScale.xScale` value will mirror the item horizontally. A negative :sip:ref:`~PyQt6.QtWidgets.QGraphicsScale.yScale` value will flip the item vertically. A negative :sip:ref:`~PyQt6.QtWidgets.QGraphicsScale.zScale` will flip the item end for end.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsTransform`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setScale`, :sip:ref:`~PyQt6.QtGui.QTransform.scale`.
