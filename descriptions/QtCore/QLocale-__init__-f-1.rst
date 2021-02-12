.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: c6a141d2b3c066e80df9aae1a70958ab

Constructs a :sip:ref:`~PyQt6.QtCore.QLocale` object with the specified *name*, which has the format "language[_script][_country][.codeset][@modifier]" or "C", where:

* language is a lowercase, two-letter, ISO 639 language code (also some three-letter codes),

* script is a titlecase, four-letter, ISO 15924 script code,

* country is an uppercase, two-letter, ISO 3166 country code (also "419" as defined by United Nations),

* and codeset and modifier are ignored.

The separator can be either underscore ``'_'`` (U+005F, "low line") or a dash ``'-'`` (U+002D, "hyphen-minus").

If the string violates the locale format, or language is not a valid ISO 639 code, the "C" locale is used instead. If country is not present, or is not a valid ISO 3166 code, the most appropriate country is chosen for the specified language.

The language, script and country codes are converted to their respective ``Language``, ``Script`` and ``Country`` enums. After this conversion is performed, the constructor behaves exactly like :sip:ref:`~PyQt6.QtCore.QLocale`\ (Country, Script, Language).

This constructor is much slower than :sip:ref:`~PyQt6.QtCore.QLocale`\ (Country, Script, Language).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.bcp47Name`.
