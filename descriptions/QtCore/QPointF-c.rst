.. sip:class-description::
    :status: todo
    :brief: Defines a point in the plane using floating point precision
    :digest: d973bc83ca914b5d07173301693f8e45

The :sip:ref:`~PyQt6.QtCore.QPointF` class defines a point in the plane using floating point precision.

A point is specified by a x coordinate and an y coordinate which can be accessed using the :sip:ref:`~PyQt6.QtCore.QPointF.x` and :sip:ref:`~PyQt6.QtCore.QPointF.y` functions. The coordinates of the point are specified using floating point numbers for accuracy. The :sip:ref:`~PyQt6.QtCore.QPointF.isNull` function returns ``true`` if both x and y are set to 0.0. The coordinates can be set (or altered) using the :sip:ref:`~PyQt6.QtCore.QPointF.setX` and :sip:ref:`~PyQt6.QtCore.QPointF.setY` functions, or alternatively the rx() and ry() functions which return references to the coordinates (allowing direct manipulation).

Given a point *p*, the following statements are all equivalent:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_tools_qpoint.py
    :lines: 125-129

A :sip:ref:`~PyQt6.QtCore.QPointF` object can also be used as a vector: Addition and subtraction are defined as for vectors (each component is added separately). A :sip:ref:`~PyQt6.QtCore.QPointF` object can also be divided or multiplied by an ``int`` or a ``qreal``.

In addition, the :sip:ref:`~PyQt6.QtCore.QPointF` class provides a constructor converting a :sip:ref:`~PyQt6.QtCore.QPoint` object into a :sip:ref:`~PyQt6.QtCore.QPointF` object, and a corresponding :sip:ref:`~PyQt6.QtCore.QPointF.toPoint` function which returns a :sip:ref:`~PyQt6.QtCore.QPoint` copy of *this* point. Finally, :sip:ref:`~PyQt6.QtCore.QPointF` objects can be streamed as well as compared.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QPoint`, :sip:ref:`~PyQt6.QtGui.QPolygonF`.
