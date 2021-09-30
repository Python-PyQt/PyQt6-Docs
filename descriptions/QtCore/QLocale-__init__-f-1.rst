.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: ae759f263e4596ea4c77f25efd28fcc4

Constructs a :sip:ref:`~PyQt6.QtCore.QLocale` object with the specified *name*, which has the format "language[_script][_territory][.codeset][@modifier]" or "C", where:

* language is a lowercase, two-letter, ISO 639 language code (some three-letter codes are also recognized),

* script is a capitalized, four-letter, ISO 15924 script code,

* territory is an uppercase, two-letter, ISO 3166 territory code (some numeric codes are also recognized), and

* codeset and modifier are ignored.

The separator can be either underscore ``'_'`` (U+005F, "low line") or a dash ``'-'`` (U+002D, "hyphen-minus"). If :sip:ref:`~PyQt6.QtCore.QLocale` has no data for the specified combination of language, script, and territory, then it uses the most suitable match it can find instead. If the string violates the locale format, or no suitable data can be found for the specified keys, the "C" locale is used instead.

This constructor is much slower than :sip:ref:`~PyQt6.QtCore.QLocale`\ (Language, Script, Territory) or :sip:ref:`~PyQt6.QtCore.QLocale`\ (Language, Territory).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.bcp47Name`, :ref:`qlocale-matching-combinations-of-language-script-and-territory`.
