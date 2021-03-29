.. sip:method-description::
    :status: todo
    :pysig: 13589a9b9c4c6c30ca426ce536937662
    :realsig: (const QRectF&)
    :digest: 382c542322acde44b08900563163c8c2

Sets the bounding rect of the glyphs in this :sip:ref:`~PyQt6.QtGui.QGlyphRun` to be *boundingRect*. This rectangle will be returned by :sip:ref:`~PyQt6.QtGui.QGlyphRun.boundingRect` unless it is empty, in which case the bounding rectangle of the glyphs in the glyph run will be returned instead.

**Note:** Unless you are implementing text shaping, you should not have to use this function. It is used specifically when the :sip:ref:`~PyQt6.QtGui.QGlyphRun` should represent an area which is smaller than the area of the glyphs it contains. This could happen e.g. if the glyph run is retrieved by calling :sip:ref:`~PyQt6.QtGui.QTextLayout.glyphRuns` and the specified range only includes part of a ligature (where two or more characters are combined to a single glyph.) When this is the case, the bounding rect should only include the appropriate part of the ligature glyph, based on a calculation of the average width of the characters in the ligature.

In order to support such a case (an example is selections which should be drawn with a different color than the main text color), it is necessary to clip the painting mechanism to the rectangle returned from :sip:ref:`~PyQt6.QtGui.QGlyphRun.boundingRect` to avoid drawing the entire ligature glyph.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QGlyphRun.boundingRect`.
