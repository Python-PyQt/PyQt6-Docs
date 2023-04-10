.. sip:class-description::
    :status: todo
    :brief: Identifies how a time representation relates to UTC
    :digest: 13de6eb2feb4b0f6d8fdb9e360c1d623

:sip:ref:`~PyQt6.QtCore.QTimeZone` identifies how a time representation relates to UTC.

When dates and times are combined, the meaning of the result depends on how time is being represented. There are various international standards for representing time; one of these, UTC, corresponds to the traditional standard of solar mean time at Greenwich (a.k.a. GMT). All other time systems supported by Qt are ultimately specified in relation to UTC. An instance of this class provides a stateless calculator for conversions between UTC and other time representations.

Some time representations are simply defined at a fixed offset to UTC. Others are defined by governments for use within their jurisdictions. The latter are properly known as time zones, but :sip:ref:`~PyQt6.QtCore.QTimeZone` (since Qt 6.5) is unifies their representation with that of general time systems. One time zone generally supported on most operating systems is designated local time; this is presumed to correspond to the time zone within which the user is living.

For time zones other than local time, UTC and those at fixed offsets from UTC, Qt can only provide support when the operating system provides some way to access that information. When Qt is built, the ``timezone`` feature controls whether such information is available. When it is not, some constructors and methods of :sip:ref:`~PyQt6.QtCore.QTimeZone` are excluded from its API; these are documented as depending on feature ``timezone``. Note that, even when Qt is built with this feature enabled, it may be unavailable to users whose systems are misconfigured, or where some standard packages (for example, the ``tzdata`` package on Linux) are not installed. This feature is enabled by default when time zone information is available.

This class is primarily designed for use in :sip:ref:`~PyQt6.QtCore.QDateTime`; most applications will not need to access this class directly and should instead use an instance of it when constructing a :sip:ref:`~PyQt6.QtCore.QDateTime`.

**Note:** For consistency with :sip:ref:`~PyQt6.QtCore.QDateTime`, :sip:ref:`~PyQt6.QtCore.QTimeZone` does not account for leap seconds.

.. _qtimezone-remarks:

Remarks
-------

:sip:ref:`~PyQt6.QtCore.QTimeZone`, like :sip:ref:`~PyQt6.QtCore.QDateTime`, measures offsets from UTC in seconds. This contrasts with their measurement of time generally, which they do in milliseconds. Real-world time zones generally have UTC offsets that are whole-number multiples of five minutes (300 seconds), at least since well before 1970. A positive offset from UTC gives a time representation puts noon on any given day before UTC noon on that day; a negative offset puts noon after UTC noon on the same day.

.. _qtimezone-lightweight-time-representations:

Lightweight Time Representations
................................

:sip:ref:`~PyQt6.QtCore.QTimeZone` can represent UTC, local time and fixed offsets from UTC even when feature ``timezone`` is disabled. The form in which it does so is also available when the feature is enabled; it is a more lightweight form and processing using it will typically be more efficient, unless methods only available when feature ``timezone`` is enabled are being exercised. See :sip:ref:`~PyQt6.QtCore.QTimeZone.Initialization.Initialization` and QTimeZone::fromSecondsAheadOfUtc(int) for how to construct these representations.

This documentation distinguishes between "time zone", used to describe a time representation described by system-supplied or standard information, and time representations more generally, which include these lightweight forms. The methods available only when feature ``timezone`` is enabled are apt to be cheaper for time zones than for lightweight time representations, for which these methods may construct a suitable transient time zone object to which to forward the query.

.. _qtimezone-iana-time-zone-ids:

IANA Time Zone IDs
..................

