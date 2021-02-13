.. sip:method-description::
    :status: todo
    :pysig: 6a1210c65f1e345144ef1fb118a47862
    :realsig: (const uchar*,int,int,QImage::Format,QImageCleanupFunction,void*)
    :digest: 1781ab101186c7b887d5a72a9b0a1886

Constructs an image with the given *width*, *height* and *format*, that uses an existing read-only memory buffer, *data*. The *width* and *height* must be specified in pixels, *data* must be 32-bit aligned, and each scanline of data in the image must also be 32-bit aligned.

The buffer must remain valid throughout the life of the :sip:ref:`~PyQt6.QtGui.QImage` and all copies that have not been modified or otherwise detached from the original buffer. The image does not delete the buffer at destruction. You can provide a function pointer *cleanupFunction* along with an extra pointer *cleanupInfo* that will be called when the last copy is destroyed.

If *format* is an indexed color format, the image color table is initially empty and must be sufficiently expanded with :sip:ref:`~PyQt6.QtGui.QImage.setColorCount` or :sip:ref:`~PyQt6.QtGui.QImage.setColorTable` before the image is used.

Unlike the similar :sip:ref:`~PyQt6.QtGui.QImage` constructor that takes a non-const data buffer, this version will never alter the contents of the buffer. For example, calling :sip:ref:`~PyQt6.QtGui.QImage.bits` will return a deep copy of the image, rather than the buffer passed to the constructor. This allows for the efficiency of constructing a :sip:ref:`~PyQt6.QtGui.QImage` from raw data, without the possibility of the raw data being changed.
