.. sip:class-description::
    :status: todo
    :brief: Converts between UTC and local time in a specific time zone
    :digest: 737f04c7d4c2ebbf12e87ca114cd0b28

The :sip:ref:`~PyQt6.QtCore.QTimeZone` class converts between UTC and local time in a specific time zone.

This class provides a stateless calculator for time zone conversions between UTC and the local time in a specific time zone. By default it uses the host system time zone data to perform these conversions.

This class is primarily designed for use in :sip:ref:`~PyQt6.QtCore.QDateTime`; most applications will not need to access this class directly and should instead use :sip:ref:`~PyQt6.QtCore.QDateTime` with a :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec` of :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.TimeZone`.

**Note:** For consistency with :sip:ref:`~PyQt6.QtCore.QDateTime`, :sip:ref:`~PyQt6.QtCore.QTimeZone` does not account for leap seconds.

.. _qtimezone-remarks:

Remarks
-------

.. _qtimezone-iana-time-zone-ids:

IANA Time Zone IDs
..................

:sip:ref:`~PyQt6.QtCore.QTimeZone` uses the IANA time zone IDs as defined in the IANA Time Zone Database (http://www.iana.org/time-zones). This is to ensure a standard ID across all supported platforms. Most platforms support the IANA IDs and the IANA Database natively, but for Windows a mapping is required to the native IDs. See below for more details.

The IANA IDs can and do change on a regular basis, and can vary depending on how recently the host system data was updated. As such you cannot rely on any given ID existing on any host system. You must use :sip:ref:`~PyQt6.QtCore.QTimeZone.availableTimeZoneIds` to determine what IANA IDs are available.

The IANA IDs and database are also know as the Olson IDs and database, named after their creator.

.. _qtimezone-utc-offset-time-zones:

UTC Offset Time Zones
.....................

A default UTC time zone backend is provided which is always guaranteed to be available. This provides a set of generic Offset From UTC time zones in the range UTC-14:00 to UTC+14:00. These time zones can be created using either the standard ISO format names "UTC+00:00" as listed by :sip:ref:`~PyQt6.QtCore.QTimeZone.availableTimeZoneIds`, or using the number of offset seconds.

.. _qtimezone-windows-time-zones:

Windows Time Zones
..................

Windows native time zone support is severely limited compared to the standard IANA TZ Database. Windows time zones cover larger geographic areas and are thus less accurate in their conversions. They also do not support as much historic conversion data and so may only be accurate for the current year.

:sip:ref:`~PyQt6.QtCore.QTimeZone` uses a conversion table derived form the Unicode CLDR data to map between IANA IDs and Windows IDs. Depending on your version of Windows and Qt, this table may not be able to provide a valid conversion, in which "UTC" will be returned.

:sip:ref:`~PyQt6.QtCore.QTimeZone` provides a public API to use this conversion table. The Windows ID used is the Windows Registry Key for the time zone which is also the MS Exchange EWS ID as well, but is different to the Time Zone Name (TZID) and COD code used by MS Exchange in versions before 2007.

.. _qtimezone-system-time-zone:

System Time Zone
................

:sip:ref:`~PyQt6.QtCore.QTimeZone` does not support any concept of a system or default time zone. If you require a :sip:ref:`~PyQt6.QtCore.QDateTime` that uses the current system time zone at any given moment then you should use a :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec` of :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.LocalTime`.

The method :sip:ref:`~PyQt6.QtCore.QTimeZone.systemTimeZoneId` returns the current system IANA time zone ID which on Unix-like systems will always be correct. On Windows this ID is translated from the Windows system ID using an internal translation table and the user's selected country. As a consequence there is a small chance any Windows install may have IDs not known by Qt, in which case "UTC" will be returned.

Creating a new :sip:ref:`~PyQt6.QtCore.QTimeZone` instance using the system time zone ID will only produce a fixed named copy of the time zone, it will not change if the system time zone changes.

.. _qtimezone-time-zone-offsets:

Time Zone Offsets
.................

The difference between UTC and the local time in a time zone is expressed as an offset in seconds from UTC, i.e. the number of seconds to add to UTC to obtain the local time. The total offset is comprised of two component parts, the standard time offset and the daylight-saving time offset. The standard time offset is the number of seconds to add to UTC to obtain standard time in the time zone. The daylight-saving time offset is the number of seconds to add to the standard time offset to obtain daylight-saving time (abbreviated DST and sometimes called "daylight time" or "summer time") in the time zone.

Note that the standard and DST offsets for a time zone may change over time as countries have changed DST laws or even their standard time offset.

.. _qtimezone-license:

License
.......

This class includes data obtained from the CLDR data files under the terms of the Unicode Data Files and Software License. See Unicode Common Locale Data Repository (CLDR) for details.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime`.
