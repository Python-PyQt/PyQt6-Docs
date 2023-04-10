.. sip:class-description::
    :status: todo
    :brief: Specifies a query for a font used for drawing text
    :digest: 378e6aad95f0f1c08857ca425738ec66

The :sip:ref:`~PyQt6.QtGui.QFont` class specifies a query for a font used for drawing text.

:sip:ref:`~PyQt6.QtGui.QFont` can be regarded as a query for one or more fonts on the system.

When you create a :sip:ref:`~PyQt6.QtGui.QFont` object you specify various attributes that you want the font to have. Qt will use the font with the specified attributes, or if no matching font exists, Qt will use the closest matching installed font. The attributes of the font that is actually used are retrievable from a :sip:ref:`~PyQt6.QtGui.QFontInfo` object. If the window system provides an exact match :sip:ref:`~PyQt6.QtGui.QFont.exactMatch` returns ``true``. Use :sip:ref:`~PyQt6.QtGui.QFontMetricsF` to get measurements, e.g. the pixel length of a string using QFontMetrics::width().

Attributes which are not specifically set will not affect the font selection algorithm, and default values will be preferred instead.

To load a specific physical font, typically represented by a single file, use :sip:ref:`~PyQt6.QtGui.QRawFont` instead.

Note that a :sip:ref:`~PyQt6.QtGui.QGuiApplication` instance must exist before a :sip:ref:`~PyQt6.QtGui.QFont` can be used. You can set the application's default font with QGuiApplication::setFont().

If a chosen font does not include all the characters that need to be displayed, :sip:ref:`~PyQt6.QtGui.QFont` will try to find the characters in the nearest equivalent fonts. When a :sip:ref:`~PyQt6.QtGui.QPainter` draws a character from a font the :sip:ref:`~PyQt6.QtGui.QFont` will report whether or not it has the character; if it does not, :sip:ref:`~PyQt6.QtGui.QPainter` will draw an unfilled square.

Create QFonts like this:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_text_qfont.py
    :lines: 60-61

The attributes set in the constructor can also be set later, e.g. :sip:ref:`~PyQt6.QtGui.QFont.setFamily`, :sip:ref:`~PyQt6.QtGui.QFont.setPointSize`, :sip:ref:`~PyQt6.QtGui.QFont.setPointSizeF`, :sip:ref:`~PyQt6.QtGui.QFont.setWeight` and :sip:ref:`~PyQt6.QtGui.QFont.setItalic`. The remaining attributes must be set after construction, e.g. :sip:ref:`~PyQt6.QtGui.QFont.setBold`, :sip:ref:`~PyQt6.QtGui.QFont.setUnderline`, :sip:ref:`~PyQt6.QtGui.QFont.setOverline`, :sip:ref:`~PyQt6.QtGui.QFont.setStrikeOut` and :sip:ref:`~PyQt6.QtGui.QFont.setFixedPitch`. :sip:ref:`~PyQt6.QtGui.QFontInfo` objects should be created *after* the font's attributes have been set. A :sip:ref:`~PyQt6.QtGui.QFontInfo` object will not change, even if you change the font's attributes. The corresponding "get" functions, e.g. :sip:ref:`~PyQt6.QtGui.QFont.family`, :sip:ref:`~PyQt6.QtGui.QFont.pointSize`, etc., return the values that were set, even though the values used may differ. The actual values are available from a :sip:ref:`~PyQt6.QtGui.QFontInfo` object.

If the requested font family is unavailable you can influence the font matching algorithm by choosing a particular :sip:ref:`~PyQt6.QtGui.QFont.StyleHint` and :sip:ref:`~PyQt6.QtGui.QFont.StyleStrategy` with :sip:ref:`~PyQt6.QtGui.QFont.setStyleHint`. The default family (corresponding to the current style hint) is returned by :sip:ref:`~PyQt6.QtGui.QFont.defaultFamily`.

You can provide substitutions for font family names using :sip:ref:`~PyQt6.QtGui.QFont.insertSubstitution` and :sip:ref:`~PyQt6.QtGui.QFont.insertSubstitutions`. Substitutions can be removed with :sip:ref:`~PyQt6.QtGui.QFont.removeSubstitutions`. Use :sip:ref:`~PyQt6.QtGui.QFont.substitute` to retrieve a family's first substitute, or the family name itself if it has no substitutes. Use :sip:ref:`~PyQt6.QtGui.QFont.substitutes` to retrieve a list of a family's substitutes (which may be empty). After substituting a font, you must trigger the updating of the font by destroying and re-creating all :sip:ref:`~PyQt6.QtGui.QFont` objects.

