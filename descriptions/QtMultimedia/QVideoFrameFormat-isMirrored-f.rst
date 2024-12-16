.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: de22184d0b02f469f31911e3e3e0061a

Returns ``true`` if the surface is mirrored around its vertical axis.

Transformations of ``QVideoFrameFormat``, specifically, rotation and mirroring, can be determined by the orientation of the camera sensor, camera settings, or the orientation of the video stream.

Mirroring is applied after rotation.

**Note:** The mirroring here differs from :sip:ref:`~PyQt6.QtGui.QImage.mirrored`, as a vertically mirrored :sip:ref:`~PyQt6.QtGui.QImage` will be mirrored around its x-axis.
