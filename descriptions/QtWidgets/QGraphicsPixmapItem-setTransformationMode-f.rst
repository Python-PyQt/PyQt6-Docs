.. sip:method-description::
    :status: todo
    :pysig: 0d89e4199380cd15948a3162cda8667a
    :realsig: (Qt::TransformationMode)
    :digest: 7e115209cd3e8e873226a66e0800e135

Sets the pixmap item's transformation mode to *mode*, and toggles an update of the item. The default mode is :sip:ref:`~PyQt6.QtCore.Qt.TransformationMode.FastTransformation`, which provides quick transformation with no smoothing.

:sip:ref:`~PyQt6.QtCore.Qt.TransformationMode.SmoothTransformation` enables :sip:ref:`~PyQt6.QtGui.QPainter.RenderHints.SmoothPixmapTransform` on the painter, and the quality depends on the platform and viewport. The result is usually not as good as calling QPixmap::scale() directly.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsPixmapItem.transformationMode`.
