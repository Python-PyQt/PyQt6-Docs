.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: () const
    :digest: 88a89d257f110f23c8ee22a31ee978f5

Returns the device pixel ratio for the pixmap. This is the ratio between *device pixels* and *device independent pixels*.

Use this function when calculating layout geometry based on the pixmap size: :sip:ref:`~PyQt6.QtCore.QSize` layoutSize = image.\ :sip:ref:`~PyQt6.QtGui.QPixmap.size` / image.

The default value is 1.0.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPixmap.setDevicePixelRatio`, :sip:ref:`~PyQt6.QtGui.QImageReader`.
