.. sip:method-description::
    :status: todo
    :pysig: 378fd81ac48242b31891e6cc04d4c188
    :realsig: (const QByteArray&,int,const QString&,const QString&,QLocale::Country,const QString&)
    :digest: 2abd3a0b3f8f1b7e00907d37c062a906

Creates a custom time zone with an ID of *ianaId* and an offset from UTC of *offsetSeconds*. The *name* will be the name used by :sip:ref:`~PyQt6.QtCore.QTimeZone.displayName` for the :sip:ref:`~PyQt6.QtCore.QTimeZone.NameType.LongName`, the *abbreviation* will be used by :sip:ref:`~PyQt6.QtCore.QTimeZone.displayName` for the :sip:ref:`~PyQt6.QtCore.QTimeZone.NameType.ShortName` and by :sip:ref:`~PyQt6.QtCore.QTimeZone.abbreviation`, and the optional *country* will be used by :sip:ref:`~PyQt6.QtCore.QTimeZone.country`. The *comment* is an optional note that may be displayed in a GUI to assist users in selecting a time zone.

The *ianaId* must not be one of the available system IDs returned by :sip:ref:`~PyQt6.QtCore.QTimeZone.availableTimeZoneIds`. The *offsetSeconds* from UTC must be in the range -14 hours to +14 hours.

If the custom time zone does not have a specific country then set it to the default value of :sip:ref:`~PyQt6.QtCore.QLocale.Country.AnyCountry`.
