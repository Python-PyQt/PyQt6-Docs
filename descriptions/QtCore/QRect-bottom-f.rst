.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: d3faa841c697b1942ada230b4afa1fd8

Returns the y-coordinate of the rectangle's bottom edge.

Note that for historical reasons this function returns :sip:ref:`~PyQt6.QtCore.QRect.top` + :sip:ref:`~PyQt6.QtCore.QRect.height` - 1; use :sip:ref:`~PyQt6.QtCore.QRect.y` + :sip:ref:`~PyQt6.QtCore.QRect.height` to retrieve the true y-coordinate.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRect.setBottom`, :sip:ref:`~PyQt6.QtCore.QRect.bottomLeft`, :sip:ref:`~PyQt6.QtCore.QRect.bottomRight`.
