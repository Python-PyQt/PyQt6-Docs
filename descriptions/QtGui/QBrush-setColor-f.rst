.. sip:method-description::
    :status: todo
    :pysig: 16a840407bcc3e0a0c7d7df60dad57e9
    :realsig: (const QColor&)
    :digest: cae366bd62411c2efc3bb6fb654c0b68

Sets the brush color to the given *color*.

Note that calling  will not make a difference if the style is a gradient. The same is the case if the style is :sip:ref:`~PyQt6.QtCore.Qt.BrushStyle.TexturePattern` style unless the current texture is a `QBitmap <https://doc.qt.io/qt-6/gui-changes-qt6.html#qbitmap>`_.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QBrush.color`.
