.. sip:method-description::
    :status: todo
    :pysig: 5fd70130e629f44666196fc320d4f2e1
    :realsig: (float*,float*,float*,float*) const
    :digest: 2f8f233e8c801ecd1c41583be7b62379

Sets the contents pointed to by *h*, *s*, *v*, and *a*, to the hue, saturation, value, and alpha-channel (transparency) components of the color's HSV value.

These components can be retrieved individually using the :sip:ref:`~PyQt6.QtGui.QColor.hueF`, :sip:ref:`~PyQt6.QtGui.QColor.saturationF`, :sip:ref:`~PyQt6.QtGui.QColor.valueF` and :sip:ref:`~PyQt6.QtGui.QColor.alphaF` functions.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QColor.setHsv`, The HSV Color Model.
