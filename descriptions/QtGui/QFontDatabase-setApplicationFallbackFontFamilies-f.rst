.. sip:method-description::
    :status: todo
    :pysig: 45e940ac4e7d15cd42c0b759463bc1fb
    :realsig: (QChar::Script, const QStringList&)
    :digest: 069dc6c6d996a466903fcf180deb033b

Sets the list of application-defined fallback fonts for *script* to *familyNames*.

When Qt encounters a character in *script* which is not supported by the current font, it will check the families in *familyNames*, in order from first to last, until it finds a match. See :sip:ref:`~PyQt6.QtGui.QFontDatabase.addApplicationFallbackFontFamily` for more details.

This function overwrites the current list of application-defined fallback fonts for *script*.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFontDatabase.addApplicationFallbackFontFamily`, :sip:ref:`~PyQt6.QtGui.QFontDatabase.removeApplicationFallbackFontFamily`, :sip:ref:`~PyQt6.QtGui.QFontDatabase.applicationFallbackFontFamilies`.
