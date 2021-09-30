.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: (qreal)
    :digest: 9cb76273aaf0f8d662a605c89ad1231e

Sets the device pixel ratio for the image. This is the ratio between image pixels and device-independent pixels.

The default *scaleFactor* is 1.0. Setting it to something else has two effects:

QPainters that are opened on the image will be scaled. For example, painting on a 200x200 image if with a ratio of 2.0 will result in effective (device-independent) painting bounds of 100x100.

Code paths in Qt that calculate layout geometry based on the image size will take the ratio into account: :sip:ref:`~PyQt6.QtCore.QSize` layoutSize = image.\ :sip:ref:`~PyQt6.QtGui.QImage.size` / image.\ :sip:ref:`~PyQt6.QtGui.QImage.devicePixelRatio` The net effect of this is that the image is displayed as high-DPI image rather than a large image (see Drawing High Resolution Versions of Pixmaps and Images).

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.devicePixelRatio`, :sip:ref:`~PyQt6.QtGui.QImage.deviceIndependentSize`.
