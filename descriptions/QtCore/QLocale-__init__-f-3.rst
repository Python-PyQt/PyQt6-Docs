.. sip:method-description::
    :status: todo
    :pysig: 2bef3274671b908eb48341df9ca6f618
    :realsig: (QLocale::Language,QLocale::Country)
    :digest: e0ec0b877ab6117bf5ed647793d5f632

Constructs a :sip:ref:`~PyQt6.QtCore.QLocale` object with the specified *language* and *country*.

* If the language/country pair is found in the database, it is used.

* If the language is found but the country is not, or if the country is ``AnyCountry``, the language is used with the most appropriate available country (for example, Germany for German),

* If neither the language nor the country are found, :sip:ref:`~PyQt6.QtCore.QLocale` defaults to the default locale (see :sip:ref:`~PyQt6.QtCore.QLocale.setDefault`).

The language and country that are actually used can be queried using :sip:ref:`~PyQt6.QtCore.QLocale.language` and :sip:ref:`~PyQt6.QtCore.QLocale.country`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.setDefault`, :sip:ref:`~PyQt6.QtCore.QLocale.language`, :sip:ref:`~PyQt6.QtCore.QLocale.country`.
