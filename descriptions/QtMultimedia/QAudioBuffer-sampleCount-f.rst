.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 91ea3d51b9187c1bce1c17c87d75a964

Returns the number of samples in this buffer.

If the format of this buffer has multiple channels, then this count includes all channels. This means that a stereo buffer with 1000 samples in total will have 500 left samples and 500 right samples (interleaved), and this function will return 1000.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QAudioBuffer.frameCount`.
