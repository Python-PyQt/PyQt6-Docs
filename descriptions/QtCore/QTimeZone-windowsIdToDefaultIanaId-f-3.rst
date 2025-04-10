.. sip:method-description::
    :status: todo
    :pysig: 562825e6224d26631f21810dfe83a806
    :realsig: (const QByteArray&, QLocale::Territory)
    :digest: 2d3360dc64aa8b5d369bda8e3407336e

Returns the default IANA ID for a given *windowsId* and *territory*.

Because a Windows ID can cover several IANA IDs within a given territory, the most frequently used IANA ID in that territory is returned.

As a special case, :sip:ref:`~PyQt6.QtCore.QLocale.Country.AnyTerritory` returns the default of those IANA IDs that have a non-territorial association, while :sip:ref:`~PyQt6.QtCore.QLocale.Country.World` returns the default for the given *windowsId* in territories that have no specific association with it.

If the return is empty, there is no IANA ID specific to the given *territory* for this *windowsId*. It is reasonable, in this case, to fall back to ``windowsIdToDefaultIanaId(windowsId)``.

This method is only available when feature ``timezone`` is enabled.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.ianaIdToWindowsId`, :sip:ref:`~PyQt6.QtCore.QTimeZone.windowsIdToIanaIds`, :sip:ref:`~PyQt6.QtCore.QTimeZone.territory`.
