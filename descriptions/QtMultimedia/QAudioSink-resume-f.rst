.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: d0777f9d1b212ac093c4025a42b1d1e6

Resumes processing audio data after a :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.suspend`.

Sets :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.state` to the state the sink had when :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.suspend` was called, and sets :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.error` to QAudioError::NoError. This function does nothing if the audio sink's state is not QtAudio::SuspendedState.
