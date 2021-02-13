.. sip:method-description::
    :status: todo
    :pysig: 032f6c0d59c34420b785d65c7ebdefa2
    :realsig: (int,int,QImage::Format)
    :digest: 1edcae4835f234450a6d84891a21b0ba

Constructs an image with the given *width*, *height* and *format*.

A :sip:ref:`~PyQt6.QtGui.QImage.isNull` image will be returned if memory cannot be allocated.

**Warning:** This will create a :sip:ref:`~PyQt6.QtGui.QImage` with uninitialized data. Call :sip:ref:`~PyQt6.QtGui.QImage.fill` to fill the image with an appropriate pixel value before drawing onto it with :sip:ref:`~PyQt6.QtGui.QPainter`.
