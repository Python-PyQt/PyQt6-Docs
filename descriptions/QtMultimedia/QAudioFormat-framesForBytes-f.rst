.. sip:method-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (qint32) const
    :digest: a7d0048843b90641e4645c7b500f8de9

Returns the number of frames represented by *byteCount* in this format.

Note that some rounding may occur if *byteCount* is not an exact multiple of the number of bytes per frame.

Each frame has one sample per channel.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QAudioFormat.framesForDuration`.
