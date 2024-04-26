.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 18f052f3248dc13c80355ccacb300860

Returns the number of free bytes available in the audio buffer.

**Note:** The returned value is only valid while in QtAudio::ActiveState or QtAudio::IdleState state, otherwise returns zero.
