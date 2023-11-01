.. sip:method-description::
    :status: todo
    :pysig: b8bd92bcf2e4fe9e6ed0c77c8c68bc88
    :realsig: (const QString&, const QSize&, QIcon::Mode, QIcon::State)
    :digest: 6b8ad9987db22819dd1c80a8dd4739db

Adds an image from the file with the given *fileName* to the icon, as a specialization for *size*, *mode* and *state*. The file will be loaded on demand. Note: custom icon engines are free to ignore additionally added pixmaps.

If *fileName* contains a relative path (e.g. the filename only) the relevant file must be found relative to the runtime working directory.

The file name can refer to an actual file on disk or to one of the application's embedded resources. See the `Resource System <https://doc.qt.io/qt-6/resources.html>`_ overview for details on how to embed images and other resource files in the application's executable.

Use the :sip:ref:`~PyQt6.QtGui.QImageReader.supportedImageFormats` and :sip:ref:`~PyQt6.QtGui.QImageWriter.supportedImageFormats` functions to retrieve a complete list of the supported file formats.

If a high resolution version of the image exists (identified by the suffix ``@2x`` on the base name), it is automatically loaded and added with the *device pixel ratio* set to a value of 2. This can be disabled by setting the environment variable ``QT_HIGHDPI_DISABLE_2X_IMAGE_LOADING`` (see :sip:ref:`~PyQt6.QtGui.QImageReader`).

**Note:** When you add a non-empty filename to a :sip:ref:`~PyQt6.QtGui.QIcon`, the icon becomes non-null, even if the file doesn't exist or points to a corrupt file.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QIcon.addPixmap`, :sip:ref:`~PyQt6.QtGui.QPixmap.devicePixelRatio`.
