.. sip:method-description::
    :status: todo
    :pysig: 9bbb98966a4b8c5842c249e11e89d9a4
    :realsig: (QtVideo::Rotation)
    :digest: 5e56ff33b8c994dc6aaea616974c4488

Sets the *angle* the frame should be rotated clockwise before displaying.

Transformations of ``QVideoFrame``, specifically rotation and mirroring, are used only for displaying the video frame and are applied on top of the surface transformation, which is determined by :sip:ref:`~PyQt6.QtMultimedia.QVideoFrameFormat`. Rotation is applied before mirroring.

Default value is ``QtVideo::Rotation::None``.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.rotation`.
