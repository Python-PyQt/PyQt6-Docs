.. sip:method-description::
    :status: todo
    :pysig: af76945fd0d9041f46237f50227c25fb
    :realsig: (const QString&)
    :digest: a7589ced5c0afadb8cf609f82e987fb7

Removes *familyName* from the list of application-defined emoji fonts, provided that it has previously been added with :sip:ref:`~PyQt6.QtGui.QFontDatabase.addApplicationEmojiFontFamily`.

Returns true if the family name was in the list and false if it was not.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFontDatabase.addApplicationEmojiFontFamily`, :sip:ref:`~PyQt6.QtGui.QFontDatabase.setApplicationEmojiFontFamilies`, :sip:ref:`~PyQt6.QtGui.QFontDatabase.applicationEmojiFontFamilies`, :sip:ref:`~PyQt6.QtGui.QFontDatabase.removeApplicationFallbackFontFamily`.
