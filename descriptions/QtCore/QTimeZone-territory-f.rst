.. sip:method-description::
    :status: todo
    :pysig: 25432847a14eb2e52909fa04a070d2ea
    :realsig: () const
    :digest: a47b91bdb3cfa89a280de2aa9a624d2d

Returns the territory for the time zone.

A return of :sip:ref:`~PyQt6.QtCore.QLocale.Country.AnyTerritory` means the zone has no known territorial association. In some cases this may be because the zone has no associated territory - for example, UTC - or because the zone is used in several territories - for example, CET. In other cases, the :sip:ref:`~PyQt6.QtCore.QTimeZone` backend may not know which territory the zone is associated with - for example, because it is not the primary zone of the territory in which it is used.

This method is only available when feature ``timezone`` is enabled.
