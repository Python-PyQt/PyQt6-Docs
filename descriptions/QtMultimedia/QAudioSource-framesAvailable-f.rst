.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: d792fdb1d3c3be4a364e3993d53f1649

Returns the amount of audio data available to read in frames.

Note: returned value is only valid while in QtAudio::ActiveState or QtAudio::IdleState state, otherwise returns zero.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.bytesAvailable`.
