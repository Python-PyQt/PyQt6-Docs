.. sip:method-description::
    :status: todo
    :pysig: 0187dd8db57ff82c779a89fcc4138b8c
    :realsig: (const QSize&,QImage::Format)
    :digest: a188ca1d7663de919624b8237986913d

Constructs an image with the given *size* and *format*.

A :sip:ref:`~PyQt6.QtGui.QImage.isNull` image is returned if memory cannot be allocated.

**Warning:** This will create a :sip:ref:`~PyQt6.QtGui.QImage` with uninitialized data. Call :sip:ref:`~PyQt6.QtGui.QImage.fill` to fill the image with an appropriate pixel value before drawing onto it with :sip:ref:`~PyQt6.QtGui.QPainter`.
