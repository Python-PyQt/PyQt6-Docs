:orphan:

.. sip:class:: PyQt6.QtMultimedia.QAudioDecoder
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtMultimedia/QAudioDecoder-c.rst

    .. sip:enum:: PyQt6.QtMultimedia.QAudioDecoder.Error
        :description: QtMultimedia/QAudioDecoder-Error-e.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QAudioDecoder.Error.AccessDeniedError
            :description: QtMultimedia/QAudioDecoder-Error-AccessDeniedError-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QAudioDecoder.Error.FormatError
            :description: QtMultimedia/QAudioDecoder-Error-FormatError-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QAudioDecoder.Error.NoError
            :description: QtMultimedia/QAudioDecoder-Error-NoError-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QAudioDecoder.Error.NotSupportedError
            :description: QtMultimedia/QAudioDecoder-Error-NotSupportedError-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QAudioDecoder.Error.ResourceError
            :description: QtMultimedia/QAudioDecoder-Error-ResourceError-v.rst

    .. sip:method:: PyQt6.QtMultimedia.QAudioDecoder.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtMultimedia/QAudioDecoder-__init__-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QAudioDecoder.audioFormat
        :returns:
            :sip:ref:`~PyQt6.QtMultimedia.QAudioFormat`
        :description: QtMultimedia/QAudioDecoder-audioFormat-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QAudioDecoder.bufferAvailable
        :returns:
            bool
        :description: QtMultimedia/QAudioDecoder-bufferAvailable-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QAudioDecoder.duration
        :returns:
            int
        :description: QtMultimedia/QAudioDecoder-duration-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QAudioDecoder.error
        :returns:
            :sip:ref:`~PyQt6.QtMultimedia.QAudioDecoder.Error`
        :description: QtMultimedia/QAudioDecoder-error-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QAudioDecoder.errorString
        :returns:
            str
        :description: QtMultimedia/QAudioDecoder-errorString-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QAudioDecoder.isDecoding
        :returns:
            bool
        :description: QtMultimedia/QAudioDecoder-isDecoding-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QAudioDecoder.isSupported
        :returns:
            bool
        :description: QtMultimedia/QAudioDecoder-isSupported-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QAudioDecoder.position
        :returns:
            int
        :description: QtMultimedia/QAudioDecoder-position-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QAudioDecoder.read
        :returns:
            :sip:ref:`~PyQt6.QtMultimedia.QAudioBuffer`
        :description: QtMultimedia/QAudioDecoder-read-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QAudioDecoder.setAudioFormat
        :args:
            :sip:ref:`~PyQt6.QtMultimedia.QAudioFormat`
        :description: QtMultimedia/QAudioDecoder-setAudioFormat-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QAudioDecoder.setSource
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtMultimedia/QAudioDecoder-setSource-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QAudioDecoder.setSourceDevice
        :args:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :description: QtMultimedia/QAudioDecoder-setSourceDevice-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QAudioDecoder.source
        :returns:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtMultimedia/QAudioDecoder-source-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QAudioDecoder.sourceDevice
        :returns:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :description: QtMultimedia/QAudioDecoder-sourceDevice-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QAudioDecoder.start
        :description: QtMultimedia/QAudioDecoder-start-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QAudioDecoder.stop
        :description: QtMultimedia/QAudioDecoder-stop-f.rst

    .. sip:signal:: PyQt6.QtMultimedia.QAudioDecoder.bufferAvailableChanged
        :args:
            bool
        :description: QtMultimedia/QAudioDecoder-bufferAvailableChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QAudioDecoder.bufferReady
        :description: QtMultimedia/QAudioDecoder-bufferReady-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QAudioDecoder.durationChanged
        :args:
            int
        :description: QtMultimedia/QAudioDecoder-durationChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QAudioDecoder.error
        :description: QtMultimedia/QAudioDecoder-error-f-1.rst

    .. sip:signal:: PyQt6.QtMultimedia.QAudioDecoder.error
        :args:
            :sip:ref:`~PyQt6.QtMultimedia.QAudioDecoder.Error`
        :description: QtMultimedia/QAudioDecoder-error-f.rst

    .. sip:signal:: PyQt6.QtMultimedia.QAudioDecoder.finished
        :description: QtMultimedia/QAudioDecoder-finished-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QAudioDecoder.formatChanged
        :args:
            :sip:ref:`~PyQt6.QtMultimedia.QAudioFormat`
        :description: QtMultimedia/QAudioDecoder-formatChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QAudioDecoder.isDecodingChanged
        :args:
            bool
        :description: QtMultimedia/QAudioDecoder-isDecodingChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QAudioDecoder.positionChanged
        :args:
            int
        :description: QtMultimedia/QAudioDecoder-positionChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QAudioDecoder.sourceChanged
        :description: QtMultimedia/QAudioDecoder-sourceChanged-s.rst
