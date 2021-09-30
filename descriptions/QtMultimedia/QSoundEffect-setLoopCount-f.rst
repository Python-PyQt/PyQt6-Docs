.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 9e8046482e46555b2764340ca96c21a0

Set the total number of times to play this sound effect to *loopCount*.

Setting the loop count to 0 or 1 means the sound effect will be played only once; pass ``QSoundEffect::Infinite`` to repeat indefinitely. The loop count can be changed while the sound effect is playing, in which case it will update the remaining loops to the new *loopCount*.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QSoundEffect.loopCount`, :sip:ref:`~PyQt6.QtMultimedia.QSoundEffect.loopsRemaining`.
