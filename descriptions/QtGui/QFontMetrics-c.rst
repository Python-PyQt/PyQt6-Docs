.. sip:class-description::
    :status: todo
    :brief: Font metrics information
    :digest: 9546ed91edc2624d78d3135613460c06

The :sip:ref:`~PyQt6.QtGui.QFontMetrics` class provides font metrics information.

:sip:ref:`~PyQt6.QtGui.QFontMetrics` functions calculate the size of characters and strings for a given font. There are three ways you can create a :sip:ref:`~PyQt6.QtGui.QFontMetrics` object:

#. Calling the :sip:ref:`~PyQt6.QtGui.QFontMetrics` constructor with a :sip:ref:`~PyQt6.QtGui.QFont` creates a font metrics object for a screen-compatible font, i.e. the font cannot be a printer font. If the font is changed later, the font metrics object is *not* updated.

   (Note: If you use a printer font the values returned may be inaccurate. Printer fonts are not always accessible so the nearest screen font is used if a printer font is supplied.)

#. :sip:ref:`~PyQt6.QtWidgets.QWidget.fontMetrics` returns the font metrics for a widget's font. This is equivalent to :sip:ref:`~PyQt6.QtGui.QFontMetrics`\ (widget->font()). If the widget's font is changed later, the font metrics object is *not* updated.

#. :sip:ref:`~PyQt6.QtGui.QPainter.fontMetrics` returns the font metrics for a painter's current font. If the painter's font is changed later, the font metrics object is *not* updated.

Once created, the object provides functions to access the individual metrics of the font, its characters, and for strings rendered in the font.

There are several functions that operate on the font: :sip:ref:`~PyQt6.QtGui.QFontMetrics.ascent`, :sip:ref:`~PyQt6.QtGui.QFontMetrics.descent`, :sip:ref:`~PyQt6.QtGui.QFontMetrics.height`, :sip:ref:`~PyQt6.QtGui.QFontMetrics.leading` and :sip:ref:`~PyQt6.QtGui.QFontMetrics.lineSpacing` return the basic size properties of the font. The :sip:ref:`~PyQt6.QtGui.QFontMetrics.underlinePos`, :sip:ref:`~PyQt6.QtGui.QFontMetrics.overlinePos`, :sip:ref:`~PyQt6.QtGui.QFontMetrics.strikeOutPos` and :sip:ref:`~PyQt6.QtGui.QFontMetrics.lineWidth` functions, return the properties of the line that underlines, overlines or strikes out the characters. These functions are all fast.

There are also some functions that operate on the set of glyphs in the font: :sip:ref:`~PyQt6.QtGui.QFontMetrics.minLeftBearing`, :sip:ref:`~PyQt6.QtGui.QFontMetrics.minRightBearing` and :sip:ref:`~PyQt6.QtGui.QFontMetrics.maxWidth`. These are by necessity slow, and we recommend avoiding them if possible.

For each character, you can get its :sip:ref:`~PyQt6.QtGui.QFontMetrics.horizontalAdvance`, :sip:ref:`~PyQt6.QtGui.QFontMetrics.leftBearing`, and :sip:ref:`~PyQt6.QtGui.QFontMetrics.rightBearing`, and find out whether it is in the font using :sip:ref:`~PyQt6.QtGui.QFontMetrics.inFont`. You can also treat the character as a string, and use the string functions on it.

The string functions include :sip:ref:`~PyQt6.QtGui.QFontMetrics.horizontalAdvance`, to return the advance width of a string in pixels (or points, for a printer), :sip:ref:`~PyQt6.QtGui.QFontMetrics.boundingRect`, to return a rectangle large enough to contain the rendered string, and :sip:ref:`~PyQt6.QtGui.QFontMetrics.size`, to return the size of that rectangle.

**Note:** The advance width can be different from the width of the actual rendered text. It refers to the distance from the origin of the string to where you would append additional characters. As text may have overhang (in the case of an italic font for instance) or padding between characters, the advance width can be either smaller or larger than the actual rendering of the text. This is called the right bearing of the text.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_text_qfontmetrics.py
    :lines: 59-62

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFont`, :sip:ref:`~PyQt6.QtGui.QFontInfo`, :sip:ref:`~PyQt6.QtGui.QFontDatabase`.
