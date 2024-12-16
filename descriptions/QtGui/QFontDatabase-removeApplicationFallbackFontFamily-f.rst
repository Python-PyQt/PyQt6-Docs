.. sip:method-description::
    :status: todo
    :pysig: 11e57eae5118a2fa22dbff39abcd01b3
    :realsig: (QChar::Script, const QString&)
    :digest: da037fce745dee71c070b258f8c489f8

Removes *familyName* from the list of application-defined fallback fonts for *script*, provided that it has previously been added with :sip:ref:`~PyQt6.QtGui.QFontDatabase.addApplicationFallbackFontFamily`.

Returns true if the family name was in the list and false if it was not.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFontDatabase.addApplicationFallbackFontFamily`, :sip:ref:`~PyQt6.QtGui.QFontDatabase.setApplicationFallbackFontFamilies`, :sip:ref:`~PyQt6.QtGui.QFontDatabase.applicationFallbackFontFamilies`.
