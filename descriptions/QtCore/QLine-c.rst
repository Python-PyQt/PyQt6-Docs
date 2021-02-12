.. sip:class-description::
    :status: todo
    :brief: Two-dimensional vector using integer precision
    :digest: 0419514203796dd8736d738d5782bab8

The :sip:ref:`~PyQt6.QtCore.QLine` class provides a two-dimensional vector using integer precision.

A :sip:ref:`~PyQt6.QtCore.QLine` describes a finite length line (or a line segment) on a two-dimensional surface. The start and end points of the line are specified using integer point accuracy for coordinates. Use the :sip:ref:`~PyQt6.QtCore.QLineF` constructor to retrieve a floating point copy.

+-------------------------+-------------------------------+
| |image-qline-point-png| | |image-qline-coordinates-png| |
+-------------------------+-------------------------------+

The positions of the line's start and end points can be retrieved using the :sip:ref:`~PyQt6.QtCore.QLine.p1`, :sip:ref:`~PyQt6.QtCore.QLine.x1`, :sip:ref:`~PyQt6.QtCore.QLine.y1`, :sip:ref:`~PyQt6.QtCore.QLine.p2`, :sip:ref:`~PyQt6.QtCore.QLine.x2`, and :sip:ref:`~PyQt6.QtCore.QLine.y2` functions. The :sip:ref:`~PyQt6.QtCore.QLine.dx` and :sip:ref:`~PyQt6.QtCore.QLine.dy` functions return the horizontal and vertical components of the line. Use :sip:ref:`~PyQt6.QtCore.QLine.isNull` to determine whether the :sip:ref:`~PyQt6.QtCore.QLine` represents a valid line or a null line.

Finally, the line can be translated a given offset using the :sip:ref:`~PyQt6.QtCore.QLine.translate` function.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLineF`, :sip:ref:`~PyQt6.QtCore.QRect`.

.. |image-qline-point-png| image:: ../../../images/qline-point.png
.. |image-qline-coordinates-png| image:: ../../../images/qline-coordinates.png
