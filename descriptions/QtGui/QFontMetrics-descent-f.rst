.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 10f06d0fe5e493e49db34653787572c9

Returns the descent of the font.

The descent is the distance from the base line to the lowest point characters extend to. In practice, some font designers break this rule, e.g. to accommodate a certain character, so it is possible (though rare) that this value will be too small.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFontMetrics.ascent`.
