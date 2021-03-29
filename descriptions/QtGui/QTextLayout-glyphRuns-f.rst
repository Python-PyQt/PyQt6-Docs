.. sip:method-description::
    :status: todo
    :pysig: f45d770c6ff53d422712081cc63f228a
    :realsig: (int,int) const
    :digest: 13c427c09a7861ee2318d5c0da23b8c4

Returns the glyph indexes and positions for all glyphs corresponding to the *length* characters starting at the position *from* in this :sip:ref:`~PyQt6.QtGui.QTextLayout`. This is an expensive function, and should not be called in a time sensitive context.

If *from* is less than zero, then the glyph run will begin at the first character in the layout. If *length* is less than zero, it will span the entire string from the start position.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextLayout.draw`, :sip:ref:`~PyQt6.QtGui.QPainter.drawGlyphRun`.
