.. sip:method-description::
    :status: todo
    :pysig: db474dbce032c5494846cc7830a7c7e0
    :realsig: (const QByteArray&, QLocale::Territory)
    :digest: fba6524b491c90707fa37e0dedb7fe11

Returns all the IANA IDs for a given *windowsId* and *territory*.

As a special case, :sip:ref:`~PyQt6.QtCore.QLocale.Country.AnyTerritory` selects those IANA IDs that have a non-territorial association, while :sip:ref:`~PyQt6.QtCore.QLocale.Country.World` selects the default for the given *windowsId* in territories that have no specific association with it.

The returned list is in order of frequency of usage, i.e. larger zones within a territory are listed first.

This method is only available when feature ``timezone`` is enabled.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.ianaIdToWindowsId`, :sip:ref:`~PyQt6.QtCore.QTimeZone.windowsIdToDefaultIanaId`, :sip:ref:`~PyQt6.QtCore.QTimeZone.territory`.
