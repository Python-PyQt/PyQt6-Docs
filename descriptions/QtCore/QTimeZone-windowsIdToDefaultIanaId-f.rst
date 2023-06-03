.. sip:method-description::
    :status: todo
    :pysig: e9501ebb4868285b8a317efaae329f55
    :realsig: (const QByteArray&)
    :digest: 8f838cd282996681771bb4cd435adc43

Returns the default IANA ID for a given *windowsId*.

Because a Windows ID can cover several IANA IDs in several different territories, this function returns the most frequently used IANA ID with no regard for the territory and should thus be used with care. It is usually best to request the default for a specific territory.

This method is only available when feature ``timezone`` is enabled.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.ianaIdToWindowsId`, :sip:ref:`~PyQt6.QtCore.QTimeZone.windowsIdToIanaIds`.
