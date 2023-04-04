.. sip:method-description::
    :status: todo
    :pysig: e147056b19e6a627c615ffd0a7d33034
    :realsig: (HBITMAP)
    :digest: c331c9dd2d3e9091d6701fc47901562e

Returns a :sip:ref:`~PyQt6.QtGui.QImage` that is equivalent to the given *hbitmap*.

HBITMAP does not store information about the alpha channel.

In the standard case, the alpha channel is ignored and a fully opaque image is created (typically of format :sip:ref:`~PyQt6.QtGui.QImage.Format.Format_RGB32`).

There are cases where the alpha channel is used, though, for example for application icon or systray icons. In that case, ``reinterpretAsFormat(QImage::Format_ARGB32)`` should be called on the returned image to ensure the format is correct.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.toHBITMAP`, :sip:ref:`~PyQt6.QtGui.QImage.reinterpretAsFormat`.
