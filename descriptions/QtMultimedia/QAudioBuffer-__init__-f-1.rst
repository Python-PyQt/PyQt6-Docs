.. sip:method-description::
    :status: todo
    :pysig: 13e6d2ca2ccd25227ab6aed42fc783c5
    :realsig: (const QAudioBuffer&)
    :digest: 7143913bca31c214957b23a15cf4a83c

Creates a new audio buffer from *other*. Audio buffers are explicitly shared, you should call :sip:ref:`~PyQt6.QtMultimedia.QAudioBuffer.detach` on the buffer to make a copy that can then be modified.
