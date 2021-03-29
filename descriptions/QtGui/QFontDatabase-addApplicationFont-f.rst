.. sip:method-description::
    :status: todo
    :pysig: 7079d0947acc4e2fbfa85152170eb388
    :realsig: (const QString&)
    :digest: 1d7bb6e2db3c091708259dc8157678b0

Loads the font from the file specified by *fileName* and makes it available to the application. An ID is returned that can be used to remove the font again with :sip:ref:`~PyQt6.QtGui.QFontDatabase.removeApplicationFont` or to retrieve the list of family names contained in the font.

The function returns -1 if the font could not be loaded.

Currently only TrueType fonts, TrueType font collections, and OpenType fonts are supported.

**Note:** Adding application fonts on Unix/X11 platforms without fontconfig is currently not supported.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFontDatabase.addApplicationFontFromData`, :sip:ref:`~PyQt6.QtGui.QFontDatabase.applicationFontFamilies`, :sip:ref:`~PyQt6.QtGui.QFontDatabase.removeApplicationFont`.
