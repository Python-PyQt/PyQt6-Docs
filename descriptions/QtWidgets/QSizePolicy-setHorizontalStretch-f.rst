.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 2c96a10e4b92f63d20142d6dd9cfae68

Sets the horizontal stretch factor of the size policy to the given *stretchFactor*. *stretchFactor* must be in the range [0,255].

When two widgets are adjacent to each other in a horizontal layout, setting the horizontal stretch factor of the widget on the left to 2 and the factor of widget on the right to 1 will ensure that the widget on the left will always be twice the size of the one on the right.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QSizePolicy.horizontalStretch`, :sip:ref:`~PyQt6.QtWidgets.QSizePolicy.setVerticalStretch`, :sip:ref:`~PyQt6.QtWidgets.QSizePolicy.setHorizontalPolicy`.
