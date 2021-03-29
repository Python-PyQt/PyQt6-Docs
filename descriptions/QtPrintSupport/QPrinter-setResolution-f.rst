.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: e21f58767952be0b28aa14a2a2af6484

Requests that the printer prints at *dpi* or as near to *dpi* as possible.

This setting affects the coordinate system as returned by, for example :sip:ref:`~PyQt6.QtGui.QPainter.viewport`.

This function must be called before :sip:ref:`~PyQt6.QtGui.QPainter.begin` to have an effect on all platforms.

.. seealso:: :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.resolution`, :sip:ref:`~PyQt6.QtGui.QPagedPaintDevice.setPageSize`.
