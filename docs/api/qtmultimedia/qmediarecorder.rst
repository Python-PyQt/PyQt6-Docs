:orphan:

.. sip:class:: PyQt6.QtMultimedia.QMediaRecorder
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtMultimedia/QMediaRecorder-c.rst

    .. sip:enum:: PyQt6.QtMultimedia.QMediaRecorder.EncodingMode
        :description: QtMultimedia/QMediaRecorder-EncodingMode-e.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QMediaRecorder.EncodingMode.AverageBitRateEncoding
            :description: QtMultimedia/QMediaRecorder-EncodingMode-AverageBitRateEncoding-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QMediaRecorder.EncodingMode.ConstantBitRateEncoding
            :description: QtMultimedia/QMediaRecorder-EncodingMode-ConstantBitRateEncoding-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QMediaRecorder.EncodingMode.ConstantQualityEncoding
            :description: QtMultimedia/QMediaRecorder-EncodingMode-ConstantQualityEncoding-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QMediaRecorder.EncodingMode.TwoPassEncoding
            :description: QtMultimedia/QMediaRecorder-EncodingMode-TwoPassEncoding-v.rst

    .. sip:enum:: PyQt6.QtMultimedia.QMediaRecorder.Error
        :description: QtMultimedia/QMediaRecorder-Error-e.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QMediaRecorder.Error.FormatError
            :description: QtMultimedia/QMediaRecorder-Error-FormatError-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QMediaRecorder.Error.LocationNotWritable
            :description: QtMultimedia/QMediaRecorder-Error-LocationNotWritable-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QMediaRecorder.Error.NoError
            :description: QtMultimedia/QMediaRecorder-Error-NoError-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QMediaRecorder.Error.OutOfSpaceError
            :description: QtMultimedia/QMediaRecorder-Error-OutOfSpaceError-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QMediaRecorder.Error.ResourceError
            :description: QtMultimedia/QMediaRecorder-Error-ResourceError-v.rst

    .. sip:enum:: PyQt6.QtMultimedia.QMediaRecorder.Quality
        :description: QtMultimedia/QMediaRecorder-Quality-e.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QMediaRecorder.Quality.HighQuality
            :description: QtMultimedia/QMediaRecorder-Quality-HighQuality-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QMediaRecorder.Quality.LowQuality
            :description: QtMultimedia/QMediaRecorder-Quality-LowQuality-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QMediaRecorder.Quality.NormalQuality
            :description: QtMultimedia/QMediaRecorder-Quality-NormalQuality-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QMediaRecorder.Quality.VeryHighQuality
            :description: QtMultimedia/QMediaRecorder-Quality-VeryHighQuality-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QMediaRecorder.Quality.VeryLowQuality
            :description: QtMultimedia/QMediaRecorder-Quality-VeryLowQuality-v.rst

    .. sip:enum:: PyQt6.QtMultimedia.QMediaRecorder.RecorderState
        :description: QtMultimedia/QMediaRecorder-RecorderState-e.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QMediaRecorder.RecorderState.PausedState
            :description: QtMultimedia/QMediaRecorder-RecorderState-PausedState-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QMediaRecorder.RecorderState.RecordingState
            :description: QtMultimedia/QMediaRecorder-RecorderState-RecordingState-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QMediaRecorder.RecorderState.StoppedState
            :description: QtMultimedia/QMediaRecorder-RecorderState-StoppedState-v.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaRecorder.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtMultimedia/QMediaRecorder-__init__-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaRecorder.actualLocation
        :returns:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtMultimedia/QMediaRecorder-actualLocation-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaRecorder.audioBitRate
        :returns:
            int
        :description: QtMultimedia/QMediaRecorder-audioBitRate-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaRecorder.audioChannelCount
        :returns:
            int
        :description: QtMultimedia/QMediaRecorder-audioChannelCount-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaRecorder.audioSampleRate
        :returns:
            int
        :description: QtMultimedia/QMediaRecorder-audioSampleRate-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaRecorder.captureSession
        :returns:
            :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession`
        :description: QtMultimedia/QMediaRecorder-captureSession-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaRecorder.duration
        :returns:
            int
        :description: QtMultimedia/QMediaRecorder-duration-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaRecorder.encodingMode
        :returns:
            :sip:ref:`~PyQt6.QtMultimedia.QMediaRecorder.EncodingMode`
        :description: QtMultimedia/QMediaRecorder-encodingMode-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaRecorder.error
        :returns:
            :sip:ref:`~PyQt6.QtMultimedia.QMediaRecorder.Error`
        :description: QtMultimedia/QMediaRecorder-error-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaRecorder.errorString
        :returns:
            str
        :description: QtMultimedia/QMediaRecorder-errorString-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaRecorder.isAvailable
        :returns:
            bool
        :description: QtMultimedia/QMediaRecorder-isAvailable-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaRecorder.mediaFormat
        :returns:
            :sip:ref:`~PyQt6.QtMultimedia.QMediaFormat`
        :description: QtMultimedia/QMediaRecorder-mediaFormat-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaRecorder.metaData
        :returns:
            :sip:ref:`~PyQt6.QtMultimedia.QMediaMetaData`
        :description: QtMultimedia/QMediaRecorder-metaData-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaRecorder.outputLocation
        :returns:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtMultimedia/QMediaRecorder-outputLocation-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaRecorder.pause
        :description: QtMultimedia/QMediaRecorder-pause-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaRecorder.quality
        :returns:
            :sip:ref:`~PyQt6.QtMultimedia.QMediaRecorder.Quality`
        :description: QtMultimedia/QMediaRecorder-quality-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaRecorder.record
        :description: QtMultimedia/QMediaRecorder-record-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaRecorder.recorderState
        :returns:
            :sip:ref:`~PyQt6.QtMultimedia.QMediaRecorder.RecorderState`
        :description: QtMultimedia/QMediaRecorder-recorderState-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaRecorder.setAudioBitRate
        :args:
            int
        :description: QtMultimedia/QMediaRecorder-setAudioBitRate-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaRecorder.setAudioChannelCount
        :args:
            int
        :description: QtMultimedia/QMediaRecorder-setAudioChannelCount-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaRecorder.setAudioSampleRate
        :args:
            int
        :description: QtMultimedia/QMediaRecorder-setAudioSampleRate-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaRecorder.setEncodingMode
        :args:
            :sip:ref:`~PyQt6.QtMultimedia.QMediaRecorder.EncodingMode`
        :description: QtMultimedia/QMediaRecorder-setEncodingMode-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaRecorder.setMediaFormat
        :args:
            :sip:ref:`~PyQt6.QtMultimedia.QMediaFormat`
        :description: QtMultimedia/QMediaRecorder-setMediaFormat-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaRecorder.setMetaData
        :args:
            :sip:ref:`~PyQt6.QtMultimedia.QMediaMetaData`
        :description: QtMultimedia/QMediaRecorder-setMetaData-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaRecorder.setOutputLocation
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtMultimedia/QMediaRecorder-setOutputLocation-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaRecorder.setQuality
        :args:
            :sip:ref:`~PyQt6.QtMultimedia.QMediaRecorder.Quality`
        :description: QtMultimedia/QMediaRecorder-setQuality-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaRecorder.setVideoBitRate
        :args:
            int
        :description: QtMultimedia/QMediaRecorder-setVideoBitRate-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaRecorder.setVideoFrameRate
        :args:
            float
        :description: QtMultimedia/QMediaRecorder-setVideoFrameRate-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaRecorder.setVideoResolution
        :args:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtMultimedia/QMediaRecorder-setVideoResolution-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaRecorder.setVideoResolution
        :args:
            int
            int
        :description: QtMultimedia/QMediaRecorder-setVideoResolution-f-1.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaRecorder.stop
        :description: QtMultimedia/QMediaRecorder-stop-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaRecorder.videoBitRate
        :returns:
            int
        :description: QtMultimedia/QMediaRecorder-videoBitRate-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaRecorder.videoFrameRate
        :returns:
            float
        :description: QtMultimedia/QMediaRecorder-videoFrameRate-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaRecorder.videoResolution
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtMultimedia/QMediaRecorder-videoResolution-f.rst

    .. sip:signal:: PyQt6.QtMultimedia.QMediaRecorder.actualLocationChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtMultimedia/QMediaRecorder-actualLocationChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QMediaRecorder.audioBitRateChanged
        :description: QtMultimedia/QMediaRecorder-audioBitRateChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QMediaRecorder.audioChannelCountChanged
        :description: QtMultimedia/QMediaRecorder-audioChannelCountChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QMediaRecorder.audioSampleRateChanged
        :description: QtMultimedia/QMediaRecorder-audioSampleRateChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QMediaRecorder.durationChanged
        :args:
            int
        :description: QtMultimedia/QMediaRecorder-durationChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QMediaRecorder.encodingModeChanged
        :description: QtMultimedia/QMediaRecorder-encodingModeChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QMediaRecorder.errorChanged
        :description: QtMultimedia/QMediaRecorder-errorChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QMediaRecorder.errorOccurred
        :args:
            :sip:ref:`~PyQt6.QtMultimedia.QMediaRecorder.Error`
            Optional[str]
        :description: QtMultimedia/QMediaRecorder-errorOccurred-s-1.rst

    .. sip:signal:: PyQt6.QtMultimedia.QMediaRecorder.mediaFormatChanged
        :description: QtMultimedia/QMediaRecorder-mediaFormatChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QMediaRecorder.metaDataChanged
        :description: QtMultimedia/QMediaRecorder-metaDataChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QMediaRecorder.qualityChanged
        :description: QtMultimedia/QMediaRecorder-qualityChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QMediaRecorder.recorderStateChanged
        :args:
            :sip:ref:`~PyQt6.QtMultimedia.QMediaRecorder.RecorderState`
        :description: QtMultimedia/QMediaRecorder-recorderStateChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QMediaRecorder.videoBitRateChanged
        :description: QtMultimedia/QMediaRecorder-videoBitRateChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QMediaRecorder.videoFrameRateChanged
        :description: QtMultimedia/QMediaRecorder-videoFrameRateChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QMediaRecorder.videoResolutionChanged
        :description: QtMultimedia/QMediaRecorder-videoResolutionChanged-s.rst
