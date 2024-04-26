.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: (qreal)
    :digest: 1ac811213f3c4e713d5d20c37d8ea4e8

Sets the output volume to *volume*.

The volume is scaled linearly from ``0.0`` (silence) to ``1.0`` (full volume). Values outside this range will be clamped.

The default volume is ``1.0``.

**Note:** Adjustments to the volume will change the volume of this audio stream, not the global volume.

UI volume controls should usually be scaled non-linearly. For example, using a logarithmic scale will produce linear changes in perceived loudness, which is what a user would normally expect from a volume control. See QtAudio::convertVolume() for more details.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.volume`.
