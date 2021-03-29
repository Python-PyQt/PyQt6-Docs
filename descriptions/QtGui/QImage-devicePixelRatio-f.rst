.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: () const
    :digest: 8a78bb58f1db911b6911e2fc73498bda

Returns the device pixel ratio for the image. This is the ratio between *device pixels* and *device independent pixels*.

Use this function when calculating layout geometry based on the image size: :sip:ref:`~PyQt6.QtCore.QSize` layoutSize = image.\ :sip:ref:`~PyQt6.QtGui.QImage.size` / image.

The default value is 1.0.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.setDevicePixelRatio`, :sip:ref:`~PyQt6.QtGui.QImageReader`.
