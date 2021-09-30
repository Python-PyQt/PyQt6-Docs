.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 0732aeb66ece546c258f8e9c7810bf74

Sets if the surface is *mirrored* around its vertical axis. This is typically needed for video frames coming from a front camera of a mobile device. Default value is false.

**Note:** The mirroring here differs from :sip:ref:`~PyQt6.QtGui.QImage.mirrored`, as a vertically mirrored :sip:ref:`~PyQt6.QtGui.QImage` will be mirrored around its x-axis.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QVideoFrameFormat.isMirrored`.
