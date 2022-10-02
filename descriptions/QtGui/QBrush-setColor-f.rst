.. sip:method-description::
    :status: todo
    :pysig: 16a840407bcc3e0a0c7d7df60dad57e9
    :realsig: (const QColor&)
    :digest: 8bc2e5d20cf68aba1913da5c734be5fb

Sets the brush color to the given *color*.

Note that calling setColor() will not make a difference if the style is a gradient. The same is the case if the style is :sip:ref:`~PyQt6.QtCore.Qt.BrushStyle.TexturePattern` style unless the current texture is a :sip:ref:`~PyQt6.QtGui.QBitmap`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QBrush.color`.
