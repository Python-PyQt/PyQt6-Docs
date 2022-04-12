.. sip:method-description::
    :status: todo
    :pysig: 995c0fb654fd363f366ab119927731bf
    :realsig: (QLocale::Language,QLocale::LanguageCodeTypes)
    :digest: 9d2773e7a6a67018a202f80495586fb9

Returns the two- or three-letter language code for *language*, as defined in the ISO 639 standards.

If specified, *codeTypes* selects which set of codes to consider. The first code from the set that is defined for *language* is returned. Otherwise, all ISO-639 codes are considered. The codes are considered in the following order: ``ISO639Part1``, ``ISO639Part2B``, ``ISO639Part2T``, ``ISO639Part3``. ``LegacyLanguageCode`` is ignored by this function.

**Note:** For ``QLocale::C`` the function returns ``"C"``. For ``QLocale::AnyLanguage`` an empty string is returned. If the language has no code in any selected code set, an empty string is returned.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.codeToLanguage`, :sip:ref:`~PyQt6.QtCore.QLocale.language`, :sip:ref:`~PyQt6.QtCore.QLocale.name`, :sip:ref:`~PyQt6.QtCore.QLocale.bcp47Name`, :sip:ref:`~PyQt6.QtCore.QLocale.territoryToCode`, :sip:ref:`~PyQt6.QtCore.QLocale.scriptToCode`.
