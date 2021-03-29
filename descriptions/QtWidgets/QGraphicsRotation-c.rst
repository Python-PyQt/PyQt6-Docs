.. sip:class-description::
    :status: todo
    :brief: Rotation transformation around a given axis
    :digest: 07ff1aba38cd82f735f4a01da41fdabd

The :sip:ref:`~PyQt6.QtWidgets.QGraphicsRotation` class provides a rotation transformation around a given axis.

You can provide the desired axis by assigning a :sip:ref:`~PyQt6.QtGui.QVector3D` to the axis property or by passing a member if :sip:ref:`~PyQt6.QtCore.Qt.Axis` to the :sip:ref:`~PyQt6.QtWidgets.QGraphicsRotation.setAxis` convenience function. By default the axis is (0, 0, 1) i.e., rotation around the Z axis.

The angle property, which is provided by :sip:ref:`~PyQt6.QtWidgets.QGraphicsRotation`, now describes the number of degrees to rotate around this axis.

:sip:ref:`~PyQt6.QtWidgets.QGraphicsRotation` provides certain parameters to help control how the rotation should be applied.

The origin is the point that the item is rotated around (i.e., it stays fixed relative to the parent as the rest of the item is rotated). By default the origin is :sip:ref:`~PyQt6.QtCore.QPointF`\ (0, 0).

The angle property provides the number of degrees to rotate the item clockwise around the origin. This value also be negative, indicating a counter-clockwise rotation. For animation purposes it may also be useful to provide rotation angles exceeding (-360, 360) degrees, for instance to animate how an item rotates several times.

Note: the final rotation is the combined effect of a rotation in 3D space followed by a projection back to 2D. If several rotations are performed in succession, they will not behave as expected unless they were all around the Z axis.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsTransform`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setRotation`, :sip:ref:`~PyQt6.QtGui.QTransform.rotate`.
