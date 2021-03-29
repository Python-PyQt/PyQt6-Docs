.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 5155534279c548a2de63f1b6a0c3257d

If *fp* is true, enables support for painting over the entire page; otherwise restricts painting to the printable area reported by the device.

By default, full page printing is disabled. In this case, the origin of the :sip:ref:`~PyQt6.QtPrintSupport.QPrinter`'s coordinate system coincides with the top-left corner of the printable area.

If full page printing is enabled, the origin of the :sip:ref:`~PyQt6.QtPrintSupport.QPrinter`'s coordinate system coincides with the top-left corner of the paper itself. In this case, the :sip:ref:`~PyQt6.QtGui.QPaintDevice.PaintDeviceMetric` will report the exact same dimensions as indicated by {\ :sip:ref:`~PyQt6.QtGui.QPageSize`}. It may not be possible to print on the entire physical page because of the printer's margins, so the application must account for the margins itself.

.. seealso:: :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.fullPage`, :sip:ref:`~PyQt6.QtGui.QPagedPaintDevice.pageLayout`, :sip:ref:`~PyQt6.QtGui.QPagedPaintDevice.setPageSize`.
