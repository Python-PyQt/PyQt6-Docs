:orphan:

.. sip:class:: PyQt6.QtTextToSpeech.QTextToSpeech
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtTextToSpeech/QTextToSpeech-c.rst

    .. sip:enum:: PyQt6.QtTextToSpeech.QTextToSpeech.BoundaryHint
        :description: QtTextToSpeech/QTextToSpeech-BoundaryHint-e.rst

        .. sip:enum-member:: PyQt6.QtTextToSpeech.QTextToSpeech.BoundaryHint.Default
            :description: QtTextToSpeech/QTextToSpeech-BoundaryHint-Default-v.rst

        .. sip:enum-member:: PyQt6.QtTextToSpeech.QTextToSpeech.BoundaryHint.Immediate
            :description: QtTextToSpeech/QTextToSpeech-BoundaryHint-Immediate-v.rst

        .. sip:enum-member:: PyQt6.QtTextToSpeech.QTextToSpeech.BoundaryHint.Sentence
            :description: QtTextToSpeech/QTextToSpeech-BoundaryHint-Sentence-v.rst

        .. sip:enum-member:: PyQt6.QtTextToSpeech.QTextToSpeech.BoundaryHint.Utterance
            :description: QtTextToSpeech/QTextToSpeech-BoundaryHint-Utterance-v.rst

        .. sip:enum-member:: PyQt6.QtTextToSpeech.QTextToSpeech.BoundaryHint.Word
            :description: QtTextToSpeech/QTextToSpeech-BoundaryHint-Word-v.rst

    .. sip:enum:: PyQt6.QtTextToSpeech.QTextToSpeech.Capability
        :description: QtTextToSpeech/QTextToSpeech-Capability-e.rst

        .. sip:enum-member:: PyQt6.QtTextToSpeech.QTextToSpeech.Capability.None_
            :description: QtTextToSpeech/QTextToSpeech-Capability-None_-v.rst

        .. sip:enum-member:: PyQt6.QtTextToSpeech.QTextToSpeech.Capability.PauseResume
            :description: QtTextToSpeech/QTextToSpeech-Capability-PauseResume-v.rst

        .. sip:enum-member:: PyQt6.QtTextToSpeech.QTextToSpeech.Capability.Speak
            :description: QtTextToSpeech/QTextToSpeech-Capability-Speak-v.rst

        .. sip:enum-member:: PyQt6.QtTextToSpeech.QTextToSpeech.Capability.Synthesize
            :description: QtTextToSpeech/QTextToSpeech-Capability-Synthesize-v.rst

        .. sip:enum-member:: PyQt6.QtTextToSpeech.QTextToSpeech.Capability.WordByWordProgress
            :description: QtTextToSpeech/QTextToSpeech-Capability-WordByWordProgress-v.rst

    .. sip:enum:: PyQt6.QtTextToSpeech.QTextToSpeech.ErrorReason
        :description: QtTextToSpeech/QTextToSpeech-ErrorReason-e.rst

        .. sip:enum-member:: PyQt6.QtTextToSpeech.QTextToSpeech.ErrorReason.Configuration
            :description: QtTextToSpeech/QTextToSpeech-ErrorReason-Configuration-v.rst

        .. sip:enum-member:: PyQt6.QtTextToSpeech.QTextToSpeech.ErrorReason.Initialization
            :description: QtTextToSpeech/QTextToSpeech-ErrorReason-Initialization-v.rst

        .. sip:enum-member:: PyQt6.QtTextToSpeech.QTextToSpeech.ErrorReason.Input
            :description: QtTextToSpeech/QTextToSpeech-ErrorReason-Input-v.rst

        .. sip:enum-member:: PyQt6.QtTextToSpeech.QTextToSpeech.ErrorReason.NoError
            :description: QtTextToSpeech/QTextToSpeech-ErrorReason-NoError-v.rst

        .. sip:enum-member:: PyQt6.QtTextToSpeech.QTextToSpeech.ErrorReason.Playback
            :description: QtTextToSpeech/QTextToSpeech-ErrorReason-Playback-v.rst

    .. sip:enum:: PyQt6.QtTextToSpeech.QTextToSpeech.State
        :description: QtTextToSpeech/QTextToSpeech-State-e.rst

        .. sip:enum-member:: PyQt6.QtTextToSpeech.QTextToSpeech.State.Error
            :description: QtTextToSpeech/QTextToSpeech-State-Error-v.rst

        .. sip:enum-member:: PyQt6.QtTextToSpeech.QTextToSpeech.State.Paused
            :description: QtTextToSpeech/QTextToSpeech-State-Paused-v.rst

        .. sip:enum-member:: PyQt6.QtTextToSpeech.QTextToSpeech.State.Ready
            :description: QtTextToSpeech/QTextToSpeech-State-Ready-v.rst

        .. sip:enum-member:: PyQt6.QtTextToSpeech.QTextToSpeech.State.Speaking
            :description: QtTextToSpeech/QTextToSpeech-State-Speaking-v.rst

        .. sip:enum-member:: PyQt6.QtTextToSpeech.QTextToSpeech.State.Synthesizing
            :description: QtTextToSpeech/QTextToSpeech-State-Synthesizing-v.rst

    .. sip:method:: PyQt6.QtTextToSpeech.QTextToSpeech.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtTextToSpeech/QTextToSpeech-__init__-f.rst

    .. sip:method:: PyQt6.QtTextToSpeech.QTextToSpeech.__init__
        :args:
            Optional[str]
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtTextToSpeech/QTextToSpeech-__init__-f-3.rst

    .. sip:method:: PyQt6.QtTextToSpeech.QTextToSpeech.__init__
        :args:
            Optional[str]
            Dict[Optional[str], Any]
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtTextToSpeech/QTextToSpeech-__init__-f-4.rst

    .. sip:method:: PyQt6.QtTextToSpeech.QTextToSpeech.availableEngines
        :returns:
            List[str]
        :static:
        :description: QtTextToSpeech/QTextToSpeech-availableEngines-f.rst

    .. sip:method:: PyQt6.QtTextToSpeech.QTextToSpeech.availableLocales
        :returns:
            List[:sip:ref:`~PyQt6.QtCore.QLocale`]
        :description: QtTextToSpeech/QTextToSpeech-availableLocales-f.rst

    .. sip:method:: PyQt6.QtTextToSpeech.QTextToSpeech.availableVoices
        :returns:
            List[:sip:ref:`~PyQt6.QtTextToSpeech.QVoice`]
        :description: QtTextToSpeech/QTextToSpeech-availableVoices-f.rst

    .. sip:method:: PyQt6.QtTextToSpeech.QTextToSpeech.engine
        :returns:
            str
        :description: QtTextToSpeech/QTextToSpeech-engine-f.rst

    .. sip:method:: PyQt6.QtTextToSpeech.QTextToSpeech.engineCapabilities
        :returns:
            :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.Capability`
        :description: QtTextToSpeech/QTextToSpeech-engineCapabilities-f.rst

    .. sip:method:: PyQt6.QtTextToSpeech.QTextToSpeech.enqueue
        :args:
            Optional[str]
        :returns:
            int
        :description: QtTextToSpeech/QTextToSpeech-enqueue-f.rst

    .. sip:method:: PyQt6.QtTextToSpeech.QTextToSpeech.errorReason
        :returns:
            :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.ErrorReason`
        :description: QtTextToSpeech/QTextToSpeech-errorReason-f.rst

    .. sip:method:: PyQt6.QtTextToSpeech.QTextToSpeech.errorString
        :returns:
            str
        :description: QtTextToSpeech/QTextToSpeech-errorString-f.rst

    .. sip:method:: PyQt6.QtTextToSpeech.QTextToSpeech.locale
        :returns:
            :sip:ref:`~PyQt6.QtCore.QLocale`
        :description: QtTextToSpeech/QTextToSpeech-locale-f.rst

    .. sip:method:: PyQt6.QtTextToSpeech.QTextToSpeech.pause
        :args:
            boundaryHint: :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.BoundaryHint` = :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.BoundaryHint.Default`
        :description: QtTextToSpeech/QTextToSpeech-pause-f.rst

    .. sip:method:: PyQt6.QtTextToSpeech.QTextToSpeech.pitch
        :returns:
            float
        :description: QtTextToSpeech/QTextToSpeech-pitch-f.rst

    .. sip:method:: PyQt6.QtTextToSpeech.QTextToSpeech.rate
        :returns:
            float
        :description: QtTextToSpeech/QTextToSpeech-rate-f.rst

    .. sip:method:: PyQt6.QtTextToSpeech.QTextToSpeech.resume
        :description: QtTextToSpeech/QTextToSpeech-resume-f.rst

    .. sip:method:: PyQt6.QtTextToSpeech.QTextToSpeech.say
        :args:
            Optional[str]
        :description: QtTextToSpeech/QTextToSpeech-say-f-1.rst

    .. sip:method:: PyQt6.QtTextToSpeech.QTextToSpeech.setEngine
        :args:
            Optional[str]
            params: Dict[Optional[str], Any] = {}
        :returns:
            bool
        :description: QtTextToSpeech/QTextToSpeech-setEngine-f-1.rst

    .. sip:method:: PyQt6.QtTextToSpeech.QTextToSpeech.setLocale
        :args:
            :sip:ref:`~PyQt6.QtCore.QLocale`
        :description: QtTextToSpeech/QTextToSpeech-setLocale-f.rst

    .. sip:method:: PyQt6.QtTextToSpeech.QTextToSpeech.setPitch
        :args:
            float
        :description: QtTextToSpeech/QTextToSpeech-setPitch-f.rst

    .. sip:method:: PyQt6.QtTextToSpeech.QTextToSpeech.setRate
        :args:
            float
        :description: QtTextToSpeech/QTextToSpeech-setRate-f.rst

    .. sip:method:: PyQt6.QtTextToSpeech.QTextToSpeech.setVoice
        :args:
            :sip:ref:`~PyQt6.QtTextToSpeech.QVoice`
        :description: QtTextToSpeech/QTextToSpeech-setVoice-f.rst

    .. sip:method:: PyQt6.QtTextToSpeech.QTextToSpeech.setVolume
        :args:
            float
        :description: QtTextToSpeech/QTextToSpeech-setVolume-f.rst

    .. sip:method:: PyQt6.QtTextToSpeech.QTextToSpeech.state
        :returns:
            :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.State`
        :description: QtTextToSpeech/QTextToSpeech-state-f.rst

    .. sip:method:: PyQt6.QtTextToSpeech.QTextToSpeech.stop
        :args:
            boundaryHint: :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.BoundaryHint` = :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.BoundaryHint.Default`
        :description: QtTextToSpeech/QTextToSpeech-stop-f.rst

    .. sip:method:: PyQt6.QtTextToSpeech.QTextToSpeech.voice
        :returns:
            :sip:ref:`~PyQt6.QtTextToSpeech.QVoice`
        :description: QtTextToSpeech/QTextToSpeech-voice-f.rst

    .. sip:method:: PyQt6.QtTextToSpeech.QTextToSpeech.volume
        :returns:
            float
        :description: QtTextToSpeech/QTextToSpeech-volume-f.rst

    .. sip:signal:: PyQt6.QtTextToSpeech.QTextToSpeech.aboutToSynthesize
        :args:
            int
        :description: QtTextToSpeech/QTextToSpeech-aboutToSynthesize-s.rst

    .. sip:signal:: PyQt6.QtTextToSpeech.QTextToSpeech.engineChanged
        :args:
            Optional[str]
        :description: QtTextToSpeech/QTextToSpeech-engineChanged-s-1.rst

    .. sip:signal:: PyQt6.QtTextToSpeech.QTextToSpeech.errorOccurred
        :args:
            :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.ErrorReason`
            Optional[str]
        :description: QtTextToSpeech/QTextToSpeech-errorOccurred-s-1.rst

    .. sip:signal:: PyQt6.QtTextToSpeech.QTextToSpeech.localeChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QLocale`
        :description: QtTextToSpeech/QTextToSpeech-localeChanged-s.rst

    .. sip:signal:: PyQt6.QtTextToSpeech.QTextToSpeech.pitchChanged
        :args:
            float
        :description: QtTextToSpeech/QTextToSpeech-pitchChanged-s.rst

    .. sip:signal:: PyQt6.QtTextToSpeech.QTextToSpeech.rateChanged
        :args:
            float
        :description: QtTextToSpeech/QTextToSpeech-rateChanged-s.rst

    .. sip:signal:: PyQt6.QtTextToSpeech.QTextToSpeech.sayingWord
        :args:
            Optional[str]
            int
            int
            int
        :description: QtTextToSpeech/QTextToSpeech-sayingWord-s.rst

    .. sip:signal:: PyQt6.QtTextToSpeech.QTextToSpeech.stateChanged
        :args:
            :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.State`
        :description: QtTextToSpeech/QTextToSpeech-stateChanged-s.rst

    .. sip:signal:: PyQt6.QtTextToSpeech.QTextToSpeech.voiceChanged
        :args:
            :sip:ref:`~PyQt6.QtTextToSpeech.QVoice`
        :description: QtTextToSpeech/QTextToSpeech-voiceChanged-s.rst

    .. sip:signal:: PyQt6.QtTextToSpeech.QTextToSpeech.volumeChanged
        :args:
            float
        :description: QtTextToSpeech/QTextToSpeech-volumeChanged-s.rst
