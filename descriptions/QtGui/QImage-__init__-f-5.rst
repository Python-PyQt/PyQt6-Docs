.. sip:method-description::
    :status: todo
    :pysig: c5c154cc8d665c929486168782c564eb
    :realsig: (const QString&,const char*)
    :digest: be8cd02dcbd6d1f49bf0deae30c7388e

Constructs an image and tries to load the image from the file with the given *fileName*.

The loader attempts to read the image using the specified *format*. If the *format* is not specified (which is the default), it is auto-detected based on the file's suffix and header. For details, see {\ :sip:ref:`~PyQt6.QtGui.QImageReader.setAutoDetectImageFormat`}{\ :sip:ref:`~PyQt6.QtGui.QImageReader`}.

If the loading of the image failed, this object is a null image.

The file name can either refer to an actual file on disk or to one of the application's embedded resources. See the `Resource System <https://doc.qt.io/qt-6/resources.html>`_ overview for details on how to embed images and other resource files in the application's executable.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.isNull`, Reading and Writing Image Files.
