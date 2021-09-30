.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: (float)
    :digest: 9c6a451d45bf18387cf8b24bc22536ea

Sets the sound effect volume to *volume*.

The volume is scaled linearly from ``0.0`` (silence) to ``1.0`` (full volume). Values outside this range will be clamped.

The default volume is ``1.0``.

UI volume controls should usually be scaled non-linearly. For example, using a logarithmic scale will produce linear changes in perceived loudness, which is what a user would normally expect from a volume control. See :sip:ref:`~PyQt6.QtMultimedia.QAudio.convertVolume` for more details.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QSoundEffect.volume`.
