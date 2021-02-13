.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 420d648e8d43794fef0698e93d03dbc1

Sets the vertical stretch factor of the size policy to the given *stretchFactor*. *stretchFactor* must be in the range [0,255].

When two widgets are adjacent to each other in a vertical layout, setting the vertical stretch factor of the widget on the top to 2 and the factor of widget on the bottom to 1 will ensure that the widget on the top will always be twice the size of the one on the bottom.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QSizePolicy.verticalStretch`, :sip:ref:`~PyQt6.QtWidgets.QSizePolicy.setHorizontalStretch`, :sip:ref:`~PyQt6.QtWidgets.QSizePolicy.setVerticalPolicy`.
