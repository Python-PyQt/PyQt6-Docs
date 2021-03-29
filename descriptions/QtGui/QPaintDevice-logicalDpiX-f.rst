.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 00ddde8691fc99ffbd2f3906bf3bb7c0

Returns the horizontal resolution of the device in dots per inch, which is used when computing font sizes. For X11, this is usually the same as could be computed from :sip:ref:`~PyQt6.QtGui.QPaintDevice.widthMM`.

Note that if the  doesn't equal the :sip:ref:`~PyQt6.QtGui.QPaintDevice.physicalDpiX`, the corresponding :sip:ref:`~PyQt6.QtGui.QPaintEngine` must handle the resolution mapping.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPaintDevice.logicalDpiY`, :sip:ref:`~PyQt6.QtGui.QPaintDevice.physicalDpiX`.
