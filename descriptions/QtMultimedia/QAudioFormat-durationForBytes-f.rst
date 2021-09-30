.. sip:method-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (qint32) const
    :digest: 103f1f711979b9ae2bf8362c904b9d06

Returns the number of microseconds represented by *bytes* in this format.

Returns 0 if this format is not valid.

Note that some rounding may occur if *bytes* is not an exact multiple of the number of bytes per frame.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QAudioFormat.bytesForDuration`.
