.. sip:method-description::
    :status: todo
    :pysig: 8aa27e0adaa46963b99c4dad999ed0ac
    :realsig: (int) const
    :digest: 7924363285061db8e870eccd2dd016b3

Returns a darker (or lighter) color, but does not change this object.

If the *factor* is greater than 100, this functions returns a darker color. Setting *factor* to 300 returns a color that has one-third the brightness. If the *factor* is less than 100, the return color is lighter, but we recommend using the :sip:ref:`~PyQt6.QtGui.QColor.lighter` function for this purpose. If the *factor* is 0 or negative, the return value is unspecified.

The function converts the current color to HSV, divides the value (V) component by *factor* and converts the color back to it's original color spec.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QColor.lighter`, :sip:ref:`~PyQt6.QtGui.QColor.isValid`.
