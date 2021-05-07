.. sip:method-description::
    :status: todo
    :pysig: c798fdc999a98312c2cd33e6dc5a34dd
    :realsig: (const uchar*,uint,const char*,Qt::ImageConversionFlags)
    :digest: 564f2181a7a2990035ab7bcd27f73cb3

Loads a pixmap from the *len* first bytes of the given binary *data*. Returns ``true`` if the pixmap was loaded successfully; otherwise invalidates the pixmap and returns ``false``.

The loader attempts to read the pixmap using the specified *format*. If the *format* is not specified (which is the default), the loader probes the file for a header to guess the file format.

If the data needs to be modified to fit in a lower-resolution result (e.g. converting from 32-bit to 8-bit), use the *flags* to control the conversion.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPixmap.load`, Reading and Writing Image Files.
