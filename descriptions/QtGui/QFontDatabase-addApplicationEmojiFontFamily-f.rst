.. sip:method-description::
    :status: todo
    :pysig: c5283bf81cad04335531dd6931c2734d
    :realsig: (const QString&)
    :digest: ade5991b912f81fcddd666232635aa8d

Adds *familyName* as an application-defined emoji font.

For displaying multi-color emojis or emoji sequences, Qt will by default prefer the system default emoji font. Sometimes the application may want to override the default, either to achieve a specific visual style or to show emojis that are not supported by the system.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFontDatabase.removeApplicationEmojiFontFamily`, :sip:ref:`~PyQt6.QtGui.QFontDatabase.setApplicationEmojiFontFamilies`, :sip:ref:`~PyQt6.QtGui.QFontDatabase.applicationEmojiFontFamilies`, :sip:ref:`~PyQt6.QtGui.QFontDatabase.addApplicationFallbackFontFamily`.
