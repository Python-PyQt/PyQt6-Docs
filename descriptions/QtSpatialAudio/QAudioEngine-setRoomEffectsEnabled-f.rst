.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 67fb1b1f84751f0e584625ea43a5592b

Enables room effects such as echos and reverb.

Enables room effects if *enabled* is true. Room effects will only apply if you create one or more :sip:ref:`~PyQt6.QtSpatialAudio.QAudioRoom` objects and the listener is inside at least one of the rooms. If the listener is inside multiple rooms, the room with the smallest volume will be used.

.. seealso:: :sip:ref:`~PyQt6.QtSpatialAudio.QAudioEngine.roomEffectsEnabled`.
