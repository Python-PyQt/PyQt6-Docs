.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 7f3f3c99d2a1b6251bf2462a0286e0d0

Returns the audio buffer size in frames.

If called before :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.start`, returns platform default value. If called before ``start()`` but :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.setBufferSize` or :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.setBufferFrameCount` was called prior, returns value set by ``setBufferSize()`` or ``setBufferFrameCount()``. If called after ``start()``, returns the actual buffer size being used. This may not be what was set previously by ``setBufferSize()`` or ``setBufferFrameCount()``.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.setBufferFrameCount`, :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.bufferSize`.
