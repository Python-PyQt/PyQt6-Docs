.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 311b878d2ccc9b47878b6024fbb86dba

Returns the horizontal resolution of the device in dots per inch, which is used when computing font sizes. For X11, this is usually the same as could be computed from :sip:ref:`~PyQt6.QtGui.QPaintDevice.widthMM`.

Note that if the logicalDpiX() doesn't equal the :sip:ref:`~PyQt6.QtGui.QPaintDevice.physicalDpiX`, the corresponding :sip:ref:`~PyQt6.QtGui.QPaintEngine` must handle the resolution mapping.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPaintDevice.logicalDpiY`, :sip:ref:`~PyQt6.QtGui.QPaintDevice.physicalDpiX`.
