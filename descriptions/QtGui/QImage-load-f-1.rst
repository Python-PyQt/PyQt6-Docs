.. sip:method-description::
    :status: todo
    :pysig: 770eee14d0fdff90f4c3720a64882ca1
    :realsig: (const QString&,const char*)
    :digest: a55ad9c473479831938729240245a751

Loads an image from the file with the given *fileName*. Returns ``true`` if the image was successfully loaded; otherwise invalidates the image and returns ``false``.

The loader attempts to read the image using the specified *format*, e.g., PNG or JPG. If *format* is not specified (which is the default), it is auto-detected based on the file's suffix and header. For details, see :sip:ref:`~PyQt6.QtGui.QImageReader.setAutoDetectImageFormat`.

The file name can either refer to an actual file on disk or to one of the application's embedded resources. See the `Resource System <https://doc.qt.io/qt-6/resources.html>`_ overview for details on how to embed images and other resource files in the application's executable.

.. seealso:: Reading and Writing Image Files.
