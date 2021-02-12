.. sip:class-description::
    :status: todo
    :brief: Defines a rectangle in the plane using integer precision
    :digest: 31759c55ebe99a60ee7ae6a52e32cc6b

The :sip:ref:`~PyQt6.QtCore.QRect` class defines a rectangle in the plane using integer precision.

A rectangle is normally expressed as a top-left corner and a size. The size (width and height) of a :sip:ref:`~PyQt6.QtCore.QRect` is always equivalent to the mathematical rectangle that forms the basis for its rendering.

A :sip:ref:`~PyQt6.QtCore.QRect` can be constructed with a set of left, top, width and height integers, or from a :sip:ref:`~PyQt6.QtCore.QPoint` and a :sip:ref:`~PyQt6.QtCore.QSize`. The following code creates two identical rectangles.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_tools_qrect.py
    :lines: 54-55

There is a third constructor that creates a :sip:ref:`~PyQt6.QtCore.QRect` using the top-left and bottom-right coordinates, but we recommend that you avoid using it. The rationale is that for historical reasons the values returned by the :sip:ref:`~PyQt6.QtCore.QRect.bottom` and :sip:ref:`~PyQt6.QtCore.QRect.right` functions deviate from the true bottom-right corner of the rectangle.

The :sip:ref:`~PyQt6.QtCore.QRect` class provides a collection of functions that return the various rectangle coordinates, and enable manipulation of these. :sip:ref:`~PyQt6.QtCore.QRect` also provides functions to move the rectangle relative to the various coordinates. In addition there is a :sip:ref:`~PyQt6.QtCore.QRect.moveTo` function that moves the rectangle, leaving its top left corner at the given coordinates. Alternatively, the :sip:ref:`~PyQt6.QtCore.QRect.translate` function moves the rectangle the given offset relative to the current position, and the :sip:ref:`~PyQt6.QtCore.QRect.translated` function returns a translated copy of this rectangle.

The :sip:ref:`~PyQt6.QtCore.QRect.size` function returns the rectangle's dimensions as a :sip:ref:`~PyQt6.QtCore.QSize`. The dimensions can also be retrieved separately using the :sip:ref:`~PyQt6.QtCore.QRect.width` and :sip:ref:`~PyQt6.QtCore.QRect.height` functions. To manipulate the dimensions use the :sip:ref:`~PyQt6.QtCore.QRect.setSize`, :sip:ref:`~PyQt6.QtCore.QRect.setWidth` or :sip:ref:`~PyQt6.QtCore.QRect.setHeight` functions. Alternatively, the size can be changed by applying either of the functions setting the rectangle coordinates, for example, :sip:ref:`~PyQt6.QtCore.QRect.setBottom` or :sip:ref:`~PyQt6.QtCore.QRect.setRight`.

The :sip:ref:`~PyQt6.QtCore.QRect.contains` function tells whether a given point is inside the rectangle or not, and the :sip:ref:`~PyQt6.QtCore.QRect.intersects` function returns ``true`` if this rectangle intersects with a given rectangle. The :sip:ref:`~PyQt6.QtCore.QRect` class also provides the :sip:ref:`~PyQt6.QtCore.QRect.intersected` function which returns the intersection rectangle, and the :sip:ref:`~PyQt6.QtCore.QRect.united` function which returns the rectangle that encloses the given rectangle and this:

+--------------------------------------------+---------------------------------------+
| |image-qrect-intersect-png|                | |image-qrect-unite-png|               |
+--------------------------------------------+---------------------------------------+
| :sip:ref:`~PyQt6.QtCore.QRect.intersected` | :sip:ref:`~PyQt6.QtCore.QRect.united` |
+--------------------------------------------+---------------------------------------+

The :sip:ref:`~PyQt6.QtCore.QRect.isEmpty` function returns ``true`` if :sip:ref:`~PyQt6.QtCore.QRect.left` > :sip:ref:`~PyQt6.QtCore.QRect.right` or :sip:ref:`~PyQt6.QtCore.QRect.top` > :sip:ref:`~PyQt6.QtCore.QRect.bottom`. Note that an empty rectangle is not valid: The :sip:ref:`~PyQt6.QtCore.QRect.isValid` function returns ``true`` if :sip:ref:`~PyQt6.QtCore.QRect.left` <= :sip:ref:`~PyQt6.QtCore.QRect.right` *and* :sip:ref:`~PyQt6.QtCore.QRect.top` <= :sip:ref:`~PyQt6.QtCore.QRect.bottom`. A null rectangle (\ :sip:ref:`~PyQt6.QtCore.QRect.isNull` == true) on the other hand, has both width and height set to 0.

Note that due to the way :sip:ref:`~PyQt6.QtCore.QRect` and :sip:ref:`~PyQt6.QtCore.QRectF` are defined, an empty :sip:ref:`~PyQt6.QtCore.QRect` is defined in essentially the same way as :sip:ref:`~PyQt6.QtCore.QRectF`.

Finally, :sip:ref:`~PyQt6.QtCore.QRect` objects can be streamed as well as compared.

.. _qrect-rendering:

Rendering
---------

When using an anti-aliased painter, the boundary line of a :sip:ref:`~PyQt6.QtCore.QRect` will be rendered symmetrically on both sides of the mathematical rectangle's boundary line. But when using an aliased painter (the default) other rules apply.

Then, when rendering with a one pixel wide pen the :sip:ref:`~PyQt6.QtCore.QRect`'s boundary line will be rendered to the right and below the mathematical rectangle's boundary line.

