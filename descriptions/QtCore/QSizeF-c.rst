.. sip:class-description::
    :status: todo
    :brief: Defines the size of a two-dimensional object using floating point precision
    :digest: c81be75a2f2995e945baacdd60771077

The :sip:ref:`~PyQt6.QtCore.QSizeF` class defines the size of a two-dimensional object using floating point precision.

A size is specified by a :sip:ref:`~PyQt6.QtCore.QSizeF.width` and a :sip:ref:`~PyQt6.QtCore.QSizeF.height`. It can be set in the constructor and changed using the :sip:ref:`~PyQt6.QtCore.QSizeF.setWidth`, :sip:ref:`~PyQt6.QtCore.QSizeF.setHeight`, or :sip:ref:`~PyQt6.QtCore.QSizeF.scale` functions, or using arithmetic operators. A size can also be manipulated directly by retrieving references to the width and height using the rwidth() and rheight() functions. Finally, the width and height can be swapped using the :sip:ref:`~PyQt6.QtCore.QSizeF.transpose` function.

The :sip:ref:`~PyQt6.QtCore.QSizeF.isValid` function determines if a size is valid. A valid size has both width and height greater than or equal to zero. The :sip:ref:`~PyQt6.QtCore.QSizeF.isEmpty` function returns ``true`` if either of the width and height is *less* than (or equal to) zero, while the :sip:ref:`~PyQt6.QtCore.QSizeF.isNull` function returns ``true`` only if both the width and the height is zero.

Use the :sip:ref:`~PyQt6.QtCore.QSizeF.expandedTo` function to retrieve a size which holds the maximum height and width of this size and a given size. Similarly, the :sip:ref:`~PyQt6.QtCore.QSizeF.boundedTo` function returns a size which holds the minimum height and width of this size and a given size.

The :sip:ref:`~PyQt6.QtCore.QSizeF` class also provides the :sip:ref:`~PyQt6.QtCore.QSizeF.toSize` function returning a :sip:ref:`~PyQt6.QtCore.QSize` copy of this size, constructed by rounding the width and height to the nearest integers.

:sip:ref:`~PyQt6.QtCore.QSizeF` objects can be streamed as well as compared.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSize`, :sip:ref:`~PyQt6.QtCore.QPointF`, :sip:ref:`~PyQt6.QtCore.QRectF`.
