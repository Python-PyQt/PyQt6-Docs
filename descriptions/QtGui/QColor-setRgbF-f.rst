.. sip:method-description::
    :status: todo
    :pysig: 0de852e9d6a0cdb34a4e7fcfa2729ef0
    :realsig: (float,float,float,float)
    :digest: 178fdd2f17a6b89400d1376501e7ef48

Sets the color channels of this color to *r* (red), *g* (green), *b* (blue) and *a* (alpha, transparency).

The alpha value must be in the range 0.0-1.0. If any of the other values are outside the range of 0.0-1.0 the color model will be set as ``ExtendedRgb``.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QColor.rgb`, :sip:ref:`~PyQt6.QtGui.QColor.getRgbF`, :sip:ref:`~PyQt6.QtGui.QColor.setRgb`.
