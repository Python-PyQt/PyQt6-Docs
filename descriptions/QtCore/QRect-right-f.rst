.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: f5e0e1bb07edd324b42323f8ebe3b06b

Returns the x-coordinate of the rectangle's right edge.

Note that for historical reasons this function returns :sip:ref:`~PyQt6.QtCore.QRect.left` + :sip:ref:`~PyQt6.QtCore.QRect.width` - 1; use :sip:ref:`~PyQt6.QtCore.QRect.x` + :sip:ref:`~PyQt6.QtCore.QRect.width` to retrieve the true x-coordinate.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRect.setRight`, :sip:ref:`~PyQt6.QtCore.QRect.topRight`, :sip:ref:`~PyQt6.QtCore.QRect.bottomRight`.
