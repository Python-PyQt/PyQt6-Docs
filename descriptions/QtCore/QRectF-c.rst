.. sip:class-description::
    :status: todo
    :brief: Defines a rectangle in the plane using floating point precision
    :digest: 68f45c51f9ecce5534c58c2412c94be8

The :sip:ref:`~PyQt6.QtCore.QRectF` class defines a rectangle in the plane using floating point precision.

A rectangle is normally expressed as a top-left corner and a size. The size (width and height) of a :sip:ref:`~PyQt6.QtCore.QRectF` is always equivalent to the mathematical rectangle that forms the basis for its rendering.

A :sip:ref:`~PyQt6.QtCore.QRectF` can be constructed with a set of left, top, width and height coordinates, or from a :sip:ref:`~PyQt6.QtCore.QPointF` and a :sip:ref:`~PyQt6.QtCore.QSizeF`. The following code creates two identical rectangles.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_tools_qrect.py
    :lines: 60-61

There is also a third constructor creating a :sip:ref:`~PyQt6.QtCore.QRectF` from a :sip:ref:`~PyQt6.QtCore.QRect`, and a corresponding :sip:ref:`~PyQt6.QtCore.QRectF.toRect` function that returns a :sip:ref:`~PyQt6.QtCore.QRect` object based on the values of this rectangle (note that the coordinates in the returned rectangle are rounded to the nearest integer).

The :sip:ref:`~PyQt6.QtCore.QRectF` class provides a collection of functions that return the various rectangle coordinates, and enable manipulation of these. :sip:ref:`~PyQt6.QtCore.QRectF` also provides functions to move the rectangle relative to the various coordinates. In addition there is a :sip:ref:`~PyQt6.QtCore.QRectF.moveTo` function that moves the rectangle, leaving its top left corner at the given coordinates. Alternatively, the :sip:ref:`~PyQt6.QtCore.QRectF.translate` function moves the rectangle the given offset relative to the current position, and the :sip:ref:`~PyQt6.QtCore.QRectF.translated` function returns a translated copy of this rectangle.

The :sip:ref:`~PyQt6.QtCore.QRectF.size` function returns the rectangle's dimensions as a :sip:ref:`~PyQt6.QtCore.QSizeF`. The dimensions can also be retrieved separately using the :sip:ref:`~PyQt6.QtCore.QRectF.width` and :sip:ref:`~PyQt6.QtCore.QRectF.height` functions. To manipulate the dimensions use the :sip:ref:`~PyQt6.QtCore.QRectF.setSize`, :sip:ref:`~PyQt6.QtCore.QRectF.setWidth` or :sip:ref:`~PyQt6.QtCore.QRectF.setHeight` functions. Alternatively, the size can be changed by applying either of the functions setting the rectangle coordinates, for example, :sip:ref:`~PyQt6.QtCore.QRectF.setBottom` or :sip:ref:`~PyQt6.QtCore.QRectF.setRight`.

The :sip:ref:`~PyQt6.QtCore.QRectF.contains` function tells whether a given point is inside the rectangle or not, and the :sip:ref:`~PyQt6.QtCore.QRectF.intersects` function returns ``true`` if this rectangle intersects with a given rectangle (otherwise false). The :sip:ref:`~PyQt6.QtCore.QRectF` class also provides the :sip:ref:`~PyQt6.QtCore.QRectF.intersected` function which returns the intersection rectangle, and the :sip:ref:`~PyQt6.QtCore.QRectF.united` function which returns the rectangle that encloses the given rectangle and this:

+---------------------------------------------+----------------------------------------+
| |image-qrect-intersect-png|                 | |image-qrect-unite-png|                |
+---------------------------------------------+----------------------------------------+
| :sip:ref:`~PyQt6.QtCore.QRectF.intersected` | :sip:ref:`~PyQt6.QtCore.QRectF.united` |
+---------------------------------------------+----------------------------------------+

The :sip:ref:`~PyQt6.QtCore.QRectF.isEmpty` function returns ``true`` if the rectangle's width or height is less than, or equal to, 0. Note that an empty rectangle is not valid: The :sip:ref:`~PyQt6.QtCore.QRectF.isValid` function returns ``true`` if both width and height is larger than 0. A null rectangle (\ :sip:ref:`~PyQt6.QtCore.QRectF.isNull` == true) on the other hand, has both width and height set to 0.

