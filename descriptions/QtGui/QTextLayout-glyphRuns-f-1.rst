.. sip:method-description::
    :status: todo
    :pysig: e85b5ffc3dab2cf059a7343a36b90f93
    :realsig: (int,int,QTextLayout::GlyphRunRetrievalFlags) const
    :digest: 10197e3eb883819d3fdcc462b4072a81

This is an overloaded function.

Returns the glyph indexes and positions for all glyphs corresponding to the *length* characters starting at the position *from* in this :sip:ref:`~PyQt6.QtGui.QTextLayout`. This is an expensive function, and should not be called in a time sensitive context.

If *from* is less than zero, then the glyph run will begin at the first character in the layout. If *length* is less than zero, it will span the entire string from the start position.

The *retrievalFlags* specifies which properties of the :sip:ref:`~PyQt6.QtGui.QGlyphRun` will be retrieved from the layout. To minimize allocations and memory consumption, this should be set to include only the properties that you need to access later.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextLayout.draw`, :sip:ref:`~PyQt6.QtGui.QPainter.drawGlyphRun`.
