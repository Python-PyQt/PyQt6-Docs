.. sip:method-description::
    :status: todo
    :pysig: 93c65966a7252879a2fdbc87264c9da8
    :realsig: (int*,int*,int*,int*) const
    :digest: d31e3042e9aa163acb7167ed96246707

Sets the contents pointed to by *h*, *s*, *l*, and *a*, to the hue, saturation, lightness, and alpha-channel (transparency) components of the color's HSL value.

These components can be retrieved individually using the :sip:ref:`~PyQt6.QtGui.QColor.hslHue`, :sip:ref:`~PyQt6.QtGui.QColor.hslSaturation`, :sip:ref:`~PyQt6.QtGui.QColor.lightness` and :sip:ref:`~PyQt6.QtGui.QColor.alpha` functions.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QColor.getHslF`, :sip:ref:`~PyQt6.QtGui.QColor.setHsl`, The HSL Color Model.
