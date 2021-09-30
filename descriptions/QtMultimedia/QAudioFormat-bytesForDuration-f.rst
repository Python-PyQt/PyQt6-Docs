.. sip:method-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (qint64) const
    :digest: 5335dae50b2ec32f78c7ea2712bbf49c

Returns the number of bytes required for this audio format for *microseconds*.

Returns 0 if this format is not valid.

Note that some rounding may occur if *microseconds* is not an exact fraction of the :sip:ref:`~PyQt6.QtMultimedia.QAudioFormat.sampleRate`.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QAudioFormat.durationForBytes`.
