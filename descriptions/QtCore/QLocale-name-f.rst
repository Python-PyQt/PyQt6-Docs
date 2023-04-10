.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 50afffbfdb202fc1465917d31f0f5156

The short name of this locale.

Returns the language and territory of this locale as a string of the form "language_territory", where language is a lowercase, two-letter ISO 639 language code, and territory is an uppercase, two- or three-letter ISO 3166 territory code. If the locale has no specified territory, only the language name is returned.

Even if the :sip:ref:`~PyQt6.QtCore.QLocale` object was constructed with an explicit script, name() will not contain it for compatibility reasons. Use :sip:ref:`~PyQt6.QtCore.QLocale.bcp47Name` instead if you need a full locale name, or construct the string you want to identify a locale by from those returned by passing its :sip:ref:`~PyQt6.QtCore.QLocale.language` to :sip:ref:`~PyQt6.QtCore.QLocale.languageToCode` and similar for the script and territory.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale`, :sip:ref:`~PyQt6.QtCore.QLocale.language`, :sip:ref:`~PyQt6.QtCore.QLocale.script`, :sip:ref:`~PyQt6.QtCore.QLocale.territory`, :sip:ref:`~PyQt6.QtCore.QLocale.bcp47Name`, :sip:ref:`~PyQt6.QtCore.QLocale.uiLanguages`.
