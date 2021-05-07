.. sip:enum-member-description::
    :status: todo
    :value: 0x10
    :digest: 8b1cf031662c30c04495d8b37f13f9f9

Indicates that the glyph run splits a ligature glyph. This means that a ligature glyph is included in the run, but the characters represented by it corresponds only to part of that ligature. The glyph run's :sip:ref:`~PyQt6.QtGui.QGlyphRun.boundingRect` function can in this case be used to retrieve the area covered by glyphs that correspond to the characters represented by the glyph run. When visualizing the glyphs, care needs to be taken to clip to this bounding rect to ensure that only the corresponding part of the ligature is painted. In particular, this can be the case when retrieving a glyph run from a :sip:ref:`~PyQt6.QtGui.QTextLayout` for a specific character range, e.g. when retrieving the selected area of a :sip:ref:`~PyQt6.QtGui.QTextLayout`.
