.. sip:method-description::
    :status: todo
    :pysig: 9a83d46629b34c5923cf484fbb5ca1fc
    :realsig: (const QByteArray&,QLocale::Country)
    :digest: c80b36c6939994703e91c6414d056356

Returns the default IANA ID for a given *windowsId* and *country*.

Because a Windows ID can cover several IANA IDs within a given country, the most frequently used IANA ID in that country is returned.

As a special case, :sip:ref:`~PyQt6.QtCore.QLocale.Country.AnyCountry` returns the default of those IANA IDs that do not have any specific country.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.ianaIdToWindowsId`, :sip:ref:`~PyQt6.QtCore.QTimeZone.windowsIdToIanaIds`.
