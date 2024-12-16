:orphan:

.. sip:class:: PyQt6.QtMultimedia.QSoundEffect
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtMultimedia/QSoundEffect-c.rst

    .. sip:enum:: PyQt6.QtMultimedia.QSoundEffect.Loop
        :description: QtMultimedia/QSoundEffect-Loop-e.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QSoundEffect.Loop.Infinite
            :description: QtMultimedia/QSoundEffect-Loop-Infinite-v.rst

    .. sip:enum:: PyQt6.QtMultimedia.QSoundEffect.Status
        :description: QtMultimedia/QSoundEffect-Status-e.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QSoundEffect.Status.Error
            :description: QtMultimedia/QSoundEffect-Status-Error-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QSoundEffect.Status.Loading
            :description: QtMultimedia/QSoundEffect-Status-Loading-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QSoundEffect.Status.Null
            :description: QtMultimedia/QSoundEffect-Status-Null-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QSoundEffect.Status.Ready
            :description: QtMultimedia/QSoundEffect-Status-Ready-v.rst

    .. sip:method:: PyQt6.QtMultimedia.QSoundEffect.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtMultimedia/QSoundEffect-__init__-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QSoundEffect.__init__
        :args:
            :sip:ref:`~PyQt6.QtMultimedia.QAudioDevice`
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtMultimedia/QSoundEffect-__init__-f-1.rst

    .. sip:method:: PyQt6.QtMultimedia.QSoundEffect.audioDevice
        :returns:
            :sip:ref:`~PyQt6.QtMultimedia.QAudioDevice`
        :description: QtMultimedia/QSoundEffect-audioDevice-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QSoundEffect.isLoaded
        :returns:
            bool
        :description: QtMultimedia/QSoundEffect-isLoaded-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QSoundEffect.isMuted
        :returns:
            bool
        :description: QtMultimedia/QSoundEffect-isMuted-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QSoundEffect.isPlaying
        :returns:
            bool
        :description: QtMultimedia/QSoundEffect-isPlaying-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QSoundEffect.loopCount
        :returns:
            int
        :description: QtMultimedia/QSoundEffect-loopCount-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QSoundEffect.loopsRemaining
        :returns:
            int
        :description: QtMultimedia/QSoundEffect-loopsRemaining-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QSoundEffect.play
        :description: QtMultimedia/QSoundEffect-play-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QSoundEffect.setAudioDevice
        :args:
            :sip:ref:`~PyQt6.QtMultimedia.QAudioDevice`
        :description: QtMultimedia/QSoundEffect-setAudioDevice-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QSoundEffect.setLoopCount
        :args:
            int
        :description: QtMultimedia/QSoundEffect-setLoopCount-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QSoundEffect.setMuted
        :args:
            bool
        :description: QtMultimedia/QSoundEffect-setMuted-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QSoundEffect.setSource
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtMultimedia/QSoundEffect-setSource-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QSoundEffect.setVolume
        :args:
            float
        :description: QtMultimedia/QSoundEffect-setVolume-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QSoundEffect.source
        :returns:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtMultimedia/QSoundEffect-source-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QSoundEffect.status
        :returns:
            :sip:ref:`~PyQt6.QtMultimedia.QSoundEffect.Status`
        :description: QtMultimedia/QSoundEffect-status-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QSoundEffect.stop
        :description: QtMultimedia/QSoundEffect-stop-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QSoundEffect.supportedMimeTypes
        :returns:
            list[str]
        :static:
        :description: QtMultimedia/QSoundEffect-supportedMimeTypes-f-1.rst

    .. sip:method:: PyQt6.QtMultimedia.QSoundEffect.volume
        :returns:
            float
        :description: QtMultimedia/QSoundEffect-volume-f.rst

    .. sip:signal:: PyQt6.QtMultimedia.QSoundEffect.audioDeviceChanged
        :description: QtMultimedia/QSoundEffect-audioDeviceChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QSoundEffect.loadedChanged
        :description: QtMultimedia/QSoundEffect-loadedChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QSoundEffect.loopCountChanged
        :description: QtMultimedia/QSoundEffect-loopCountChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QSoundEffect.loopsRemainingChanged
        :description: QtMultimedia/QSoundEffect-loopsRemainingChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QSoundEffect.mutedChanged
        :description: QtMultimedia/QSoundEffect-mutedChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QSoundEffect.playingChanged
        :description: QtMultimedia/QSoundEffect-playingChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QSoundEffect.sourceChanged
        :description: QtMultimedia/QSoundEffect-sourceChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QSoundEffect.statusChanged
        :description: QtMultimedia/QSoundEffect-statusChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QSoundEffect.volumeChanged
        :description: QtMultimedia/QSoundEffect-volumeChanged-s.rst
