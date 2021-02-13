.. sip:method-description::
    :status: todo
    :pysig: c2a647d5516b1918d5a328f3ea644957
    :realsig: (int*,int*,int*,int*,int*) const
    :digest: a671b9faba01d675a7f4be2708a0c305

Sets the contents pointed to by *c*, *m*, *y*, *k*, and *a*, to the cyan, magenta, yellow, black, and alpha-channel (transparency) components of the color's CMYK value.

These components can be retrieved individually using the :sip:ref:`~PyQt6.QtGui.QColor.cyan`, :sip:ref:`~PyQt6.QtGui.QColor.magenta`, :sip:ref:`~PyQt6.QtGui.QColor.yellow`, :sip:ref:`~PyQt6.QtGui.QColor.black` and :sip:ref:`~PyQt6.QtGui.QColor.alpha` functions.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QColor.setCmyk`, The CMYK Color Model.
