.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (qsizetype)
    :digest: b2278a51b04f5bba5ec239a4954f757a

Sets the audio buffer size to *value* in frame count.

**Note:** This function can be called anytime before :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.start`. Calls to this are ignored after :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.start`. It should not be assumed that the buffer size set is the actual buffer size used - call :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.bufferFrameCount` anytime after :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.start` to return the actual buffer size being used.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.bufferFrameCount`, :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.setBufferSize`.
