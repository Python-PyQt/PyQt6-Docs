.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: c5a06db809624de001f450f6806778be

Returns the number of free bytes available in the audio buffer.

**Note:** The returned value is only valid while in :sip:ref:`~PyQt6.QtMultimedia.QAudio.State.ActiveState` or :sip:ref:`~PyQt6.QtMultimedia.QAudio.State.IdleState` state, otherwise returns zero.
