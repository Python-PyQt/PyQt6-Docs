.. sip:method-description::
    :status: todo
    :pysig: 7079d0947acc4e2fbfa85152170eb388
    :realsig: (const QString&)
    :digest: d2f0fc43755a317c87ef653656bae28b

Loads the font from the file specified by *fileName* and makes it available to the application. An ID is returned that can be used to remove the font again with :sip:ref:`~PyQt6.QtGui.QFontDatabase.removeApplicationFont` or to retrieve the list of family names contained in the font.

The function returns -1 if the font could not be loaded.

Currently only TrueType fonts, TrueType font collections, and OpenType fonts are supported.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFontDatabase.addApplicationFontFromData`, :sip:ref:`~PyQt6.QtGui.QFontDatabase.applicationFontFamilies`, :sip:ref:`~PyQt6.QtGui.QFontDatabase.removeApplicationFont`.