Note that due to the way :sip:ref:`~PyQt6.QtCore.QRect` and :sip:ref:`~PyQt6.QtCore.QRectF` are defined, an empty :sip:ref:`~PyQt6.QtCore.QRectF` is defined in essentially the same way as :sip:ref:`~PyQt6.QtCore.QRect`.

Finally, :sip:ref:`~PyQt6.QtCore.QRectF` objects can be streamed as well as compared.

.. _qrectf-rendering:

Rendering
---------

When using an :sip:ref:`~PyQt6.QtGui.QPainter.RenderHints.Antialiasing` painter, the boundary line of a :sip:ref:`~PyQt6.QtCore.QRectF` will be rendered symmetrically on both sides of the mathematical rectangle's boundary line. But when using an aliased painter (the default) other rules apply.

Then, when rendering with a one pixel wide pen the :sip:ref:`~PyQt6.QtCore.QRectF`'s boundary line will be rendered to the right and below the mathematical rectangle's boundary line.

When rendering with a two pixels wide pen the boundary line will be split in the middle by the mathematical rectangle. This will be the case whenever the pen is set to an even number of pixels, while rendering with a pen with an odd number of pixels, the spare pixel will be rendered to the right and below the mathematical rectangle as in the one pixel case.

+--------------------------------+----------------------------------+
| |image-qrect-diagram-zero-png| | |image-qrectf-diagram-one-png|   |
+--------------------------------+----------------------------------+
| Logical representation         | One pixel wide pen               |
+--------------------------------+----------------------------------+
| |image-qrectf-diagram-two-png| | |image-qrectf-diagram-three-png| |
+--------------------------------+----------------------------------+
| Two pixel wide pen             | Three pixel wide pen             |
+--------------------------------+----------------------------------+

.. _qrectf-coordinates:

Coordinates
-----------

The :sip:ref:`~PyQt6.QtCore.QRectF` class provides a collection of functions that return the various rectangle coordinates, and enable manipulation of these. :sip:ref:`~PyQt6.QtCore.QRectF` also provides functions to move the rectangle relative to the various coordinates.

For example: the :sip:ref:`~PyQt6.QtCore.QRectF.bottom`, :sip:ref:`~PyQt6.QtCore.QRectF.setBottom` and :sip:ref:`~PyQt6.QtCore.QRectF.moveBottom` functions: :sip:ref:`~PyQt6.QtCore.QRectF.bottom` returns the y-coordinate of the rectangle's bottom edge, :sip:ref:`~PyQt6.QtCore.QRectF.setBottom` sets the bottom edge of the rectangle to the given y coordinate (it may change the height, but will never change the rectangle's top edge) and :sip:ref:`~PyQt6.QtCore.QRectF.moveBottom` moves the entire rectangle vertically, leaving the rectangle's bottom edge at the given y coordinate and its size unchanged.

.. image:: ../../../images/qrectf-coordinates.png

It is also possible to add offsets to this rectangle's coordinates using the :sip:ref:`~PyQt6.QtCore.QRectF.adjust` function, as well as retrieve a new rectangle based on adjustments of the original one using the :sip:ref:`~PyQt6.QtCore.QRectF.adjusted` function. If either of the width and height is negative, use the :sip:ref:`~PyQt6.QtCore.QRectF.normalized` function to retrieve a rectangle where the corners are swapped.

In addition, :sip:ref:`~PyQt6.QtCore.QRectF` provides the :sip:ref:`~PyQt6.QtCore.QRectF.getCoords` function which extracts the position of the rectangle's top-left and bottom-right corner, and the :sip:ref:`~PyQt6.QtCore.QRectF.getRect` function which extracts the rectangle's top-left corner, width and height. Use the :sip:ref:`~PyQt6.QtCore.QRectF.setCoords` and :sip:ref:`~PyQt6.QtCore.QRectF.setRect` function to manipulate the rectangle's coordinates and dimensions in one go.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRect`, :sip:ref:`~PyQt6.QtGui.QRegion`.

.. |image-qrect-intersect-png| image:: ../../../images/qrect-intersect.png
.. |image-qrect-unite-png| image:: ../../../images/qrect-unite.png
.. |image-qrect-diagram-zero-png| image:: ../../../images/qrect-diagram-zero.png
.. |image-qrectf-diagram-one-png| image:: ../../../images/qrectf-diagram-one.png
.. |image-qrectf-diagram-two-png| image:: ../../../images/qrectf-diagram-two.png
.. |image-qrectf-diagram-three-png| image:: ../../../images/qrectf-diagram-three.png
