.. sip:class-description::
    :status: todo
    :brief: Defines a point in the plane using integer precision
    :digest: 6825f12155e020cf116d14a72c28c166

The :sip:ref:`~PyQt6.QtCore.QPoint` class defines a point in the plane using integer precision.

A point is specified by a x coordinate and an y coordinate which can be accessed using the :sip:ref:`~PyQt6.QtCore.QPoint.x` and :sip:ref:`~PyQt6.QtCore.QPoint.y` functions. The :sip:ref:`~PyQt6.QtCore.QPoint.isNull` function returns ``true`` if both x and y are set to 0. The coordinates can be set (or altered) using the :sip:ref:`~PyQt6.QtCore.QPoint.setX` and :sip:ref:`~PyQt6.QtCore.QPoint.setY` functions, or alternatively the rx() and ry() functions which return references to the coordinates (allowing direct manipulation).

Given a point *p*, the following statements are all equivalent:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_tools_qpoint.py
    :lines: 54-58

A :sip:ref:`~PyQt6.QtCore.QPoint` object can also be used as a vector: Addition and subtraction are defined as for vectors (each component is added separately). A :sip:ref:`~PyQt6.QtCore.QPoint` object can also be divided or multiplied by an ``int`` or a ``qreal``.

In addition, the :sip:ref:`~PyQt6.QtCore.QPoint` class provides the :sip:ref:`~PyQt6.QtCore.QPoint.manhattanLength` function which gives an inexpensive approximation of the length of the :sip:ref:`~PyQt6.QtCore.QPoint` object interpreted as a vector. Finally, :sip:ref:`~PyQt6.QtCore.QPoint` objects can be streamed as well as compared.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QPointF`.
