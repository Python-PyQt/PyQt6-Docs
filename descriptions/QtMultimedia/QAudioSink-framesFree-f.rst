.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 51c94c1e67b9e04a567169d7803bf378

Returns the number of free frames available in the audio buffer.

**Note:** The returned value is only valid while in QtAudio::ActiveState or QtAudio::IdleState state, otherwise returns zero.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.bytesFree`.
