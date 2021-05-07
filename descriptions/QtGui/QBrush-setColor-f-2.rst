.. sip:method-description::
    :status: todo
    :pysig: 33f6fbfef44611b7e8172cb56a78f4c0
    :realsig: (const QColor&)
    :digest: cae366bd62411c2efc3bb6fb654c0b68

Sets the brush color to the given *color*.

Note that calling  will not make a difference if the style is a gradient. The same is the case if the style is :sip:ref:`~PyQt6.QtCore.Qt.BrushStyle.TexturePattern` style unless the current texture is a :sip:ref:`~PyQt6.QtGui.QBitmap`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QBrush.color`.
