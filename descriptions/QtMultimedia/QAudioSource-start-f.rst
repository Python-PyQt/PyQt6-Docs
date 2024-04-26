.. sip:method-description::
    :status: todo
    :pysig: 7f3af5685d06b3c562a73c51e37f2a3f
    :realsig: ()
    :digest: bd42eff62c8af99163f7bafd9fc91a0d

Returns a pointer to the internal :sip:ref:`~PyQt6.QtCore.QIODevice` being used to transfer data from the system's audio input. The device will already be open and :sip:ref:`~PyQt6.QtCore.QIODevice.read` can read data directly from it.

**Note:** The pointer will become invalid after the stream is stopped or if you start another stream.

If the :sip:ref:`~PyQt6.QtMultimedia.QAudioSource` is able to access the system's audio device, :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.state` returns QtAudio::IdleState, :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.error` returns QtAudio::NoError and the :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.stateChanged` signal is emitted.

If a problem occurs during this process, :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.error` returns QtAudio::OpenError, :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.state` returns QtAudio::StoppedState and the :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.stateChanged` signal is emitted.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QIODevice`.
