.. sip:method-description::
    :status: todo
    :pysig: 1d557afd38e9b10837d8f94f0b85c942
    :realsig: (int) const
    :digest: d3a85f321aab3852e00bdf67e0b1e82e

Returns a pointer to the pixel data at the scanline with index *i*. The first scanline is at index 0.

The scanline data is as minimum 32-bit aligned. For 64-bit formats it follows the native alignment of 64-bit integers (64-bit for most platforms, but notably 32-bit on i386).

Note that :sip:ref:`~PyQt6.QtGui.QImage` uses `implicit data sharing <https://doc.qt.io/qt-6/implicit-sharing.html>`_, but this function does *not* perform a deep copy of the shared pixel data, because the returned data is const.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.scanLine`, :sip:ref:`~PyQt6.QtGui.QImage.constBits`.
