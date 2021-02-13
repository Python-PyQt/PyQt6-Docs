.. sip:class-description::
    :status: todo
    :brief: Access to a single physical instance of a font
    :digest: 87c171a52db2319884bb3770d153dba7

The :sip:ref:`~PyQt6.QtGui.QRawFont` class provides access to a single physical instance of a font.

**Note:** :sip:ref:`~PyQt6.QtGui.QRawFont` is a low level class. For most purposes `QFont <https://doc.qt.io/qt-6/gui-changes-qt6.html#qfont>`_ is a more appropriate class.

Most commonly, when presenting text in a user interface, the exact fonts used to render the characters is to some extent unknown. This can be the case for several reasons: For instance, the actual, physical fonts present on the target system could be unexpected to the developers, or the text could contain user selected styles, sizes or writing systems that are not supported by font chosen in the code.

Therefore, Qt's `QFont <https://doc.qt.io/qt-6/gui-changes-qt6.html#qfont>`_ class really represents a query for fonts. When text is interpreted, Qt will do its best to match the text to the query, but depending on the support, different fonts can be used behind the scenes.

For most use cases, this is both expected and necessary, as it minimizes the possibility of text in the user interface being undisplayable. In some cases, however, more direct control over the process might be useful. It is for these use cases the :sip:ref:`~PyQt6.QtGui.QRawFont` class exists.

A :sip:ref:`~PyQt6.QtGui.QRawFont` object represents a single, physical instance of a given font in a given pixel size. I.e. in the typical case it represents a set of TrueType or OpenType font tables and uses a user specified pixel size to convert metrics into logical pixel units. It can be used in combination with the :sip:ref:`~PyQt6.QtGui.QGlyphRun` class to draw specific glyph indexes at specific positions, and also have accessors to some relevant data in the physical font.

:sip:ref:`~PyQt6.QtGui.QRawFont` only provides support for the main font technologies: GDI and DirectWrite on Windows platforms, FreeType on Linux platforms and CoreText on macOS. For other font back-ends, the APIs will be disabled.

:sip:ref:`~PyQt6.QtGui.QRawFont` can be constructed in a number of ways:

* It can be constructed by calling QTextLayout::glyphs() or QTextFragment::glyphs(). The returned QGlyphs objects will contain :sip:ref:`~PyQt6.QtGui.QRawFont` objects which represent the actual fonts used to render each portion of the text.

* It can be constructed by passing a `QFont <https://doc.qt.io/qt-6/gui-changes-qt6.html#qfont>`_ object to :sip:ref:`~PyQt6.QtGui.QRawFont.fromFont`. The function will return a :sip:ref:`~PyQt6.QtGui.QRawFont` object representing the font that will be selected as response to the `QFont <https://doc.qt.io/qt-6/gui-changes-qt6.html#qfont>`_ query and the selected writing system.

* It can be constructed by passing a file name or :sip:ref:`~PyQt6.QtCore.QByteArray` directly to the :sip:ref:`~PyQt6.QtGui.QRawFont` constructor, or by calling :sip:ref:`~PyQt6.QtGui.QRawFont.loadFromFile` or :sip:ref:`~PyQt6.QtGui.QRawFont.loadFromData`. In this case, the font will not be registered in `QFontDatabase <https://doc.qt.io/qt-6/gui-changes-qt6.html#qfontdatabase>`_, and it will not be available as part of regular font selection.

:sip:ref:`~PyQt6.QtGui.QRawFont` is considered local to the thread in which it is constructed (either using a constructor, or by calling :sip:ref:`~PyQt6.QtGui.QRawFont.loadFromData` or :sip:ref:`~PyQt6.QtGui.QRawFont.loadFromFile`). The :sip:ref:`~PyQt6.QtGui.QRawFont` cannot be moved to a different thread, but will have to be recreated in the thread in question.

**Note:** For the requirement of caching glyph indexes and font selections for static text to avoid reshaping and relayouting in the inner loop of an application, a better choice is the :sip:ref:`~PyQt6.QtGui.QStaticText` class, since it optimizes the memory cost of the cache and also provides the possibility of paint engine specific caches for an additional speed-up.
