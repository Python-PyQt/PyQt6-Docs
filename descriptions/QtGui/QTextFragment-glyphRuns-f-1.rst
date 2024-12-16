.. sip:method-description::
    :status: todo
    :pysig: 4406c5b73d5751f931819ac762b8edbe
    :realsig: (int, int) const
    :digest: 1be78b7c025458136100da392cebf6f0

Returns the glyphs corresponding to *len* characters of this text fragment starting at position *pos*. The positions of the glyphs are relative to the position of the :sip:ref:`~PyQt6.QtGui.QTextBlock`'s layout.

If *pos* is less than zero, it will default to the start of the :sip:ref:`~PyQt6.QtGui.QTextFragment`. If *len* is less than zero, it will default to the length of the fragment.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QGlyphRun`, :sip:ref:`~PyQt6.QtGui.QTextBlock.layout`, :sip:ref:`~PyQt6.QtGui.QTextLayout.position`, :sip:ref:`~PyQt6.QtGui.QPainter.drawGlyphRun`.
