.. sip:method-description::
    :status: todo
    :pysig: 93c65966a7252879a2fdbc87264c9da8
    :realsig: (int*,int*,int*,int*) const
    :digest: 19c0b5b546bf4edd12e613cf410e09db

Sets the contents pointed to by *h*, *s*, *v*, and *a*, to the hue, saturation, value, and alpha-channel (transparency) components of the color's HSV value.

These components can be retrieved individually using the :sip:ref:`~PyQt6.QtGui.QColor.hue`, :sip:ref:`~PyQt6.QtGui.QColor.saturation`, :sip:ref:`~PyQt6.QtGui.QColor.value` and :sip:ref:`~PyQt6.QtGui.QColor.alpha` functions.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QColor.setHsv`, The HSV Color Model.
