.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (qsizetype)
    :digest: 66092a5888d80b7a27b76c76e39d68da

Sets the audio buffer size to *value* in bytes.

**Note:** This function can be called anytime before :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.start`. Calls to this are ignored after :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.start`. It should not be assumed that the buffer size set is the actual buffer size used - call :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.bufferSize` anytime after :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.start` to return the actual buffer size being used.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.bufferSize`, :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.setBufferFrameCount`.
