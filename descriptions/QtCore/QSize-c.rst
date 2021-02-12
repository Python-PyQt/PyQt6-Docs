.. sip:class-description::
    :status: todo
    :brief: Defines the size of a two-dimensional object using integer point precision
    :digest: 31e8f65f694e49ffb153627ab1d5d2ba

The :sip:ref:`~PyQt6.QtCore.QSize` class defines the size of a two-dimensional object using integer point precision.

A size is specified by a :sip:ref:`~PyQt6.QtCore.QSize.width` and a :sip:ref:`~PyQt6.QtCore.QSize.height`. It can be set in the constructor and changed using the :sip:ref:`~PyQt6.QtCore.QSize.setWidth`, :sip:ref:`~PyQt6.QtCore.QSize.setHeight`, or :sip:ref:`~PyQt6.QtCore.QSize.scale` functions, or using arithmetic operators. A size can also be manipulated directly by retrieving references to the width and height using the rwidth() and rheight() functions. Finally, the width and height can be swapped using the :sip:ref:`~PyQt6.QtCore.QSize.transpose` function.

The :sip:ref:`~PyQt6.QtCore.QSize.isValid` function determines if a size is valid (a valid size has both width and height greater than or equal to zero). The :sip:ref:`~PyQt6.QtCore.QSize.isEmpty` function returns ``true`` if either of the width and height is less than, or equal to, zero, while the :sip:ref:`~PyQt6.QtCore.QSize.isNull` function returns ``true`` only if both the width and the height is zero.

Use the :sip:ref:`~PyQt6.QtCore.QSize.expandedTo` function to retrieve a size which holds the maximum height and width of *this* size and a given size. Similarly, the :sip:ref:`~PyQt6.QtCore.QSize.boundedTo` function returns a size which holds the minimum height and width of *this* size and a given size.

:sip:ref:`~PyQt6.QtCore.QSize` objects can be streamed as well as compared.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSizeF`, :sip:ref:`~PyQt6.QtCore.QPoint`, :sip:ref:`~PyQt6.QtCore.QRect`.
