.. sip:method-description::
    :status: todo
    :pysig: 27ad3e71fea3cf39b84aef2d9d7ee0a3
    :realsig: (quint32) const
    :digest: b1c1e3f1647593e91611244368a0fc14

This function returns the shape of the glyph at a given *glyphIndex* in the underlying font if the :sip:ref:`~PyQt6.QtGui.QRawFont` is valid. Otherwise, it returns an empty :sip:ref:`~PyQt6.QtGui.QPainterPath`.

The returned glyph will always be unhinted.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QRawFont.alphaMapForGlyph`, :sip:ref:`~PyQt6.QtGui.QPainterPath.addText`.
