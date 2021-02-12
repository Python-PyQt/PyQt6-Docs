.. sip:method-description::
    :status: todo
    :pysig: ca127cf173eb8c54db33d1c465630b2c
    :realsig: (QLocale::Language,QLocale::Script,QLocale::Country)
    :digest: 7b17bb1be9c54e1ad35b5aed1415dc29

Returns a list of valid locale objects that match the given *language*, *script* and *country*.

Getting a list of all locales: QList<\ :sip:ref:`~PyQt6.QtCore.QLocale`> allLocales = (\ :sip:ref:`~PyQt6.QtCore.QLocale.Language.AnyLanguage`, :sip:ref:`~PyQt6.QtCore.QLocale.Script.AnyScript`, :sip:ref:`~PyQt6.QtCore.QLocale.Country.AnyCountry`);

Getting a list of locales suitable for Russia: QList<\ :sip:ref:`~PyQt6.QtCore.QLocale`> locales = (\ :sip:ref:`~PyQt6.QtCore.QLocale.Language.AnyLanguage`, :sip:ref:`~PyQt6.QtCore.QLocale.Script.AnyScript`, :sip:ref:`~PyQt6.QtCore.QLocale.Country.Russia`);
