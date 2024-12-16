.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: b01aa8088fe8687d90ac05f708313c3b

Sets if the surface is *mirrored* around its vertical axis.

Transformations of ``QVideoFrameFormat``, specifically, rotation and mirroring, can be determined by the orientation of the camera sensor, camera settings, or the orientation of the video stream.

Mirroring is applied after rotation.

Default value is ``false``.

**Note:** The mirroring here differs from :sip:ref:`~PyQt6.QtGui.QImage.mirrored`, as a vertically mirrored :sip:ref:`~PyQt6.QtGui.QImage` will be mirrored around its x-axis.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QVideoFrameFormat.isMirrored`.
