.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: (qreal)
    :digest: bcc95161fcbfcce629a003f90f589486

Sets the input volume to *volume*.

The volume is scaled linearly from ``0.0`` (silence) to ``1.0`` (full volume). Values outside this range will be clamped.

If the device does not support adjusting the input volume then *volume* will be ignored and the input volume will remain at 1.0.

The default volume is ``1.0``.

**Note:** Adjustments to the volume will change the volume of this audio stream, not the global volume.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.volume`.
