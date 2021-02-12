.. sip:method-description::
    :status: todo
    :pysig: e9501ebb4868285b8a317efaae329f55
    :realsig: (const QByteArray&)
    :digest: c04a83702f9b5fd54846a6c138fd497e

Returns the default IANA ID for a given *windowsId*.

Because a Windows ID can cover several IANA IDs in several different countries, this function returns the most frequently used IANA ID with no regard for the country and should thus be used with care. It is usually best to request the default for a specific country.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.ianaIdToWindowsId`, :sip:ref:`~PyQt6.QtCore.QTimeZone.windowsIdToIanaIds`.
