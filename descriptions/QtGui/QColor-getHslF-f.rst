.. sip:method-description::
    :status: todo
    :pysig: 5fd70130e629f44666196fc320d4f2e1
    :realsig: (float*,float*,float*,float*) const
    :digest: 44df5b023a24684c3940abfffffb9e2d

Sets the contents pointed to by *h*, *s*, *l*, and *a*, to the hue, saturation, lightness, and alpha-channel (transparency) components of the color's HSL value.

These components can be retrieved individually using the :sip:ref:`~PyQt6.QtGui.QColor.hslHueF`, :sip:ref:`~PyQt6.QtGui.QColor.hslSaturationF`, :sip:ref:`~PyQt6.QtGui.QColor.lightnessF` and :sip:ref:`~PyQt6.QtGui.QColor.alphaF` functions.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QColor.getHsl`, :sip:ref:`~PyQt6.QtGui.QColor.setHslF`, The HSL Color Model.
