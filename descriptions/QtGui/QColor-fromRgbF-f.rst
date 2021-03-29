.. sip:method-description::
    :status: todo
    :pysig: 564805c35505c02060e2b31fa0ffe570
    :realsig: (float,float,float,float)
    :digest: 44893a80459bd26e32c3b97f7135e0be

Static convenience function that returns a :sip:ref:`~PyQt6.QtGui.QColor` constructed from the RGB color values, *r* (red), *g* (green), *b* (blue), and *a* (alpha-channel, i.e. transparency).

The alpha value must be in the range 0.0-1.0. If any of the other values are outside the range of 0.0-1.0 the color model will be set as ``ExtendedRgb``.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QColor.fromRgb`, :sip:ref:`~PyQt6.QtGui.QColor.fromRgba64`, :sip:ref:`~PyQt6.QtGui.QColor.toRgb`, :sip:ref:`~PyQt6.QtGui.QColor.isValid`.
