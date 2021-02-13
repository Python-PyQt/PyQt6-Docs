.. sip:method-description::
    :status: todo
    :pysig: 26d03db616987dc18ab1da007d223ab3
    :realsig: (const QPixmap&)
    :digest: d84f15f110a6d61a0046874779835e80

Sets the brush pixmap to *pixmap*. The style is set to :sip:ref:`~PyQt6.QtCore.Qt.BrushStyle.TexturePattern`.

The current brush color will only have an effect for monochrome pixmaps, i.e. for :sip:ref:`~PyQt6.QtGui.QPixmap.depth` == 1 (`QBitmaps <https://doc.qt.io/qt-6/gui-changes-qt6.html#qbitmap>`_).

.. seealso:: :sip:ref:`~PyQt6.QtGui.QBrush.texture`.
