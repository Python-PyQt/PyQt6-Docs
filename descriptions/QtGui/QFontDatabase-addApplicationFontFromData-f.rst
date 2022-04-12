.. sip:method-description::
    :status: todo
    :pysig: dbfb8b22abe8f64a5673fea458d78c0f
    :realsig: (const QByteArray&)
    :digest: 786b4efcfeeb3df56d344a998fbfe87b

Loads the font from binary data specified by *fontData* and makes it available to the application. An ID is returned that can be used to remove the font again with :sip:ref:`~PyQt6.QtGui.QFontDatabase.removeApplicationFont` or to retrieve the list of family names contained in the font.

The function returns -1 if the font could not be loaded.

Currently only TrueType fonts, TrueType font collections, and OpenType fonts are supported.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFontDatabase.addApplicationFont`, :sip:ref:`~PyQt6.QtGui.QFontDatabase.applicationFontFamilies`, :sip:ref:`~PyQt6.QtGui.QFontDatabase.removeApplicationFont`.
