.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 3883f3a6ba894d5b90ae44fae52f2811

Stops the audio output, detaching from the system resource.

Sets :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.error` to QtAudio::NoError, :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.state` to QtAudio::StoppedState and emit :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.stateChanged` signal.

**Note:** On Linux, and Darwin, this operation synchronously drains the underlying audio buffer, which may cause delays accordingly to the buffer payload. To reset all the buffers immediately, use the method :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.reset` instead.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.reset`.
