.. sip:method-description::
    :status: todo
    :pysig: 9bbb98966a4b8c5842c249e11e89d9a4
    :realsig: () const
    :digest: 4cf5577107cdbf9ae5352b04d60648f0

Returns the angle the frame should be rotated clockwise before displaying.

Transformations of ``QVideoFrame``, specifically rotation and mirroring, are used only for displaying the video frame and are applied on top of the surface transformation, which is determined by :sip:ref:`~PyQt6.QtMultimedia.QVideoFrameFormat`. Rotation is applied before mirroring.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.setRotation`.
