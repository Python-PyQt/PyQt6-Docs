.. sip:method-description::
    :status: todo
    :pysig: 13d1615d68c695a811f9c65d90ffa58e
    :realsig: (uchar*,int,int,QImage::Format,QImageCleanupFunction,void*)
    :digest: 93f4c1f2440c75fa977012d56ecf9524

Constructs an image with the given *width*, *height* and *format*, that uses an existing memory buffer, *data*. The *width* and *height* must be specified in pixels, *data* must be 32-bit aligned, and each scanline of data in the image must also be 32-bit aligned.

The buffer must remain valid throughout the life of the :sip:ref:`~PyQt6.QtGui.QImage` and all copies that have not been modified or otherwise detached from the original buffer. The image does not delete the buffer at destruction. You can provide a function pointer *cleanupFunction* along with an extra pointer *cleanupInfo* that will be called when the last copy is destroyed.

If *format* is an indexed color format, the image color table is initially empty and must be sufficiently expanded with :sip:ref:`~PyQt6.QtGui.QImage.setColorCount` or :sip:ref:`~PyQt6.QtGui.QImage.setColorTable` before the image is used.
