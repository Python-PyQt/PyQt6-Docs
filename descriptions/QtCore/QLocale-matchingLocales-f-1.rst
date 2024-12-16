.. sip:method-description::
    :status: todo
    :pysig: 3ba7bf58b86014b02a3f3be55d4a7655
    :realsig: (QLocale::Language, QLocale::Script, QLocale::Territory)
    :digest: ba49db947ca03e4d33c1948821122432

Returns a list of valid locale objects that match the given *language*, *script* and *territory*.

Getting a list of all locales: QList<\ :sip:ref:`~PyQt6.QtCore.QLocale`> allLocales = QLocale::matchingLocales(\ :sip:ref:`~PyQt6.QtCore.QLocale.Language.AnyLanguage`, :sip:ref:`~PyQt6.QtCore.QLocale.Script.AnyScript`, :sip:ref:`~PyQt6.QtCore.QLocale.Country.AnyTerritory`);

Getting a list of locales suitable for Russia: QList<\ :sip:ref:`~PyQt6.QtCore.QLocale`> locales = QLocale::matchingLocales(\ :sip:ref:`~PyQt6.QtCore.QLocale.Language.AnyLanguage`, :sip:ref:`~PyQt6.QtCore.QLocale.Script.AnyScript`, :sip:ref:`~PyQt6.QtCore.QLocale.Country.Russia`);
