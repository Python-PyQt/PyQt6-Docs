.. sip:method-description::
    :status: todo
    :pysig: 9bbb98966a4b8c5842c249e11e89d9a4
    :realsig: (QtVideo::Rotation)
    :digest: 4ef5c74a075ec572bc1b84591cfb26bb

Sets the *angle* by which the surface is rotated clockwise.

Transformations of ``QVideoFrameFormat``, specifically, rotation and mirroring, can be determined by the orientation of the camera sensor, camera settings, or the orientation of the video stream.

Rotation is applied before mirroring.

Default value is ``QtVideo::Rotation::None``.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QVideoFrameFormat.rotation`.
