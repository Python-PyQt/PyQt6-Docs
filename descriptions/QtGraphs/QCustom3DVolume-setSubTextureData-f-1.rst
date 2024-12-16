.. sip:method-description::
    :status: todo
    :pysig: 2d307c0895673213595df0bd0df47b50
    :realsig: (Qt::Axis, int, const QImage&)
    :digest: 27192e80e9867ad57bb1acd4ec64fae9

Sets a single 2D subtexture of the 3D texture along the specified *axis* of the volume. The *index* parameter specifies the subtexture to set. The source *image* must be in the format specified by the :sip:ref:`~PyQt6.QtGraphs.QCustom3DVolume.textureFormat` property if :sip:ref:`~PyQt6.QtGraphs.QCustom3DVolume.textureFormat` is indexed. If :sip:ref:`~PyQt6.QtGraphs.QCustom3DVolume.textureFormat` is :sip:ref:`~PyQt6.QtGui.QImage.Format.Format_ARGB32`, the image is converted to that format. The image must have the size of the cross-section of the volume texture along the specified axis. The orientation of the image should correspond to the orientation of the slice image produced by :sip:ref:`~PyQt6.QtGraphs.QCustom3DVolume.renderSlice` method along the same axis.

**Note:** Each x-dimension line of the data needs to be 32-bit aligned when targeting the y-axis or z-axis. If :sip:ref:`~PyQt6.QtGraphs.QCustom3DVolume.textureFormat` is :sip:ref:`~PyQt6.QtGui.QImage.Format.Format_Indexed8` and the :sip:ref:`~PyQt6.QtGraphs.QCustom3DVolume.textureWidth` value is not divisible by four, padding bytes might need to be added to each x-dimension line of the image to properly align it. The padding bytes should indicate a fully transparent color to avoid rendering artifacts. It is not guaranteed that :sip:ref:`~PyQt6.QtGui.QImage` will do this automatically.

.. seealso:: :sip:ref:`~PyQt6.QtGraphs.QCustom3DVolume.textureData`, :sip:ref:`~PyQt6.QtGraphs.QCustom3DVolume.renderSlice`.
