.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 96460149bea7d5a242bd4920f4b536ff

Returns the amount of audio data available to read in bytes.

Note: returned value is only valid while in :sip:ref:`~PyQt6.QtMultimedia.QAudio.State.ActiveState` or :sip:ref:`~PyQt6.QtMultimedia.QAudio.State.IdleState` state, otherwise returns zero.
