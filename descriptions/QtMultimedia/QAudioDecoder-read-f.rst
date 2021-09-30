.. sip:method-description::
    :status: todo
    :pysig: 13e6d2ca2ccd25227ab6aed42fc783c5
    :realsig: () const
    :digest: 0b6eda29a7bb777e33b6bf7d816164c9

Read a buffer from the decoder, if one is available. Returns an invalid buffer if there are no decoded buffers currently available, or on failure. In both cases this function will not block.

You should either respond to the :sip:ref:`~PyQt6.QtMultimedia.QAudioDecoder.bufferReady` signal or check the :sip:ref:`~PyQt6.QtMultimedia.QAudioDecoder.bufferAvailable` function before calling  to make sure you get useful data.
