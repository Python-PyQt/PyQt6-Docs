.. sip:method-description::
    :status: todo
    :pysig: decde6f0317b457453b50b8e51f63e2d
    :realsig: (QStringView,QLocale::LanguageCodeTypes)
    :digest: b3f3f29d7124b65c8acba338f0a21e46

Returns the :sip:ref:`~PyQt6.QtCore.QLocale.Language` enum corresponding to the two- or three-letter *languageCode*, as defined in the ISO 639 standards.

If specified, *codeTypes* selects which set of codes to consider for conversion. By default all codes known to Qt are considered. The codes are matched in the following order: ``ISO639Part1``, ``ISO639Part2B``, ``ISO639Part2T``, ``ISO639Part3``, ``LegacyLanguageCode``.

If the code is invalid or not known ``QLocale::AnyLanguage`` is returned.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.languageToCode`, :sip:ref:`~PyQt6.QtCore.QLocale.codeToTerritory`, :sip:ref:`~PyQt6.QtCore.QLocale.codeToScript`.
