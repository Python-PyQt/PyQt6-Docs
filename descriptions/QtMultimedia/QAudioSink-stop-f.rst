.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: e02d6f17ae3de42a115a58d75d2fc62e

Stops the audio output, detaching from the system resource.

Sets :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.error` to QtAudio::NoError, :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.state` to QtAudio::StoppedState and emit :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.stateChanged` signal.
