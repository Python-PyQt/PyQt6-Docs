.. sip:class-description::
    :status: todo
    :brief: Formatting information for characters in a QTextDocument
    :digest: 0535419bcd398582e59427027a732d1a

The :sip:ref:`~PyQt6.QtGui.QTextCharFormat` class provides formatting information for characters in a :sip:ref:`~PyQt6.QtGui.QTextDocument`.

The character format of text in a document specifies the visual properties of the text, as well as information about its role in a hypertext document.

The font used can be set by supplying a font to the :sip:ref:`~PyQt6.QtGui.QTextCharFormat.setFont` function, and each aspect of its appearance can be adjusted to give the desired effect.  and :sip:ref:`~PyQt6.QtGui.QTextCharFormat.setFontPointSize` define the font's family (e.g. Times) and printed size; :sip:ref:`~PyQt6.QtGui.QTextCharFormat.setFontWeight` and :sip:ref:`~PyQt6.QtGui.QTextCharFormat.setFontItalic` provide control over the style of the font. :sip:ref:`~PyQt6.QtGui.QTextCharFormat.setFontUnderline`, :sip:ref:`~PyQt6.QtGui.QTextCharFormat.setFontOverline`, :sip:ref:`~PyQt6.QtGui.QTextCharFormat.setFontStrikeOut`, and :sip:ref:`~PyQt6.QtGui.QTextCharFormat.setFontFixedPitch` provide additional effects for text.

The color is set with setForeground(). If the text is intended to be used as an anchor (for hyperlinks), this can be enabled with :sip:ref:`~PyQt6.QtGui.QTextCharFormat.setAnchor`. The :sip:ref:`~PyQt6.QtGui.QTextCharFormat.setAnchorHref` and :sip:ref:`~PyQt6.QtGui.QTextCharFormat.setAnchorNames` functions are used to specify the information about the hyperlink's destination and the anchor's name.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextFormat`, :sip:ref:`~PyQt6.QtGui.QTextBlockFormat`, :sip:ref:`~PyQt6.QtGui.QTextTableFormat`, :sip:ref:`~PyQt6.QtGui.QTextListFormat`.
