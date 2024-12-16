.. sip:method-description::
    :status: todo
    :pysig: 8a7171a268df4bb72471e15f4dba6e66
    :realsig: (int, int, QTextLayout::GlyphRunRetrievalFlags) const
    :digest: cd664cb6b0af29be59284d50c5c883dd

Returns the glyph indexes and positions for all glyphs in this :sip:ref:`~PyQt6.QtGui.QTextLine` for characters in the range defined by *from* and *length*. The *from* index is relative to the beginning of the text in the containing :sip:ref:`~PyQt6.QtGui.QTextLayout`, and the range must be within the range of :sip:ref:`~PyQt6.QtGui.QTextLine` as given by functions :sip:ref:`~PyQt6.QtGui.QTextLine.textStart` and :sip:ref:`~PyQt6.QtGui.QTextLine.textLength`.

The *retrievalFlags* specifies which properties of the :sip:ref:`~PyQt6.QtGui.QGlyphRun` will be retrieved from the layout. To minimize allocations and memory consumption, this should be set to include only the properties that you need to access later.

If *from* is negative, it will default to :sip:ref:`~PyQt6.QtGui.QTextLine.textStart`, and if *length* is negative it will default to the return value of :sip:ref:`~PyQt6.QtGui.QTextLine.textLength`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextLayout.glyphRuns`.
