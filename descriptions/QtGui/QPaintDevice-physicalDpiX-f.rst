.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: f05b58e0ce76db8e18085e953f87e43a

Returns the horizontal resolution of the device in dots per inch. For example, when printing, this resolution refers to the physical printer's resolution. The logical DPI on the other hand, refers to the resolution used by the actual paint engine.

Note that if the  doesn't equal the :sip:ref:`~PyQt6.QtGui.QPaintDevice.logicalDpiX`, the corresponding :sip:ref:`~PyQt6.QtGui.QPaintEngine` must handle the resolution mapping.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPaintDevice.physicalDpiY`, :sip:ref:`~PyQt6.QtGui.QPaintDevice.logicalDpiX`.
