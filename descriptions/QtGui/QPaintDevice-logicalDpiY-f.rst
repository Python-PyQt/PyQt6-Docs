.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: eacf066e2ef6450160e767f98ce9dff2

Returns the vertical resolution of the device in dots per inch, which is used when computing font sizes. For X11, this is usually the same as could be computed from :sip:ref:`~PyQt6.QtGui.QPaintDevice.heightMM`.

Note that if the logicalDpiY() doesn't equal the :sip:ref:`~PyQt6.QtGui.QPaintDevice.physicalDpiY`, the corresponding :sip:ref:`~PyQt6.QtGui.QPaintEngine` must handle the resolution mapping.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPaintDevice.logicalDpiX`, :sip:ref:`~PyQt6.QtGui.QPaintDevice.physicalDpiY`.