:sip:ref:`~PyQt6.QtCore.QTimeZone` uses the IANA time zone IDs as defined in the IANA Time Zone Database (http://www.iana.org/time-zones). This is to ensure a standard ID across all supported platforms. Most platforms support the IANA IDs and the IANA Database natively, but for Windows a mapping is required to the native IDs. See below for more details.

The IANA IDs can and do change on a regular basis, and can vary depending on how recently the host system data was updated. As such you cannot rely on any given ID existing on any host system. You must use :sip:ref:`~PyQt6.QtCore.QTimeZone.availableTimeZoneIds` to determine what IANA IDs are available.

The IANA IDs and database are also know as the Olson IDs and database, named after the original compiler of the database.

.. _qtimezone-utc-offset-time-zones:

UTC Offset Time Zones
.....................

A default UTC time zone backend is provided which is always available when feature ``timezone`` is enabled. This provides a set of generic Offset From UTC time zones in the range UTC-14:00 to UTC+14:00. These time zones can be created using either the standard ISO format names, such as "UTC+00:00", as listed by :sip:ref:`~PyQt6.QtCore.QTimeZone.availableTimeZoneIds`, or using a name of similar form in combination with the number of offset seconds.

.. _qtimezone-windows-time-zones:

Windows Time Zones
..................

Windows native time zone support is severely limited compared to the standard IANA TZ Database. Windows time zones cover larger geographic areas and are thus less accurate in their conversions. They also do not support as much historical data and so may only be accurate for the current year. In particular, when MS's zone data claims that DST was observed prior to 1900 (this is historically known to be untrue), the claim is ignored and the standard time (allegedly) in force in 1900 is taken to have always been in effect.

:sip:ref:`~PyQt6.QtCore.QTimeZone` uses a conversion table derived from the Unicode CLDR data to map between IANA IDs and Windows IDs. Depending on your version of Windows and Qt, this table may not be able to provide a valid conversion, in which "UTC" will be returned.

:sip:ref:`~PyQt6.QtCore.QTimeZone` provides a public API to use this conversion table. The Windows ID used is the Windows Registry Key for the time zone which is also the MS Exchange EWS ID as well, but is different to the Time Zone Name (TZID) and COD code used by MS Exchange in versions before 2007.

**Note:** When Qt is built with the ICU library, it is used in preference to the Windows system APIs, bypassing all problems with those APIs using different names.

.. _qtimezone-system-time-zone:

System Time Zone
................

The method :sip:ref:`~PyQt6.QtCore.QTimeZone.systemTimeZoneId` returns the current system IANA time zone ID which on Unix-like systems will always be correct. On Windows this ID is translated from the Windows system ID using an internal translation table and the user's selected country. As a consequence there is a small chance any Windows install may have IDs not known by Qt, in which case "UTC" will be returned.

Creating a new :sip:ref:`~PyQt6.QtCore.QTimeZone` instance using the system time zone ID will only produce a fixed named copy of the time zone, it will not change if the system time zone changes. :sip:ref:`~PyQt6.QtCore.QTimeZone.systemTimeZone` will return an instance representing the zone named by this system ID. Note that constructing a :sip:ref:`~PyQt6.QtCore.QDateTime` using this system zone may behave differently than constructing a :sip:ref:`~PyQt6.QtCore.QDateTime` that uses :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.LocalTime` as its :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec`, as the latter directly uses system APIs for accessing local time information, which may behave differently (and, in particular, might adapt if the user adjusts the system zone setting).

.. _qtimezone-time-zone-offsets:

Time Zone Offsets
.................

The difference between UTC and the local time in a time zone is expressed as an offset in seconds from UTC, i.e. the number of seconds to add to UTC to obtain the local time. The total offset is comprised of two component parts, the standard time offset and the daylight-saving time offset. The standard time offset is the number of seconds to add to UTC to obtain standard time in the time zone. The daylight-saving time offset is the number of seconds to add to the standard time offset to obtain daylight-saving time (abbreviated DST and sometimes called "daylight time" or "summer time") in the time zone. The usual case for DST (using standard time in winter, DST in summer) has a positive daylight-saving time offset. However, some zones have negative DST offsets, used in winter, with summer using standard time.

Note that the standard and DST offsets for a time zone may change over time as countries have changed DST laws or even their standard time offset.

.. _qtimezone-license:

License
.......

This class includes data obtained from the CLDR data files under the terms of the Unicode Data Files and Software License. See Unicode Common Locale Data Repository (CLDR) for details.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime`, :sip:ref:`~PyQt6.QtCore.QCalendar`.
