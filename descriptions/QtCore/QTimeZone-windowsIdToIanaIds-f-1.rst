.. sip:method-description::
    :status: todo
    :pysig: db474dbce032c5494846cc7830a7c7e0
    :realsig: (const QByteArray&, QLocale::Territory)
    :digest: 637e9a360fd602955a20369dc83d6ffa

Returns all the IANA IDs for a given *windowsId* and *territory*.

As a special case, :sip:ref:`~PyQt6.QtCore.QLocale.Country.AnyTerritory` selects those IANA IDs that have no known territorial association.

The returned list is in order of frequency of usage, i.e. larger zones within a territory are listed first.

This method is only available when feature ``timezone`` is enabled.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.ianaIdToWindowsId`, :sip:ref:`~PyQt6.QtCore.QTimeZone.windowsIdToDefaultIanaId`, :sip:ref:`~PyQt6.QtCore.QTimeZone.territory`.
