.. sip:method-description::
    :status: todo
    :pysig: f45d770c6ff53d422712081cc63f228a
    :realsig: (int,int) const
    :digest: e80cea12cdb30c90f0caf059d6a50159

Returns the glyph indexes and positions for all glyphs in this :sip:ref:`~PyQt6.QtGui.QTextLine` for characters in the range defined by *from* and *length*. The *from* index is relative to the beginning of the text in the containing :sip:ref:`~PyQt6.QtGui.QTextLayout`, and the range must be within the range of :sip:ref:`~PyQt6.QtGui.QTextLine` as given by functions :sip:ref:`~PyQt6.QtGui.QTextLine.textStart` and :sip:ref:`~PyQt6.QtGui.QTextLine.textLength`.

If *from* is negative, it will default to :sip:ref:`~PyQt6.QtGui.QTextLine.textStart`, and if *length* is negative it will default to the return value of :sip:ref:`~PyQt6.QtGui.QTextLine.textLength`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextLayout.glyphRuns`.
