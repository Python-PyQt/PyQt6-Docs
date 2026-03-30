.. sip:method-description::
    :status: todo
    :pysig: 259c17175844d15fad8b006ad4b31242
    :realsig: (QChar::Script, const QString&)
    :digest: da037fce745dee71c070b258f8c489f8

Removes *familyName* from the list of application-defined fallback fonts for *script*, provided that it has previously been added with :sip:ref:`~PyQt6.QtGui.QFontDatabase.addApplicationFallbackFontFamily`.

Returns true if the family name was in the list and false if it was not.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFontDatabase.addApplicationFallbackFontFamily`, :sip:ref:`~PyQt6.QtGui.QFontDatabase.setApplicationFallbackFontFamilies`, :sip:ref:`~PyQt6.QtGui.QFontDatabase.applicationFallbackFontFamilies`.
