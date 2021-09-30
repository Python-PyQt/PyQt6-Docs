.. sip:method-description::
    :status: todo
    :pysig: c5d6e3115e754b395283dc1c09f54493
    :realsig: () const
    :digest: d7a9c0755aa825eaeee0655eb3be7a12

Returns the size of the pixmap in device independent pixels.

This value should be used when using the pixmap size in user interface size calculations.

The return value is equivalent to pixmap.\ :sip:ref:`~PyQt6.QtGui.QImage.size` / pixmap.\ :sip:ref:`~PyQt6.QtGui.QImage.devicePixelRatio`,
