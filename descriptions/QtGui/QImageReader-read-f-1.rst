.. sip:method-description::
    :status: todo
    :pysig: b5207006acd9098e45a6c3737781523d
    :realsig: (QImage*)
    :digest: 1d5aac3e8a9d44500058b9a5d43a69d4

This is an overloaded function.

Reads an image from the device into *image*, which must point to a :sip:ref:`~PyQt6.QtGui.QImage`. Returns ``true`` on success; otherwise, returns ``false``.

If *image* has same format and size as the image data that is about to be read, this function may not need to allocate a new image before reading. Because of this, it can be faster than the other :sip:ref:`~PyQt6.QtGui.QImageReader.read` overload, which always constructs a new image; especially when reading several images with the same format and size.

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_image_qimagereader.py
    :lines: 75-79

For image formats that support animation, calling :sip:ref:`~PyQt6.QtGui.QImageReader.read` repeatedly will return the next frame. When all frames have been read, a null image will be returned.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImageReader.canRead`, :sip:ref:`~PyQt6.QtGui.QImageReader.supportedImageFormats`, :sip:ref:`~PyQt6.QtGui.QImageReader.supportsAnimation`, :sip:ref:`~PyQt6.QtGui.QMovie`.
