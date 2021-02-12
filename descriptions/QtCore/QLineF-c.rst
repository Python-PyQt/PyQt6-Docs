.. sip:class-description::
    :status: todo
    :brief: Two-dimensional vector using floating point precision
    :digest: 9b6c340e65ded3f7dbc140fa08543816

The :sip:ref:`~PyQt6.QtCore.QLineF` class provides a two-dimensional vector using floating point precision.

A :sip:ref:`~PyQt6.QtCore.QLineF` describes a finite length line (or line segment) on a two-dimensional surface. :sip:ref:`~PyQt6.QtCore.QLineF` defines the start and end points of the line using floating point accuracy for coordinates. Use the :sip:ref:`~PyQt6.QtCore.QLineF.toLine` function to retrieve an integer based copy of this line.

+-------------------------+-------------------------------+
| |image-qline-point-png| | |image-qline-coordinates-png| |
+-------------------------+-------------------------------+

The positions of the line's start and end points can be retrieved using the :sip:ref:`~PyQt6.QtCore.QLineF.p1`, :sip:ref:`~PyQt6.QtCore.QLineF.x1`, :sip:ref:`~PyQt6.QtCore.QLineF.y1`, :sip:ref:`~PyQt6.QtCore.QLineF.p2`, :sip:ref:`~PyQt6.QtCore.QLineF.x2`, and :sip:ref:`~PyQt6.QtCore.QLineF.y2` functions. The :sip:ref:`~PyQt6.QtCore.QLineF.dx` and :sip:ref:`~PyQt6.QtCore.QLineF.dy` functions return the horizontal and vertical components of the line, respectively.

The line's length can be retrieved using the :sip:ref:`~PyQt6.QtCore.QLineF.length` function, and altered using the :sip:ref:`~PyQt6.QtCore.QLineF.setLength` function. Similarly, :sip:ref:`~PyQt6.QtCore.QLineF.angle` and :sip:ref:`~PyQt6.QtCore.QLineF.setAngle` are respectively used for retrieving and altering the angle of the line. Use the :sip:ref:`~PyQt6.QtCore.QLineF.isNull` function to determine whether the :sip:ref:`~PyQt6.QtCore.QLineF` represents a valid line or a null line.

The :sip:ref:`~PyQt6.QtCore.QLineF.intersects` function determines the :sip:ref:`~PyQt6.QtCore.QLineF.IntersectionType.IntersectionType` for this line and a given line, while the :sip:ref:`~PyQt6.QtCore.QLineF.angleTo` function returns the angle between the lines. In addition, the :sip:ref:`~PyQt6.QtCore.QLineF.unitVector` function returns a line that has the same starting point as this line, but with a length of only 1, while the :sip:ref:`~PyQt6.QtCore.QLineF.normalVector` function returns a line that is perpendicular to this line with the same starting point and length.

Finally, the line can be translated a given offset using the :sip:ref:`~PyQt6.QtCore.QLineF.translate` function, and can be traversed using the :sip:ref:`~PyQt6.QtCore.QLineF.pointAt` function.

.. _qlinef-constraints:

Constraints
-----------

:sip:ref:`~PyQt6.QtCore.QLine` is limited to the minimum and maximum values for the ``int`` type. Operations on a :sip:ref:`~PyQt6.QtCore.QLine` that could potentially result in values outside this range will result in undefined behavior.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLine`, :sip:ref:`~PyQt6.QtCore.QRectF`.

.. |image-qline-point-png| image:: ../../../images/qline-point.png
.. |image-qline-coordinates-png| image:: ../../../images/qline-coordinates.png
