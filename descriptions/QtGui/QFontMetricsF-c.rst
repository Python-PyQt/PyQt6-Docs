.. sip:class-description::
    :status: todo
    :brief: Font metrics information
    :digest: e99824be3a933026ecf34d1c6b58c551

The :sip:ref:`~PyQt6.QtGui.QFontMetricsF` class provides font metrics information.

:sip:ref:`~PyQt6.QtGui.QFontMetricsF` functions calculate the size of characters and strings for a given font. You can construct a :sip:ref:`~PyQt6.QtGui.QFontMetricsF` object with an existing `QFont <https://doc.qt.io/qt-6/gui-changes-qt6.html#qfont>`_ to obtain metrics for that font. If the font is changed later, the font metrics object is *not* updated.

Once created, the object provides functions to access the individual metrics of the font, its characters, and for strings rendered in the font.

There are several functions that operate on the font: :sip:ref:`~PyQt6.QtGui.QFontMetricsF.ascent`, :sip:ref:`~PyQt6.QtGui.QFontMetricsF.descent`, :sip:ref:`~PyQt6.QtGui.QFontMetricsF.height`, :sip:ref:`~PyQt6.QtGui.QFontMetricsF.leading` and :sip:ref:`~PyQt6.QtGui.QFontMetricsF.lineSpacing` return the basic size properties of the font. The :sip:ref:`~PyQt6.QtGui.QFontMetricsF.underlinePos`, :sip:ref:`~PyQt6.QtGui.QFontMetricsF.overlinePos`, :sip:ref:`~PyQt6.QtGui.QFontMetricsF.strikeOutPos` and :sip:ref:`~PyQt6.QtGui.QFontMetricsF.lineWidth` functions, return the properties of the line that underlines, overlines or strikes out the characters. These functions are all fast.

There are also some functions that operate on the set of glyphs in the font: :sip:ref:`~PyQt6.QtGui.QFontMetricsF.minLeftBearing`, :sip:ref:`~PyQt6.QtGui.QFontMetricsF.minRightBearing` and :sip:ref:`~PyQt6.QtGui.QFontMetricsF.maxWidth`. These are by necessity slow, and we recommend avoiding them if possible.

For each character, you can get its :sip:ref:`~PyQt6.QtGui.QFontMetricsF.horizontalAdvance`, :sip:ref:`~PyQt6.QtGui.QFontMetricsF.leftBearing`, and :sip:ref:`~PyQt6.QtGui.QFontMetricsF.rightBearing`, and find out whether it is in the font using :sip:ref:`~PyQt6.QtGui.QFontMetricsF.inFont`. You can also treat the character as a string, and use the string functions on it.

The string functions include :sip:ref:`~PyQt6.QtGui.QFontMetricsF.horizontalAdvance`, to return the width of a string in pixels (or points, for a printer), :sip:ref:`~PyQt6.QtGui.QFontMetricsF.boundingRect`, to return a rectangle large enough to contain the rendered string, and :sip:ref:`~PyQt6.QtGui.QFontMetricsF.size`, to return the size of that rectangle.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_text_qfontmetrics.py
    :lines: 72-75

.. seealso:: `QFont <https://doc.qt.io/qt-6/gui-changes-qt6.html#qfont>`_, :sip:ref:`~PyQt6.QtGui.QFontInfo`, `QFontDatabase <https://doc.qt.io/qt-6/gui-changes-qt6.html#qfontdatabase>`_.
