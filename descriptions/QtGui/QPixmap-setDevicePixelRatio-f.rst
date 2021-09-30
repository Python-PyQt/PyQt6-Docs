.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: (qreal)
    :digest: 2fd2a1acc57796e651b083232c43a118

Sets the device pixel ratio for the pixmap. This is the ratio between image pixels and device-independent pixels.

The default *scaleFactor* is 1.0. Setting it to something else has two effects:

QPainters that are opened on the pixmap will be scaled. For example, painting on a 200x200 image if with a ratio of 2.0 will result in effective (device-independent) painting bounds of 100x100.

Code paths in Qt that calculate layout geometry based on the pixmap size will take the ratio into account: :sip:ref:`~PyQt6.QtCore.QSize` layoutSize = pixmap.\ :sip:ref:`~PyQt6.QtGui.QPixmap.size` / pixmap.\ :sip:ref:`~PyQt6.QtGui.QPixmap.devicePixelRatio` The net effect of this is that the pixmap is displayed as high-DPI pixmap rather than a large pixmap (see Drawing High Resolution Versions of Pixmaps and Images).

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPixmap.devicePixelRatio`, :sip:ref:`~PyQt6.QtGui.QPixmap.deviceIndependentSize`.
