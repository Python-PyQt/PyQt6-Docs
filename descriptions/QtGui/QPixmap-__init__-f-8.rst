.. sip:method-description::
    :status: todo
    :pysig: 412be8b39d1ca3b35cd9de8d379e0b20
    :realsig: (const QString&, const char*, Qt::ImageConversionFlags)
    :digest: 3ad2940a8747eb1436cbca16a3a05055

Constructs a pixmap from the file with the given *fileName*. If the file does not exist or is of an unknown format, the pixmap becomes a null pixmap.

The loader attempts to read the pixmap using the specified *format*. If the *format* is not specified (which is the default), the loader probes the file for a header to guess the file format.

The file name can either refer to an actual file on disk or to one of the application's embedded resources. See the `Resource System <https://doc.qt.io/qt-6/resources.html>`_ overview for details on how to embed images and other resource files in the application's executable.

If the image needs to be modified to fit in a lower-resolution result (e.g. converting from 32-bit to 8-bit), use the *flags* to control the conversion.

The *fileName*, *format* and *flags* parameters are passed on to :sip:ref:`~PyQt6.QtGui.QPixmap.load`. This means that the data in *fileName* is not compiled into the binary. If *fileName* contains a relative path (e.g. the filename only) the relevant file must be found relative to the runtime working directory.

.. seealso:: Reading and Writing Image Files.
