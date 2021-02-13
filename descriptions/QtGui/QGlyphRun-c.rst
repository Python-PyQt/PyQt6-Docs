.. sip:class-description::
    :status: todo
    :brief: Direct access to the internal glyphs in a font
    :digest: 6e48aad3855bf5f4af5080beadf8da05

The :sip:ref:`~PyQt6.QtGui.QGlyphRun` class provides direct access to the internal glyphs in a font.

When Qt displays a string of text encoded in Unicode, it will first convert the Unicode points into a list of glyph indexes and a list of positions based on one or more fonts. The Unicode representation of the text and the `QFont <https://doc.qt.io/qt-6/gui-changes-qt6.html#qfont>`_ object will in this case serve as a convenient abstraction that hides the details of what actually takes place when displaying the text on-screen. For instance, by the time the text actually reaches the screen, it may be represented by a set of fonts in addition to the one specified by the user, e.g. in case the originally selected font did not support all the writing systems contained in the text.

Under certain circumstances, it can be useful as an application developer to have more low-level control over which glyphs in a specific font are drawn to the screen. This could for instance be the case in applications that use an external font engine and text shaper together with Qt. :sip:ref:`~PyQt6.QtGui.QGlyphRun` provides an interface to the raw data needed to get text on the screen. It contains a list of glyph indexes, a position for each glyph and a font.

It is the user's responsibility to ensure that the selected font actually contains the provided glyph indexes.

:sip:ref:`~PyQt6.QtGui.QTextLayout.glyphRuns` or :sip:ref:`~PyQt6.QtGui.QTextFragment.glyphRuns` can be used to convert unicode encoded text into a list of :sip:ref:`~PyQt6.QtGui.QGlyphRun` objects, and :sip:ref:`~PyQt6.QtGui.QPainter.drawGlyphRun` can be used to draw the glyphs.

**Note:** Please note that :sip:ref:`~PyQt6.QtGui.QRawFont` is considered local to the thread in which it is constructed. This in turn means that a new :sip:ref:`~PyQt6.QtGui.QRawFont` will have to be created and set on the :sip:ref:`~PyQt6.QtGui.QGlyphRun` if it is moved to a different thread. If the :sip:ref:`~PyQt6.QtGui.QGlyphRun` contains a reference to a :sip:ref:`~PyQt6.QtGui.QRawFont` from a different thread than the current, it will not be possible to draw the glyphs using a :sip:ref:`~PyQt6.QtGui.QPainter`, as the :sip:ref:`~PyQt6.QtGui.QRawFont` is considered invalid and inaccessible in this case.
