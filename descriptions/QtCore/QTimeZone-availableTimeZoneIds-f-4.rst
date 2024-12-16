.. sip:method-description::
    :status: todo
    :pysig: 29737c35c54bc24115556b82f9745fe1
    :realsig: (QLocale::Territory)
    :digest: 32a5cec6b917505e6cd8ac6fd2aaca2a

Returns a list of all available IANA time zone IDs for a given *territory*.

As a special case, a *territory* of :sip:ref:`~PyQt6.QtCore.QLocale.Country.AnyTerritory` selects those time zones that have no known territorial association, such as UTC. If you require a list of all time zone IDs for all territories then use the standard :sip:ref:`~PyQt6.QtCore.QTimeZone.availableTimeZoneIds` method.

This method is only available when feature ``timezone`` is enabled.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.isTimeZoneIdAvailable`, :sip:ref:`~PyQt6.QtCore.QTimeZone.territory`.
