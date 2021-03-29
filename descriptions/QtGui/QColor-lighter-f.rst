.. sip:method-description::
    :status: todo
    :pysig: 5644a519985d05ddc17c2558e7247812
    :realsig: (int) const
    :digest: e7e3ec88ecd6cd2d211733e5be054489

Returns a lighter (or darker) color, but does not change this object.

If the *factor* is greater than 100, this functions returns a lighter color. Setting *factor* to 150 returns a color that is 50% brighter. If the *factor* is less than 100, the return color is darker, but we recommend using the :sip:ref:`~PyQt6.QtGui.QColor.darker` function for this purpose. If the *factor* is 0 or negative, the return value is unspecified.

The function converts the current color to HSV, multiplies the value (V) component by *factor* and converts the color back to it's original color spec.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QColor.darker`, :sip:ref:`~PyQt6.QtGui.QColor.isValid`.
