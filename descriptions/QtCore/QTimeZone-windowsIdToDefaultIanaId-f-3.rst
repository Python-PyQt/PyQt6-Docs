.. sip:method-description::
    :status: todo
    :pysig: 562825e6224d26631f21810dfe83a806
    :realsig: (const QByteArray&, QLocale::Territory)
    :digest: 76eaad327f82556288e951a6a45caa0a

Returns the default IANA ID for a given *windowsId* and *territory*.

Because a Windows ID can cover several IANA IDs within a given territory, the most frequently used IANA ID in that territory is returned.

As a special case, :sip:ref:`~PyQt6.QtCore.QLocale.Country.AnyTerritory` returns the default of those IANA IDs that have no known territorial association.

This method is only available when feature ``timezone`` is enabled.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.ianaIdToWindowsId`, :sip:ref:`~PyQt6.QtCore.QTimeZone.windowsIdToIanaIds`, :sip:ref:`~PyQt6.QtCore.QTimeZone.territory`.
