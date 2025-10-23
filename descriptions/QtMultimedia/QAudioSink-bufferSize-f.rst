.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 6431b5696b0d1dd65d627239ee443e1f

Returns the audio buffer size in bytes.

If called before :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.start`, returns platform default value. If called before ``start()`` but :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.setBufferSize` or :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.setBufferFrameCount` was called prior, returns value set by ``setBufferSize()`` or ``setBufferFrameCount()``. If called after ``start()``, returns the actual buffer size being used. This may not be what was set previously by ``setBufferSize()`` or ``setBufferFrameCount()``.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.setBufferSize`, :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.bufferFrameCount`.
