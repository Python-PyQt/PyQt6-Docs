:orphan:

.. sip:class:: PyQt6.QtGui.QImageWriter
    :description: QtGui/QImageWriter-c.rst

    .. sip:enum:: PyQt6.QtGui.QImageWriter.ImageWriterError
        :description: QtGui/QImageWriter-ImageWriterError-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QImageWriter.ImageWriterError.DeviceError
            :description: QtGui/QImageWriter-ImageWriterError-DeviceError-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QImageWriter.ImageWriterError.InvalidImageError
            :description: QtGui/QImageWriter-ImageWriterError-InvalidImageError-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QImageWriter.ImageWriterError.UnknownError
            :description: QtGui/QImageWriter-ImageWriterError-UnknownError-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QImageWriter.ImageWriterError.UnsupportedFormatError
            :description: QtGui/QImageWriter-ImageWriterError-UnsupportedFormatError-v.rst

    .. sip:method:: PyQt6.QtGui.QImageWriter.__init__
        :description: QtGui/QImageWriter-__init__-f.rst

    .. sip:method:: PyQt6.QtGui.QImageWriter.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :description: QtGui/QImageWriter-__init__-f-3.rst

    .. sip:method:: PyQt6.QtGui.QImageWriter.__init__
        :args:
            Optional[str]
            format: Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview] = QByteArray()
        :description: QtGui/QImageWriter-__init__-f-4.rst

    .. sip:method:: PyQt6.QtGui.QImageWriter.canWrite
        :returns:
            bool
        :description: QtGui/QImageWriter-canWrite-f.rst

    .. sip:method:: PyQt6.QtGui.QImageWriter.compression
        :returns:
            int
        :description: QtGui/QImageWriter-compression-f.rst

    .. sip:method:: PyQt6.QtGui.QImageWriter.device
        :returns:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :description: QtGui/QImageWriter-device-f.rst

    .. sip:method:: PyQt6.QtGui.QImageWriter.error
        :returns:
            :sip:ref:`~PyQt6.QtGui.QImageWriter.ImageWriterError`
        :description: QtGui/QImageWriter-error-f.rst

    .. sip:method:: PyQt6.QtGui.QImageWriter.errorString
        :returns:
            str
        :description: QtGui/QImageWriter-errorString-f.rst

    .. sip:method:: PyQt6.QtGui.QImageWriter.fileName
        :returns:
            str
        :description: QtGui/QImageWriter-fileName-f.rst

    .. sip:method:: PyQt6.QtGui.QImageWriter.format
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtGui/QImageWriter-format-f.rst

    .. sip:method:: PyQt6.QtGui.QImageWriter.imageFormatsForMimeType
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            List[:sip:ref:`~PyQt6.QtCore.QByteArray`]
        :static:
        :description: QtGui/QImageWriter-imageFormatsForMimeType-f-1.rst

    .. sip:method:: PyQt6.QtGui.QImageWriter.optimizedWrite
        :returns:
            bool
        :description: QtGui/QImageWriter-optimizedWrite-f.rst

    .. sip:method:: PyQt6.QtGui.QImageWriter.progressiveScanWrite
        :returns:
            bool
        :description: QtGui/QImageWriter-progressiveScanWrite-f.rst

    .. sip:method:: PyQt6.QtGui.QImageWriter.quality
        :returns:
            int
        :description: QtGui/QImageWriter-quality-f.rst

    .. sip:method:: PyQt6.QtGui.QImageWriter.setCompression
        :args:
            int
        :description: QtGui/QImageWriter-setCompression-f.rst

    .. sip:method:: PyQt6.QtGui.QImageWriter.setDevice
        :args:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :description: QtGui/QImageWriter-setDevice-f.rst

    .. sip:method:: PyQt6.QtGui.QImageWriter.setFileName
        :args:
            Optional[str]
        :description: QtGui/QImageWriter-setFileName-f-1.rst

    .. sip:method:: PyQt6.QtGui.QImageWriter.setFormat
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :description: QtGui/QImageWriter-setFormat-f-1.rst

    .. sip:method:: PyQt6.QtGui.QImageWriter.setOptimizedWrite
        :args:
            bool
        :description: QtGui/QImageWriter-setOptimizedWrite-f.rst

    .. sip:method:: PyQt6.QtGui.QImageWriter.setProgressiveScanWrite
        :args:
            bool
        :description: QtGui/QImageWriter-setProgressiveScanWrite-f.rst

    .. sip:method:: PyQt6.QtGui.QImageWriter.setQuality
        :args:
            int
        :description: QtGui/QImageWriter-setQuality-f.rst

    .. sip:method:: PyQt6.QtGui.QImageWriter.setSubType
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :description: QtGui/QImageWriter-setSubType-f-1.rst

    .. sip:method:: PyQt6.QtGui.QImageWriter.setText
        :args:
            Optional[str]
            Optional[str]
        :description: QtGui/QImageWriter-setText-f-1.rst

    .. sip:method:: PyQt6.QtGui.QImageWriter.setTransformation
        :args:
            :sip:ref:`~PyQt6.QtGui.QImageIOHandler.Transformation`
        :description: QtGui/QImageWriter-setTransformation-f-1.rst

    .. sip:method:: PyQt6.QtGui.QImageWriter.subType
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtGui/QImageWriter-subType-f.rst

    .. sip:method:: PyQt6.QtGui.QImageWriter.supportedImageFormats
        :returns:
            List[:sip:ref:`~PyQt6.QtCore.QByteArray`]
        :static:
        :description: QtGui/QImageWriter-supportedImageFormats-f.rst

    .. sip:method:: PyQt6.QtGui.QImageWriter.supportedMimeTypes
        :returns:
            List[:sip:ref:`~PyQt6.QtCore.QByteArray`]
        :static:
        :description: QtGui/QImageWriter-supportedMimeTypes-f.rst

    .. sip:method:: PyQt6.QtGui.QImageWriter.supportedSubTypes
        :returns:
            List[:sip:ref:`~PyQt6.QtCore.QByteArray`]
        :description: QtGui/QImageWriter-supportedSubTypes-f.rst

    .. sip:method:: PyQt6.QtGui.QImageWriter.supportsOption
        :args:
            :sip:ref:`~PyQt6.QtGui.QImageIOHandler.ImageOption`
        :returns:
            bool
        :description: QtGui/QImageWriter-supportsOption-f.rst

    .. sip:method:: PyQt6.QtGui.QImageWriter.transformation
        :returns:
            :sip:ref:`~PyQt6.QtGui.QImageIOHandler.Transformation`
        :description: QtGui/QImageWriter-transformation-f-1.rst

    .. sip:method:: PyQt6.QtGui.QImageWriter.write
        :args:
            :sip:ref:`~PyQt6.QtGui.QImage`
        :returns:
            bool
        :description: QtGui/QImageWriter-write-f.rst
