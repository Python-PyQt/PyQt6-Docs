.. sip:method-description::
    :status: todo
    :pysig: 1c39dde99eb284c5cb162c0e5688e3dd
    :realsig: (const QString&) const
    :digest: 4bf40ab4a1546ea619974bb887b5451e

Converts the string of unicode points given by *text* to glyph indexes using the CMAP table in the underlying font, and returns a list containing the result.

Note that, in cases where there are other tables in the font that affect the shaping of the text, the returned glyph indexes will not correctly represent the rendering of the text. To get the correctly shaped text, you can use :sip:ref:`~PyQt6.QtGui.QTextLayout` to lay out and shape the text, then call QTextLayout::glyphs() to get the set of glyph index list and :sip:ref:`~PyQt6.QtGui.QRawFont` pairs.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QRawFont.advancesForGlyphIndexes`, glyphIndexesForChars(), :sip:ref:`~PyQt6.QtGui.QGlyphRun`, :sip:ref:`~PyQt6.QtGui.QTextLayout.glyphRuns`, :sip:ref:`~PyQt6.QtGui.QTextFragment.glyphRuns`.
