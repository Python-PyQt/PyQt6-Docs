:orphan:

.. sip:class:: PyQt6.QtMultimedia.QImageCapture
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtMultimedia/QImageCapture-c.rst

    .. sip:enum:: PyQt6.QtMultimedia.QImageCapture.Error
        :description: QtMultimedia/QImageCapture-Error-e.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QImageCapture.Error.FormatError
            :description: QtMultimedia/QImageCapture-Error-FormatError-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QImageCapture.Error.NoError
            :description: QtMultimedia/QImageCapture-Error-NoError-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QImageCapture.Error.NotReadyError
            :description: QtMultimedia/QImageCapture-Error-NotReadyError-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QImageCapture.Error.NotSupportedFeatureError
            :description: QtMultimedia/QImageCapture-Error-NotSupportedFeatureError-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QImageCapture.Error.OutOfSpaceError
            :description: QtMultimedia/QImageCapture-Error-OutOfSpaceError-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QImageCapture.Error.ResourceError
            :description: QtMultimedia/QImageCapture-Error-ResourceError-v.rst

    .. sip:enum:: PyQt6.QtMultimedia.QImageCapture.FileFormat
        :description: QtMultimedia/QImageCapture-FileFormat-e.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QImageCapture.FileFormat.JPEG
            :description: QtMultimedia/QImageCapture-FileFormat-JPEG-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QImageCapture.FileFormat.PNG
            :description: QtMultimedia/QImageCapture-FileFormat-PNG-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QImageCapture.FileFormat.Tiff
            :description: QtMultimedia/QImageCapture-FileFormat-Tiff-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QImageCapture.FileFormat.UnspecifiedFormat
            :description: QtMultimedia/QImageCapture-FileFormat-UnspecifiedFormat-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QImageCapture.FileFormat.WebP
            :description: QtMultimedia/QImageCapture-FileFormat-WebP-v.rst

    .. sip:enum:: PyQt6.QtMultimedia.QImageCapture.Quality
        :description: QtMultimedia/QImageCapture-Quality-e.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QImageCapture.Quality.HighQuality
            :description: QtMultimedia/QImageCapture-Quality-HighQuality-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QImageCapture.Quality.LowQuality
            :description: QtMultimedia/QImageCapture-Quality-LowQuality-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QImageCapture.Quality.NormalQuality
            :description: QtMultimedia/QImageCapture-Quality-NormalQuality-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QImageCapture.Quality.VeryHighQuality
            :description: QtMultimedia/QImageCapture-Quality-VeryHighQuality-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QImageCapture.Quality.VeryLowQuality
            :description: QtMultimedia/QImageCapture-Quality-VeryLowQuality-v.rst

    .. sip:method:: PyQt6.QtMultimedia.QImageCapture.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtMultimedia/QImageCapture-__init__-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QImageCapture.addMetaData
        :args:
            :sip:ref:`~PyQt6.QtMultimedia.QMediaMetaData`
        :description: QtMultimedia/QImageCapture-addMetaData-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QImageCapture.capture
        :returns:
            int
        :description: QtMultimedia/QImageCapture-capture-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QImageCapture.captureSession
        :returns:
            :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession`
        :description: QtMultimedia/QImageCapture-captureSession-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QImageCapture.captureToFile
        :args:
            location: Optional[str] = ''
        :returns:
            int
        :description: QtMultimedia/QImageCapture-captureToFile-f-1.rst

    .. sip:method:: PyQt6.QtMultimedia.QImageCapture.error
        :returns:
            :sip:ref:`~PyQt6.QtMultimedia.QImageCapture.Error`
        :description: QtMultimedia/QImageCapture-error-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QImageCapture.errorString
        :returns:
            str
        :description: QtMultimedia/QImageCapture-errorString-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QImageCapture.fileFormat
        :returns:
            :sip:ref:`~PyQt6.QtMultimedia.QImageCapture.FileFormat`
        :description: QtMultimedia/QImageCapture-fileFormat-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QImageCapture.fileFormatDescription
        :args:
            :sip:ref:`~PyQt6.QtMultimedia.QImageCapture.FileFormat`
        :returns:
            str
        :static:
        :description: QtMultimedia/QImageCapture-fileFormatDescription-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QImageCapture.fileFormatName
        :args:
            :sip:ref:`~PyQt6.QtMultimedia.QImageCapture.FileFormat`
        :returns:
            str
        :static:
        :description: QtMultimedia/QImageCapture-fileFormatName-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QImageCapture.isAvailable
        :returns:
            bool
        :description: QtMultimedia/QImageCapture-isAvailable-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QImageCapture.isReadyForCapture
        :returns:
            bool
        :description: QtMultimedia/QImageCapture-isReadyForCapture-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QImageCapture.metaData
        :returns:
            :sip:ref:`~PyQt6.QtMultimedia.QMediaMetaData`
        :description: QtMultimedia/QImageCapture-metaData-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QImageCapture.quality
        :returns:
            :sip:ref:`~PyQt6.QtMultimedia.QImageCapture.Quality`
        :description: QtMultimedia/QImageCapture-quality-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QImageCapture.resolution
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtMultimedia/QImageCapture-resolution-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QImageCapture.setFileFormat
        :args:
            :sip:ref:`~PyQt6.QtMultimedia.QImageCapture.FileFormat`
        :description: QtMultimedia/QImageCapture-setFileFormat-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QImageCapture.setMetaData
        :args:
            :sip:ref:`~PyQt6.QtMultimedia.QMediaMetaData`
        :description: QtMultimedia/QImageCapture-setMetaData-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QImageCapture.setQuality
        :args:
            :sip:ref:`~PyQt6.QtMultimedia.QImageCapture.Quality`
        :description: QtMultimedia/QImageCapture-setQuality-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QImageCapture.setResolution
        :args:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtMultimedia/QImageCapture-setResolution-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QImageCapture.setResolution
        :args:
            int
            int
        :description: QtMultimedia/QImageCapture-setResolution-f-1.rst

    .. sip:method:: PyQt6.QtMultimedia.QImageCapture.supportedFormats
        :returns:
            List[:sip:ref:`~PyQt6.QtMultimedia.QImageCapture.FileFormat`]
        :static:
        :description: QtMultimedia/QImageCapture-supportedFormats-f.rst

    .. sip:signal:: PyQt6.QtMultimedia.QImageCapture.errorChanged
        :description: QtMultimedia/QImageCapture-errorChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QImageCapture.errorOccurred
        :args:
            int
            :sip:ref:`~PyQt6.QtMultimedia.QImageCapture.Error`
            Optional[str]
        :description: QtMultimedia/QImageCapture-errorOccurred-s-1.rst

    .. sip:signal:: PyQt6.QtMultimedia.QImageCapture.fileFormatChanged
        :description: QtMultimedia/QImageCapture-fileFormatChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QImageCapture.imageAvailable
        :args:
            int
            :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame`
        :description: QtMultimedia/QImageCapture-imageAvailable-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QImageCapture.imageCaptured
        :args:
            int
            :sip:ref:`~PyQt6.QtGui.QImage`
        :description: QtMultimedia/QImageCapture-imageCaptured-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QImageCapture.imageExposed
        :args:
            int
        :description: QtMultimedia/QImageCapture-imageExposed-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QImageCapture.imageSaved
        :args:
            int
            Optional[str]
        :description: QtMultimedia/QImageCapture-imageSaved-s-1.rst

    .. sip:signal:: PyQt6.QtMultimedia.QImageCapture.metaDataChanged
        :description: QtMultimedia/QImageCapture-metaDataChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QImageCapture.qualityChanged
        :description: QtMultimedia/QImageCapture-qualityChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QImageCapture.readyForCaptureChanged
        :args:
            bool
        :description: QtMultimedia/QImageCapture-readyForCaptureChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QImageCapture.resolutionChanged
        :description: QtMultimedia/QImageCapture-resolutionChanged-s.rst
