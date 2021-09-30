.. sip:method-description::
    :status: todo
    :pysig: 7f3af5685d06b3c562a73c51e37f2a3f
    :realsig: ()
    :digest: df49d3f1d91694c2c518a4adc33289b7

Returns a pointer to the internal :sip:ref:`~PyQt6.QtCore.QIODevice` being used to transfer data to the system's audio output. The device will already be open and :sip:ref:`~PyQt6.QtCore.QIODevice.write` can write data directly to it.

**Note:** The pointer will become invalid after the stream is stopped or if you start another stream.

If the :sip:ref:`~PyQt6.QtMultimedia.QAudioSink` is able to access the system's audio device, :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.state` returns :sip:ref:`~PyQt6.QtMultimedia.QAudio.State.IdleState`, :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.error` returns :sip:ref:`~PyQt6.QtMultimedia.QAudio.Error.NoError` and the :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.stateChanged` signal is emitted.

If a problem occurs during this process, :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.error` returns :sip:ref:`~PyQt6.QtMultimedia.QAudio.Error.OpenError`, :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.state` returns :sip:ref:`~PyQt6.QtMultimedia.QAudio.State.StoppedState` and the :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.stateChanged` signal is emitted.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QIODevice`.
