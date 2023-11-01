.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: 1a03cb4a8550aa93d7cdb13eb7855c6b

Sets the file name of :sip:ref:`~PyQt6.QtGui.QImageReader` to *fileName*. Internally, :sip:ref:`~PyQt6.QtGui.QImageReader` will create a :sip:ref:`~PyQt6.QtCore.QFile` object and open it in :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenMode.ReadOnly` mode, and use this when reading images.

If *fileName* does not include a file extension (e.g., .png or .bmp), :sip:ref:`~PyQt6.QtGui.QImageReader` will cycle through all supported extensions until it finds a matching file.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImageReader.fileName`, :sip:ref:`~PyQt6.QtGui.QImageReader.setDevice`, :sip:ref:`~PyQt6.QtGui.QImageReader.supportedImageFormats`.
