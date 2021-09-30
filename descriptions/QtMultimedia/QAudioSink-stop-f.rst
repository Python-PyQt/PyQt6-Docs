.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 0f6fbd945dc4166430e221d27a8e50c4

Stops the audio output, detaching from the system resource.

Sets :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.error` to :sip:ref:`~PyQt6.QtMultimedia.QAudio.Error.NoError`, :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.state` to :sip:ref:`~PyQt6.QtMultimedia.QAudio.State.StoppedState` and emit :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.stateChanged` signal.
