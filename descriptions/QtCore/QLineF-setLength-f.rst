.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: (qreal)
    :digest: 272adcba8ac9cb324719dd504d481474

Sets the length of the line to the given *length*. :sip:ref:`~PyQt6.QtCore.QLineF` will move the end point - :sip:ref:`~PyQt6.QtCore.QLineF.p2` - of the line to give the line its new length, unless :sip:ref:`~PyQt6.QtCore.QLineF.length` was previously zero, in which case no scaling is attempted. For lines with very short lengths (represented by denormal floating-point values), results may be imprecise.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLineF.length`, :sip:ref:`~PyQt6.QtCore.QLineF.unitVector`.
