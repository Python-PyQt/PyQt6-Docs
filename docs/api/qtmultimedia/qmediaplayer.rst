:orphan:

.. sip:class:: PyQt6.QtMultimedia.QMediaPlayer
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtMultimedia/QMediaPlayer-c.rst

    .. sip:enum:: PyQt6.QtMultimedia.QMediaPlayer.Error
        :description: QtMultimedia/QMediaPlayer-Error-e.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QMediaPlayer.Error.AccessDeniedError
            :description: QtMultimedia/QMediaPlayer-Error-AccessDeniedError-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QMediaPlayer.Error.FormatError
            :description: QtMultimedia/QMediaPlayer-Error-FormatError-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QMediaPlayer.Error.NetworkError
            :description: QtMultimedia/QMediaPlayer-Error-NetworkError-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QMediaPlayer.Error.NoError
            :description: QtMultimedia/QMediaPlayer-Error-NoError-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QMediaPlayer.Error.ResourceError
            :description: QtMultimedia/QMediaPlayer-Error-ResourceError-v.rst

    .. sip:enum:: PyQt6.QtMultimedia.QMediaPlayer.Loops
        :description: QtMultimedia/QMediaPlayer-Loops-e.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QMediaPlayer.Loops.Infinite
            :description: QtMultimedia/QMediaPlayer-Loops-Infinite-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QMediaPlayer.Loops.Once
            :description: QtMultimedia/QMediaPlayer-Loops-Once-v.rst

    .. sip:enum:: PyQt6.QtMultimedia.QMediaPlayer.MediaStatus
        :description: QtMultimedia/QMediaPlayer-MediaStatus-e.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QMediaPlayer.MediaStatus.BufferedMedia
            :description: QtMultimedia/QMediaPlayer-MediaStatus-BufferedMedia-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QMediaPlayer.MediaStatus.BufferingMedia
            :description: QtMultimedia/QMediaPlayer-MediaStatus-BufferingMedia-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QMediaPlayer.MediaStatus.EndOfMedia
            :description: QtMultimedia/QMediaPlayer-MediaStatus-EndOfMedia-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QMediaPlayer.MediaStatus.InvalidMedia
            :description: QtMultimedia/QMediaPlayer-MediaStatus-InvalidMedia-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QMediaPlayer.MediaStatus.LoadedMedia
            :description: QtMultimedia/QMediaPlayer-MediaStatus-LoadedMedia-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QMediaPlayer.MediaStatus.LoadingMedia
            :description: QtMultimedia/QMediaPlayer-MediaStatus-LoadingMedia-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QMediaPlayer.MediaStatus.NoMedia
            :description: QtMultimedia/QMediaPlayer-MediaStatus-NoMedia-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QMediaPlayer.MediaStatus.StalledMedia
            :description: QtMultimedia/QMediaPlayer-MediaStatus-StalledMedia-v.rst

    .. sip:enum:: PyQt6.QtMultimedia.QMediaPlayer.PlaybackState
        :description: QtMultimedia/QMediaPlayer-PlaybackState-e.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QMediaPlayer.PlaybackState.PausedState
            :description: QtMultimedia/QMediaPlayer-PlaybackState-PausedState-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QMediaPlayer.PlaybackState.PlayingState
            :description: QtMultimedia/QMediaPlayer-PlaybackState-PlayingState-v.rst

        .. sip:enum-member:: PyQt6.QtMultimedia.QMediaPlayer.PlaybackState.StoppedState
            :description: QtMultimedia/QMediaPlayer-PlaybackState-StoppedState-v.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtMultimedia/QMediaPlayer-__init__-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.activeAudioTrack
        :returns:
            int
        :description: QtMultimedia/QMediaPlayer-activeAudioTrack-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.activeSubtitleTrack
        :returns:
            int
        :description: QtMultimedia/QMediaPlayer-activeSubtitleTrack-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.activeVideoTrack
        :returns:
            int
        :description: QtMultimedia/QMediaPlayer-activeVideoTrack-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.audioOutput
        :returns:
            :sip:ref:`~PyQt6.QtMultimedia.QAudioOutput`
        :description: QtMultimedia/QMediaPlayer-audioOutput-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.audioTracks
        :returns:
            List[:sip:ref:`~PyQt6.QtMultimedia.QMediaMetaData`]
        :description: QtMultimedia/QMediaPlayer-audioTracks-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.bufferedTimeRange
        :returns:
            :sip:ref:`~PyQt6.QtMultimedia.QMediaTimeRange`
        :description: QtMultimedia/QMediaPlayer-bufferedTimeRange-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.bufferProgress
        :returns:
            float
        :description: QtMultimedia/QMediaPlayer-bufferProgress-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.duration
        :returns:
            int
        :description: QtMultimedia/QMediaPlayer-duration-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.error
        :returns:
            :sip:ref:`~PyQt6.QtMultimedia.QMediaPlayer.Error`
        :description: QtMultimedia/QMediaPlayer-error-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.errorString
        :returns:
            str
        :description: QtMultimedia/QMediaPlayer-errorString-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.hasAudio
        :returns:
            bool
        :description: QtMultimedia/QMediaPlayer-hasAudio-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.hasVideo
        :returns:
            bool
        :description: QtMultimedia/QMediaPlayer-hasVideo-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.isAvailable
        :returns:
            bool
        :description: QtMultimedia/QMediaPlayer-isAvailable-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.isPlaying
        :returns:
            bool
        :description: QtMultimedia/QMediaPlayer-isPlaying-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.isSeekable
        :returns:
            bool
        :description: QtMultimedia/QMediaPlayer-isSeekable-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.loops
        :returns:
            int
        :description: QtMultimedia/QMediaPlayer-loops-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.mediaStatus
        :returns:
            :sip:ref:`~PyQt6.QtMultimedia.QMediaPlayer.MediaStatus`
        :description: QtMultimedia/QMediaPlayer-mediaStatus-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.metaData
        :returns:
            :sip:ref:`~PyQt6.QtMultimedia.QMediaMetaData`
        :description: QtMultimedia/QMediaPlayer-metaData-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.pause
        :description: QtMultimedia/QMediaPlayer-pause-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.play
        :description: QtMultimedia/QMediaPlayer-play-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.playbackRate
        :returns:
            float
        :description: QtMultimedia/QMediaPlayer-playbackRate-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.playbackState
        :returns:
            :sip:ref:`~PyQt6.QtMultimedia.QMediaPlayer.PlaybackState`
        :description: QtMultimedia/QMediaPlayer-playbackState-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.position
        :returns:
            int
        :description: QtMultimedia/QMediaPlayer-position-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.setActiveAudioTrack
        :args:
            int
        :description: QtMultimedia/QMediaPlayer-setActiveAudioTrack-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.setActiveSubtitleTrack
        :args:
            int
        :description: QtMultimedia/QMediaPlayer-setActiveSubtitleTrack-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.setActiveVideoTrack
        :args:
            int
        :description: QtMultimedia/QMediaPlayer-setActiveVideoTrack-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.setAudioOutput
        :args:
            :sip:ref:`~PyQt6.QtMultimedia.QAudioOutput`
        :description: QtMultimedia/QMediaPlayer-setAudioOutput-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.setLoops
        :args:
            int
        :description: QtMultimedia/QMediaPlayer-setLoops-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.setPlaybackRate
        :args:
            float
        :description: QtMultimedia/QMediaPlayer-setPlaybackRate-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.setPosition
        :args:
            int
        :description: QtMultimedia/QMediaPlayer-setPosition-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.setSource
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtMultimedia/QMediaPlayer-setSource-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.setSourceDevice
        :args:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
            sourceUrl: :sip:ref:`~PyQt6.QtCore.QUrl` = QUrl()
        :description: QtMultimedia/QMediaPlayer-setSourceDevice-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.setVideoOutput
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :description: QtMultimedia/QMediaPlayer-setVideoOutput-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.setVideoSink
        :args:
            :sip:ref:`~PyQt6.QtMultimedia.QVideoSink`
        :description: QtMultimedia/QMediaPlayer-setVideoSink-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.source
        :returns:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtMultimedia/QMediaPlayer-source-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.sourceDevice
        :returns:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
        :description: QtMultimedia/QMediaPlayer-sourceDevice-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.stop
        :description: QtMultimedia/QMediaPlayer-stop-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.subtitleTracks
        :returns:
            List[:sip:ref:`~PyQt6.QtMultimedia.QMediaMetaData`]
        :description: QtMultimedia/QMediaPlayer-subtitleTracks-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.videoOutput
        :returns:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :description: QtMultimedia/QMediaPlayer-videoOutput-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.videoSink
        :returns:
            :sip:ref:`~PyQt6.QtMultimedia.QVideoSink`
        :description: QtMultimedia/QMediaPlayer-videoSink-f.rst

    .. sip:method:: PyQt6.QtMultimedia.QMediaPlayer.videoTracks
        :returns:
            List[:sip:ref:`~PyQt6.QtMultimedia.QMediaMetaData`]
        :description: QtMultimedia/QMediaPlayer-videoTracks-f.rst

    .. sip:signal:: PyQt6.QtMultimedia.QMediaPlayer.activeTracksChanged
        :description: QtMultimedia/QMediaPlayer-activeTracksChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QMediaPlayer.audioOutputChanged
        :description: QtMultimedia/QMediaPlayer-audioOutputChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QMediaPlayer.bufferProgressChanged
        :args:
            float
        :description: QtMultimedia/QMediaPlayer-bufferProgressChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QMediaPlayer.durationChanged
        :args:
            int
        :description: QtMultimedia/QMediaPlayer-durationChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QMediaPlayer.errorChanged
        :description: QtMultimedia/QMediaPlayer-errorChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QMediaPlayer.errorOccurred
        :args:
            :sip:ref:`~PyQt6.QtMultimedia.QMediaPlayer.Error`
            Optional[str]
        :description: QtMultimedia/QMediaPlayer-errorOccurred-s-1.rst

    .. sip:signal:: PyQt6.QtMultimedia.QMediaPlayer.hasAudioChanged
        :args:
            bool
        :description: QtMultimedia/QMediaPlayer-hasAudioChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QMediaPlayer.hasVideoChanged
        :args:
            bool
        :description: QtMultimedia/QMediaPlayer-hasVideoChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QMediaPlayer.loopsChanged
        :description: QtMultimedia/QMediaPlayer-loopsChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QMediaPlayer.mediaStatusChanged
        :args:
            :sip:ref:`~PyQt6.QtMultimedia.QMediaPlayer.MediaStatus`
        :description: QtMultimedia/QMediaPlayer-mediaStatusChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QMediaPlayer.metaDataChanged
        :description: QtMultimedia/QMediaPlayer-metaDataChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QMediaPlayer.playbackRateChanged
        :args:
            float
        :description: QtMultimedia/QMediaPlayer-playbackRateChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QMediaPlayer.playbackStateChanged
        :args:
            :sip:ref:`~PyQt6.QtMultimedia.QMediaPlayer.PlaybackState`
        :description: QtMultimedia/QMediaPlayer-playbackStateChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QMediaPlayer.playingChanged
        :args:
            bool
        :description: QtMultimedia/QMediaPlayer-playingChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QMediaPlayer.positionChanged
        :args:
            int
        :description: QtMultimedia/QMediaPlayer-positionChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QMediaPlayer.seekableChanged
        :args:
            bool
        :description: QtMultimedia/QMediaPlayer-seekableChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QMediaPlayer.sourceChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtMultimedia/QMediaPlayer-sourceChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QMediaPlayer.tracksChanged
        :description: QtMultimedia/QMediaPlayer-tracksChanged-s.rst

    .. sip:signal:: PyQt6.QtMultimedia.QMediaPlayer.videoOutputChanged
        :description: QtMultimedia/QMediaPlayer-videoOutputChanged-s.rst
