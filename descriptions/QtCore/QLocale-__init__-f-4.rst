.. sip:method-description::
    :status: todo
    :pysig: 34db16e1be9aaf1cbe16ae24da81d1ea
    :realsig: (QLocale::Language,QLocale::Script,QLocale::Country)
    :digest: e4a7bd32bef0c06142c52c75dd2a7167

Constructs a :sip:ref:`~PyQt6.QtCore.QLocale` object with the specified *language*, *script* and *country*.

* If the language/script/country is found in the database, it is used.

* If both *script* is :sip:ref:`~PyQt6.QtCore.QLocale.Script.AnyScript` and *country* is :sip:ref:`~PyQt6.QtCore.QLocale.Country.AnyCountry`, the language is used with the most appropriate available script and country (for example, Germany for German),

* If either *script* is :sip:ref:`~PyQt6.QtCore.QLocale.Script.AnyScript` or *country* is :sip:ref:`~PyQt6.QtCore.QLocale.Country.AnyCountry`, the language is used with the first locale that matches the given *script* and *country*.

* If neither the language nor the country are found, :sip:ref:`~PyQt6.QtCore.QLocale` defaults to the default locale (see :sip:ref:`~PyQt6.QtCore.QLocale.setDefault`).

The language, script and country that are actually used can be queried using :sip:ref:`~PyQt6.QtCore.QLocale.language`, :sip:ref:`~PyQt6.QtCore.QLocale.script` and :sip:ref:`~PyQt6.QtCore.QLocale.country`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.setDefault`, :sip:ref:`~PyQt6.QtCore.QLocale.language`, :sip:ref:`~PyQt6.QtCore.QLocale.script`, :sip:ref:`~PyQt6.QtCore.QLocale.country`.
