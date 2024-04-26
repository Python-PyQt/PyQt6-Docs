.. sip:method-description::
    :status: todo
    :pysig: fc41f1bc529af0d6626eb8dec9fd7479
    :realsig: (QLocale::TagSeparator) const
    :digest: f39a8b371211b6dead42718039ae9a83

The short name of this locale.

Returns the language and territory of this locale as a string of the form "language_territory", where language is a lowercase, two-letter ISO 639 language code, and territory is an uppercase, two- or three-letter ISO 3166 territory code. If the locale has no specified territory, only the language name is returned. Since Qt 6.7 an optional *separator* parameter can be supplied to override the default underscore character separating the two tags.

Even if the :sip:ref:`~PyQt6.QtCore.QLocale` object was constructed with an explicit script, name() will not contain it for compatibility reasons. Use :sip:ref:`~PyQt6.QtCore.QLocale.bcp47Name` instead if you need a full locale name, or construct the string you want to identify a locale by from those returned by passing its :sip:ref:`~PyQt6.QtCore.QLocale.language` to :sip:ref:`~PyQt6.QtCore.QLocale.languageToCode` and similar for the script and territory.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale`, :sip:ref:`~PyQt6.QtCore.QLocale.language`, :sip:ref:`~PyQt6.QtCore.QLocale.script`, :sip:ref:`~PyQt6.QtCore.QLocale.territory`, :sip:ref:`~PyQt6.QtCore.QLocale.bcp47Name`, :sip:ref:`~PyQt6.QtCore.QLocale.uiLanguages`.
