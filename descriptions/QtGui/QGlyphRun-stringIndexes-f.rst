.. sip:method-description::
    :status: todo
    :pysig: 547b203239a35d1de005c5b84090af5b
    :realsig: () const
    :digest: c3726bd46b9cc07e55915a47fe694e55

Returns the string indexes corresponding to each glyph index, if the glyph run has been constructed from a string and string indexes have been requested from the layout. In this case, the length of the returned vector will correspond to the length of :sip:ref:`~PyQt6.QtGui.QGlyphRun.glyphIndexes`. In other cases, it will be empty.

Since a single glyph may correspond to multiple characters in the source string, there may be gaps in the list of string indexes. For instance, if the string "first" is processed by a font which contains a ligature for the character pair "fi", then the five character string will generate a glyph run consisting of only four glyphs. Then the glyph indexes may in this case be (1, 2, 3, 4) (four arbitrary glyph indexes) whereas the string indexes would be (0, 2, 3, 4). The glyphs are in the logical order of the string, thus it is implied that the first glyphs spans characters 0 and 1 in this case.

Inversely, a single character may also generate multiple glyphs, in which case there will be duplicate entries in the list of string indexes.

The string indexes correspond to the string, optionally available through :sip:ref:`~PyQt6.QtGui.QGlyphRun.sourceString`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QGlyphRun.setStringIndexes`, :sip:ref:`~PyQt6.QtGui.QGlyphRun.sourceString`, :sip:ref:`~PyQt6.QtGui.QTextLayout.glyphRuns`.
