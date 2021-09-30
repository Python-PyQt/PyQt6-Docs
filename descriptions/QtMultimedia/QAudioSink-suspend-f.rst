.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 96b67149e42c5809a1fdb454d720ed24

Stops processing audio data, preserving buffered audio data.

Sets :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.error` to :sip:ref:`~PyQt6.QtMultimedia.QAudio.Error.NoError`, :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.state` to :sip:ref:`~PyQt6.QtMultimedia.QAudio.State.SuspendedState` and emits :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.stateChanged` signal.
