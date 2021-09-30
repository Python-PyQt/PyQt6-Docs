.. sip:method-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (qint64) const
    :digest: e5b3ea30e80df1de342169510fe6da43

Returns the number of frames required to represent *microseconds* in this format.

Note that some rounding may occur if *microseconds* is not an exact fraction of the :sip:ref:`~PyQt6.QtMultimedia.QAudioFormat.sampleRate`.
