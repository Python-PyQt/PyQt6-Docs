.. sip:method-description::
    :status: todo
    :pysig: 69483954c54f32e4c4c85fce225f51dd
    :realsig: (uchar*,int,int,qsizetype,QImage::Format,QImageCleanupFunction,void*)
    :digest: 0927e533fcc98501367176558c32181c

Constructs an image with the given *width*, *height* and *format*, that uses an existing memory buffer, *data*. The *width* and *height* must be specified in pixels. *bytesPerLine* specifies the number of bytes per line (stride).

The buffer must remain valid throughout the life of the :sip:ref:`~PyQt6.QtGui.QImage` and all copies that have not been modified or otherwise detached from the original buffer. The image does not delete the buffer at destruction. You can provide a function pointer *cleanupFunction* along with an extra pointer *cleanupInfo* that will be called when the last copy is destroyed.

If *format* is an indexed color format, the image color table is initially empty and must be sufficiently expanded with :sip:ref:`~PyQt6.QtGui.QImage.setColorCount` or :sip:ref:`~PyQt6.QtGui.QImage.setColorTable` before the image is used.
