.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: ec4fd1c36324e0a5a95edf1fbcbdc6ff

Starts decoding the audio resource.

As data gets decoded, the :sip:ref:`~PyQt6.QtMultimedia.QAudioDecoder.bufferReady` signal will be emitted when enough data has been decoded. Calling :sip:ref:`~PyQt6.QtMultimedia.QAudioDecoder.read` will then return an audio buffer without blocking.

If you call :sip:ref:`~PyQt6.QtMultimedia.QAudioDecoder.read` before a buffer is ready, an invalid buffer will be returned, again without blocking.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QAudioDecoder.read`.
