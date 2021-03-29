.. sip:method-description::
    :status: todo
    :pysig: e1b64a4356ad71fb3e60d75bec6ee041
    :realsig: (const QByteArray&,QLocale::Country)
    :digest: efd54cd0a7ba0ae0da1039e03bd6fdf1

Returns all the IANA IDs for a given *windowsId* and *country*.

As a special case :sip:ref:`~PyQt6.QtCore.QLocale.Country.AnyCountry` returns those IANA IDs that do not have any specific country.

The returned list is in order of frequency of usage, i.e. larger zones within a country are listed first.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.ianaIdToWindowsId`, :sip:ref:`~PyQt6.QtCore.QTimeZone.windowsIdToDefaultIanaId`.
