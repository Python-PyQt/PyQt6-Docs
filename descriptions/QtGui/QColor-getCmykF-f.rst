.. sip:method-description::
    :status: todo
    :pysig: 568b014a366a71095f4f9661cf095121
    :realsig: (float*,float*,float*,float*,float*) const
    :digest: 3281d82fd41b336bc4106e6cf8748d57

Sets the contents pointed to by *c*, *m*, *y*, *k*, and *a*, to the cyan, magenta, yellow, black, and alpha-channel (transparency) components of the color's CMYK value.

These components can be retrieved individually using the :sip:ref:`~PyQt6.QtGui.QColor.cyanF`, :sip:ref:`~PyQt6.QtGui.QColor.magentaF`, :sip:ref:`~PyQt6.QtGui.QColor.yellowF`, :sip:ref:`~PyQt6.QtGui.QColor.blackF` and :sip:ref:`~PyQt6.QtGui.QColor.alphaF` functions.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QColor.setCmykF`, The CMYK Color Model.
