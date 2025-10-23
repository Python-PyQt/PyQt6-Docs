.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 27c2ccfd1bb609b6c9ad0ca2853514cf

Returns the amount of audio data available to read in bytes.

**Note:** returned value is only valid while in QtAudio::ActiveState or QtAudio::IdleState state, otherwise returns zero.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.framesAvailable`.
