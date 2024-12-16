.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 045a6a9b78ad20171e8ff1b4955d0a71

Sets whether the frame should be *mirrored* around its vertical axis before displaying.

Transformations of ``QVideoFrame``, specifically rotation and mirroring, are used only for displaying the video frame and are applied on top of the surface transformation, which is determined by :sip:ref:`~PyQt6.QtMultimedia.QVideoFrameFormat`. Mirroring is applied after rotation.

Mirroring is typically needed for video frames coming from a front camera of a mobile device.

Default value is ``false``.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.mirrored`.
