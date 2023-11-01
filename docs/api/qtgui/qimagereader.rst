:orphan:

.. sip:class:: PyQt6.QtGui.QImageReader
    :description: QtGui/QImageReader-c.rst

    .. sip:enum:: PyQt6.QtGui.QImageReader.ImageReaderError
        :description: QtGui/QImageReader-ImageReaderError-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QImageReader.ImageReaderError.DeviceError
            :description: QtGui/QImageReader-ImageReaderError-DeviceError-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QImageReader.ImageReaderError.FileNotFoundError
            :description: QtGui/QImageReader-ImageReaderError-FileNotFoundError-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QImageReader.ImageReaderError.InvalidDataError
            :description: QtGui/QImageReader-ImageReaderError-InvalidDataError-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QImageReader.ImageReaderError.UnknownError
            :description: QtGui/QImageReader-ImageReaderError-UnknownError-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QImageReader.ImageReaderError.UnsupportedFormatError
            :description: QtGui/QImageReader-ImageReaderError-UnsupportedFormatError-v.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.__init__
        :description: QtGui/QImageReader-__init__-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
            format: Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview] = QByteArray()
        :description: QtGui/QImageReader-__init__-f-3.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.__init__
        :args:
            Optional[str]
            format: Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview] = QByteArray()
        :description: QtGui/QImageReader-__init__-f-4.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.allocationLimit
        :returns:
            int
        :static:
        :description: QtGui/QImageReader-allocationLimit-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.autoDetectImageFormat
        :returns:
            bool
        :description: QtGui/QImageReader-autoDetectImageFormat-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.autoTransform
        :returns:
            bool
        :description: QtGui/QImageReader-autoTransform-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.backgroundColor
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :description: QtGui/QImageReader-backgroundColor-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.canRead
        :returns:
            bool
        :description: QtGui/QImageReader-canRead-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.clipRect
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtGui/QImageReader-clipRect-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.currentImageNumber
        :returns:
            int
        :description: QtGui/QImageReader-currentImageNumber-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.currentImageRect
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtGui/QImageReader-currentImageRect-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.decideFormatFromContent
        :returns:
            bool
        :description: QtGui/QImageReader-decideFormatFromContent-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.device
        :returns:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :description: QtGui/QImageReader-device-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.error
        :returns:
            :sip:ref:`~PyQt6.QtGui.QImageReader.ImageReaderError`
        :description: QtGui/QImageReader-error-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.errorString
        :returns:
            str
        :description: QtGui/QImageReader-errorString-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.fileName
        :returns:
            str
        :description: QtGui/QImageReader-fileName-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.format
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtGui/QImageReader-format-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.imageCount
        :returns:
            int
        :description: QtGui/QImageReader-imageCount-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.imageFormat
        :returns:
            :sip:ref:`~PyQt6.QtGui.QImage.Format`
        :description: QtGui/QImageReader-imageFormat-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.imageFormat
        :args:
            Optional[str]
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :static:
        :description: QtGui/QImageReader-imageFormat-f-3.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.imageFormat
        :args:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :static:
        :description: QtGui/QImageReader-imageFormat-f-2.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.imageFormatsForMimeType
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            List[:sip:ref:`~PyQt6.QtCore.QByteArray`]
        :static:
        :description: QtGui/QImageReader-imageFormatsForMimeType-f-1.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.jumpToImage
        :args:
            int
        :returns:
            bool
        :description: QtGui/QImageReader-jumpToImage-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.jumpToNextImage
        :returns:
            bool
        :description: QtGui/QImageReader-jumpToNextImage-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.loopCount
        :returns:
            int
        :description: QtGui/QImageReader-loopCount-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.nextImageDelay
        :returns:
            int
        :description: QtGui/QImageReader-nextImageDelay-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.quality
        :returns:
            int
        :description: QtGui/QImageReader-quality-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.read
        :returns:
            :sip:ref:`~PyQt6.QtGui.QImage`
        :description: QtGui/QImageReader-read-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.read
        :args:
            :sip:ref:`~PyQt6.QtGui.QImage`
        :returns:
            bool
        :description: QtGui/QImageReader-read-f-1.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.scaledClipRect
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtGui/QImageReader-scaledClipRect-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.scaledSize
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtGui/QImageReader-scaledSize-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.setAllocationLimit
        :args:
            int
        :static:
        :description: QtGui/QImageReader-setAllocationLimit-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.setAutoDetectImageFormat
        :args:
            bool
        :description: QtGui/QImageReader-setAutoDetectImageFormat-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.setAutoTransform
        :args:
            bool
        :description: QtGui/QImageReader-setAutoTransform-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.setBackgroundColor
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
        :description: QtGui/QImageReader-setBackgroundColor-f-2.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.setClipRect
        :args:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtGui/QImageReader-setClipRect-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.setDecideFormatFromContent
        :args:
            bool
        :description: QtGui/QImageReader-setDecideFormatFromContent-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.setDevice
        :args:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :description: QtGui/QImageReader-setDevice-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.setFileName
        :args:
            Optional[str]
        :description: QtGui/QImageReader-setFileName-f-1.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.setFormat
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :description: QtGui/QImageReader-setFormat-f-1.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.setQuality
        :args:
            int
        :description: QtGui/QImageReader-setQuality-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.setScaledClipRect
        :args:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtGui/QImageReader-setScaledClipRect-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.setScaledSize
        :args:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtGui/QImageReader-setScaledSize-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.size
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtGui/QImageReader-size-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.subType
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtGui/QImageReader-subType-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.supportedImageFormats
        :returns:
            List[:sip:ref:`~PyQt6.QtCore.QByteArray`]
        :static:
        :description: QtGui/QImageReader-supportedImageFormats-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.supportedMimeTypes
        :returns:
            List[:sip:ref:`~PyQt6.QtCore.QByteArray`]
        :static:
        :description: QtGui/QImageReader-supportedMimeTypes-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.supportedSubTypes
        :returns:
            List[:sip:ref:`~PyQt6.QtCore.QByteArray`]
        :description: QtGui/QImageReader-supportedSubTypes-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.supportsAnimation
        :returns:
            bool
        :description: QtGui/QImageReader-supportsAnimation-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.supportsOption
        :args:
            :sip:ref:`~PyQt6.QtGui.QImageIOHandler.ImageOption`
        :returns:
            bool
        :description: QtGui/QImageReader-supportsOption-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.text
        :args:
            Optional[str]
        :returns:
            str
        :description: QtGui/QImageReader-text-f-1.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.textKeys
        :returns:
            List[str]
        :description: QtGui/QImageReader-textKeys-f.rst

    .. sip:method:: PyQt6.QtGui.QImageReader.transformation
        :returns:
            :sip:ref:`~PyQt6.QtGui.QImageIOHandler.Transformation`
        :description: QtGui/QImageReader-transformation-f-1.rst
