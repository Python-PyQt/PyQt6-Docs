.. sip:method-description::
    :status: todo
    :pysig: 7f3af5685d06b3c562a73c51e37f2a3f
    :realsig: ()
    :digest: 341429fa9245ca055799d13b089f0d14

Returns a pointer to the internal :sip:ref:`~PyQt6.QtCore.QIODevice` being used to transfer data to the system's audio output. The device will already be open and :sip:ref:`~PyQt6.QtCore.QIODevice.write` can write data directly to it.

**Note:** The pointer will become invalid after the stream is stopped or if you start another stream.

If the :sip:ref:`~PyQt6.QtMultimedia.QAudioSink` is able to access the system's audio device, :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.state` returns QtAudio::IdleState, :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.error` returns QtAudio::NoError and the :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.stateChanged` signal is emitted.

If a problem occurs during this process, :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.error` returns QtAudio::OpenError, :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.state` returns QtAudio::StoppedState and the :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.stateChanged` signal is emitted.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QIODevice`.
