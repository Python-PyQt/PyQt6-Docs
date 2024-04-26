.. sip:method-description::
    :status: todo
    :pysig: c7bfc1cba36c8b80550b3d1b7d3cc3a7
    :realsig: (const QByteArray&,int,const QString&,const QString&,QLocale::Territory,const QString&)
    :digest: 1a75cd6ada80eb78dbf04e7fb6385c2f

Creates a custom time zone instance at fixed offset from UTC.

The returned time zone has an ID of *zoneId* and an offset from UTC of *offsetSeconds*. The *name* will be the name used by :sip:ref:`~PyQt6.QtCore.QTimeZone.displayName` for the :sip:ref:`~PyQt6.QtCore.QTimeZone.NameType.LongName`, the *abbreviation* will be used by :sip:ref:`~PyQt6.QtCore.QTimeZone.displayName` for the :sip:ref:`~PyQt6.QtCore.QTimeZone.NameType.ShortName` and by :sip:ref:`~PyQt6.QtCore.QTimeZone.abbreviation`, and the optional *territory* will be used by :sip:ref:`~PyQt6.QtCore.QTimeZone.territory`. The *comment* is an optional note that may be displayed in a GUI to assist users in selecting a time zone.

The *zoneId* *must not* be one of the available system IDs returned by :sip:ref:`~PyQt6.QtCore.QTimeZone.availableTimeZoneIds`. The *offsetSeconds* from UTC must be in the range -16 hours to +16 hours.

If the custom time zone does not have a specific territory then set it to the default value of :sip:ref:`~PyQt6.QtCore.QLocale.Country.AnyTerritory`.

This constructor is only available when feature ``timezone`` is enabled.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.id`, :sip:ref:`~PyQt6.QtCore.QTimeZone.offsetFromUtc`, :sip:ref:`~PyQt6.QtCore.QTimeZone.displayName`, :sip:ref:`~PyQt6.QtCore.QTimeZone.abbreviation`, :sip:ref:`~PyQt6.QtCore.QTimeZone.territory`, :sip:ref:`~PyQt6.QtCore.QTimeZone.comment`, MinUtcOffsetSecs, MaxUtcOffsetSecs.
