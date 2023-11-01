.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: f9b179bdd0fa594a74257d197544fa98

Constructs an icon from the file with the given *fileName*. The file will be loaded on demand.

If *fileName* contains a relative path (e.g. the filename only) the relevant file must be found relative to the runtime working directory.

The file name can refer to an actual file on disk or to one of the application's embedded resources. See the `Resource System <https://doc.qt.io/qt-6/resources.html>`_ overview for details on how to embed images and other resource files in the application's executable.

Use the :sip:ref:`~PyQt6.QtGui.QImageReader.supportedImageFormats` and :sip:ref:`~PyQt6.QtGui.QImageWriter.supportedImageFormats` functions to retrieve a complete list of the supported file formats.