When rendering with a two pixels wide pen the boundary line will be split in the middle by the mathematical rectangle. This will be the case whenever the pen is set to an even number of pixels, while rendering with a pen with an odd number of pixels, the spare pixel will be rendered to the right and below the mathematical rectangle as in the one pixel case.

+--------------------------------+---------------------------------+
| |image-qrect-diagram-zero-png| | |image-qrect-diagram-one-png|   |
+--------------------------------+---------------------------------+
| Logical representation         | One pixel wide pen              |
+--------------------------------+---------------------------------+
| |image-qrect-diagram-two-png|  | |image-qrect-diagram-three-png| |
+--------------------------------+---------------------------------+
| Two pixel wide pen             | Three pixel wide pen            |
+--------------------------------+---------------------------------+

.. _qrect-coordinates:

Coordinates
-----------

The :sip:ref:`~PyQt6.QtCore.QRect` class provides a collection of functions that return the various rectangle coordinates, and enable manipulation of these. :sip:ref:`~PyQt6.QtCore.QRect` also provides functions to move the rectangle relative to the various coordinates.

For example the :sip:ref:`~PyQt6.QtCore.QRect.left`, :sip:ref:`~PyQt6.QtCore.QRect.setLeft` and :sip:ref:`~PyQt6.QtCore.QRect.moveLeft` functions as an example: :sip:ref:`~PyQt6.QtCore.QRect.left` returns the x-coordinate of the rectangle's left edge, :sip:ref:`~PyQt6.QtCore.QRect.setLeft` sets the left edge of the rectangle to the given x coordinate (it may change the width, but will never change the rectangle's right edge) and :sip:ref:`~PyQt6.QtCore.QRect.moveLeft` moves the entire rectangle horizontally, leaving the rectangle's left edge at the given x coordinate and its size unchanged.

.. image:: ../../../images/qrect-coordinates.png

Note that for historical reasons the values returned by the :sip:ref:`~PyQt6.QtCore.QRect.bottom` and :sip:ref:`~PyQt6.QtCore.QRect.right` functions deviate from the true bottom-right corner of the rectangle: The :sip:ref:`~PyQt6.QtCore.QRect.right` function returns * :sip:ref:`~PyQt6.QtCore.QRect.left` + :sip:ref:`~PyQt6.QtCore.QRect.width` - 1* and the :sip:ref:`~PyQt6.QtCore.QRect.bottom` function returns *\ :sip:ref:`~PyQt6.QtCore.QRect.top` + :sip:ref:`~PyQt6.QtCore.QRect.height` - 1*. The same is the case for the point returned by the :sip:ref:`~PyQt6.QtCore.QRect.bottomRight` convenience function. In addition, the x and y coordinate of the :sip:ref:`~PyQt6.QtCore.QRect.topRight` and :sip:ref:`~PyQt6.QtCore.QRect.bottomLeft` functions, respectively, contain the same deviation from the true right and bottom edges.

We recommend that you use :sip:ref:`~PyQt6.QtCore.QRect.x` + :sip:ref:`~PyQt6.QtCore.QRect.width` and :sip:ref:`~PyQt6.QtCore.QRect.y` + :sip:ref:`~PyQt6.QtCore.QRect.height` to find the true bottom-right corner, and avoid :sip:ref:`~PyQt6.QtCore.QRect.right` and :sip:ref:`~PyQt6.QtCore.QRect.bottom`. Another solution is to use :sip:ref:`~PyQt6.QtCore.QRectF`: The :sip:ref:`~PyQt6.QtCore.QRectF` class defines a rectangle in the plane using floating point accuracy for coordinates, and the :sip:ref:`~PyQt6.QtCore.QRectF.right` and :sip:ref:`~PyQt6.QtCore.QRectF.bottom` functions *do* return the right and bottom coordinates.

It is also possible to add offsets to this rectangle's coordinates using the :sip:ref:`~PyQt6.QtCore.QRect.adjust` function, as well as retrieve a new rectangle based on adjustments of the original one using the :sip:ref:`~PyQt6.QtCore.QRect.adjusted` function. If either of the width and height is negative, use the :sip:ref:`~PyQt6.QtCore.QRect.normalized` function to retrieve a rectangle where the corners are swapped.

In addition, :sip:ref:`~PyQt6.QtCore.QRect` provides the :sip:ref:`~PyQt6.QtCore.QRect.getCoords` function which extracts the position of the rectangle's top-left and bottom-right corner, and the :sip:ref:`~PyQt6.QtCore.QRect.getRect` function which extracts the rectangle's top-left corner, width and height. Use the :sip:ref:`~PyQt6.QtCore.QRect.setCoords` and :sip:ref:`~PyQt6.QtCore.QRect.setRect` function to manipulate the rectangle's coordinates and dimensions in one go.

.. _qrect-constraints:

Constraints
-----------

:sip:ref:`~PyQt6.QtCore.QRect` is limited to the minimum and maximum values for the ``int`` type. Operations on a :sip:ref:`~PyQt6.QtCore.QRect` that could potentially result in values outside this range will result in undefined behavior.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRectF`.

.. |image-qrect-intersect-png| image:: ../../../images/qrect-intersect.png
.. |image-qrect-unite-png| image:: ../../../images/qrect-unite.png
.. |image-qrect-diagram-zero-png| image:: ../../../images/qrect-diagram-zero.png
.. |image-qrect-diagram-one-png| image:: ../../../images/qrect-diagram-one.png
.. |image-qrect-diagram-two-png| image:: ../../../images/qrect-diagram-two.png
.. |image-qrect-diagram-three-png| image:: ../../../images/qrect-diagram-three.png
