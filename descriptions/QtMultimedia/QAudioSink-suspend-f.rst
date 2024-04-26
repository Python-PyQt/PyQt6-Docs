.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 8c21bb4fbf5bf845c05ea1db183ad2e7

Stops processing audio data, preserving buffered audio data.

Sets :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.error` to QtAudio::NoError, :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.state` to QtAudio::SuspendedState and emits :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.stateChanged` signal.
