.. sip:method-description::
    :status: todo
    :pysig: 29737c35c54bc24115556b82f9745fe1
    :realsig: (QLocale::Territory)
    :digest: 173c47060bae48259c2016de5f41172f

Returns a list of all available IANA time zone IDs for a given *territory*.

As a special case, a *territory* of :sip:ref:`~PyQt6.QtCore.QLocale.Country.AnyTerritory` selects those time zones that have a non-territorial association, such as UTC, while :sip:ref:`~PyQt6.QtCore.QLocale.Country.World` selects those time-zones for which there is a global default IANA ID. If you require a list of all time zone IDs for all territories then use the standard :sip:ref:`~PyQt6.QtCore.QTimeZone.availableTimeZoneIds` method.

This method is only available when feature ``timezone`` is enabled.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.isTimeZoneIdAvailable`, :sip:ref:`~PyQt6.QtCore.QTimeZone.territory`.
