.. sip:method-description::
    :status: todo
    :pysig: 1f0dc312dc4893420e6715683874f4ea
    :realsig: (const uchar*,int,const char*)
    :digest: 7cf88cb1875482da76bcc1d1853f5d80

Constructs a :sip:ref:`~PyQt6.QtGui.QImage` from the first *size* bytes of the given binary *data*. The loader attempts to read the image using the specified *format*. If *format* is not specified (which is the default), the loader probes the data for a header to guess the file format.

If *format* is specified, it must be one of the values returned by :sip:ref:`~PyQt6.QtGui.QImageReader.supportedImageFormats`.

If the loading of the image fails, the image returned will be a null image.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.load`, :sip:ref:`~PyQt6.QtGui.QImage.save`, Reading and Writing Image Files.