Every :sip:ref:`~PyQt6.QtGui.QFont` has a :sip:ref:`~PyQt6.QtGui.QFont.key` which you can use, for example, as the key in a cache or dictionary. If you want to store a user's font preferences you could use :sip:ref:`~PyQt6.QtCore.QSettings`, writing the font information with :sip:ref:`~PyQt6.QtGui.QFont.toString` and reading it back with :sip:ref:`~PyQt6.QtGui.QFont.fromString`. The operator<<() and operator>>() functions are also available, but they work on a data stream.

It is possible to set the height of characters shown on the screen to a specified number of pixels with :sip:ref:`~PyQt6.QtGui.QFont.setPixelSize`; however using :sip:ref:`~PyQt6.QtGui.QFont.setPointSize` has a similar effect and provides device independence.

Loading fonts can be expensive, especially on X11. :sip:ref:`~PyQt6.QtGui.QFont` contains extensive optimizations to make the copying of :sip:ref:`~PyQt6.QtGui.QFont` objects fast, and to cache the results of the slow window system functions it depends upon.

.. _qfont-fontmatching:

The font matching algorithm works as follows:

#. The specified font families (set by :sip:ref:`~PyQt6.QtGui.QFont.setFamilies`) are searched for.

#. If not found, then if set the specified font family exists and can be used to represent the writing system in use, it will be selected.

#. If not, a replacement font that supports the writing system is selected. The font matching algorithm will try to find the best match for all the properties set in the :sip:ref:`~PyQt6.QtGui.QFont`. How this is done varies from platform to platform.

#. If no font exists on the system that can support the text, then special "missing character" boxes will be shown in its place.

**Note:** If the selected font, though supporting the writing system in general, is missing glyphs for one or more specific characters, then Qt will try to find a fallback font for this or these particular characters. This feature can be disabled using :sip:ref:`~PyQt6.QtGui.QFont.StyleStrategy.NoFontMerging` style strategy.

In Windows a request for the "Courier" font is automatically changed to "Courier New", an improved version of Courier that allows for smooth scaling. The older "Courier" bitmap font can be selected by setting the :sip:ref:`~PyQt6.QtGui.QFont.StyleStrategy.PreferBitmap` style strategy (see :sip:ref:`~PyQt6.QtGui.QFont.setStyleStrategy`).

Once a font is found, the remaining attributes are matched in order of priority:

#. :sip:ref:`~PyQt6.QtGui.QFont.fixedPitch`

#. :sip:ref:`~PyQt6.QtGui.QFont.pointSize` (see below)

#. :sip:ref:`~PyQt6.QtGui.QFont.weight`

#. :sip:ref:`~PyQt6.QtGui.QFont.style`

If you have a font which matches on family, even if none of the other attributes match, this font will be chosen in preference to a font which doesn't match on family but which does match on the other attributes. This is because font family is the dominant search criteria.

The point size is defined to match if it is within 20% of the requested point size. When several fonts match and are only distinguished by point size, the font with the closest point size to the one requested will be chosen.

The actual family, font size, weight and other font attributes used for drawing text will depend on what's available for the chosen family under the window system. A :sip:ref:`~PyQt6.QtGui.QFontInfo` object can be used to determine the actual values used for drawing the text.

Examples:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_text_qfont.py
    :lines: 66-66

If you had both an Adobe and a Cronyx Helvetica, you might get either.

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_text_qfont.py
    :lines: 75-75

You can specify the foundry you want in the family name. The font f in the above example will be set to "Helvetica [Cronyx]".

To determine the attributes of the font actually used in the window system, use a :sip:ref:`~PyQt6.QtGui.QFontInfo` object, e.g.

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_text_qfont.py
    :lines: 80-81

To find out font metrics use a :sip:ref:`~PyQt6.QtGui.QFontMetrics` object, e.g.

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_text_qfont.py
    :lines: 86-88

For more general information on fonts, see the `comp.fonts FAQ <https://doc.qt.io/qt-6/http://nwalsh.com/comp.fonts/FAQ/>`_. Information on encodings can be found from the `UTR17 <https://doc.qt.io/qt-6/https://www.unicode.org/reports/tr17/>`_ page.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFontMetrics`, :sip:ref:`~PyQt6.QtGui.QFontInfo`, :sip:ref:`~PyQt6.QtGui.QFontDatabase`, `Character Map Example <https://doc.qt.io/qt-6/qtwidgets-widgets-charactermap-example.html>`_.
