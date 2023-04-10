.. sip:class-description::
    :status: todo
    :brief: Date and time functions
    :digest: 4cb7ad685bc6d51c5ccc01d006203a8b

The :sip:ref:`~PyQt6.QtCore.QDateTime` class provides date and time functions.

A :sip:ref:`~PyQt6.QtCore.QDateTime` object encodes a calendar date and a clock time (a "datetime") in accordance with a time representation. It combines features of the :sip:ref:`~PyQt6.QtCore.QDate` and :sip:ref:`~PyQt6.QtCore.QTime` classes. It can read the current datetime from the system clock. It provides functions for comparing datetimes and for manipulating a datetime by adding a number of seconds, days, months, or years.

:sip:ref:`~PyQt6.QtCore.QDateTime` can describe datetimes with respect to :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.LocalTime`, to :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.UTC`, to a specified :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.OffsetFromUTC` or to a specified :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.TimeZone`. Each of these time representations can be encapsulated in a suitable instance of the :sip:ref:`~PyQt6.QtCore.QTimeZone` class. For example, a time zone of "Europe/Berlin" will apply the daylight-saving rules as used in Germany. In contrast, a fixed offset from UTC of +3600 seconds is one hour ahead of UTC (usually written in ISO standard notation as "UTC+01:00"), with no daylight-saving complications. When using either local time or a specified time zone, time-zone transitions (see :ref:`qdatetime-daylight-saving-time-dst`) are taken into account. A :sip:ref:`~PyQt6.QtCore.QDateTime`'s :sip:ref:`~PyQt6.QtCore.QDateTime.timeSpec` will tell you which of the four types of time representation is in use; its :sip:ref:`~PyQt6.QtCore.QDateTime.timeRepresentation` provides a full representation of that time representation, as a :sip:ref:`~PyQt6.QtCore.QTimeZone`.

A :sip:ref:`~PyQt6.QtCore.QDateTime` object is typically created either by giving a date and time explicitly in the constructor, or by using a static function such as :sip:ref:`~PyQt6.QtCore.QDateTime.currentDateTime` or fromMSecsSinceEpoch(). The date and time can be changed with :sip:ref:`~PyQt6.QtCore.QDateTime.setDate` and :sip:ref:`~PyQt6.QtCore.QDateTime.setTime`. A datetime can also be set using the :sip:ref:`~PyQt6.QtCore.QDateTime.setMSecsSinceEpoch` function that takes the time, in milliseconds, since the start, in UTC of the year 1970. The :sip:ref:`~PyQt6.QtCore.QDateTime.fromString` function returns a :sip:ref:`~PyQt6.QtCore.QDateTime`, given a string and a date format used to interpret the date within the string.

:sip:ref:`~PyQt6.QtCore.QDateTime.currentDateTime` returns a :sip:ref:`~PyQt6.QtCore.QDateTime` that expresses the current date and time with respect to a specific time representation, such as local time (its default). :sip:ref:`~PyQt6.QtCore.QDateTime.currentDateTimeUtc` returns a :sip:ref:`~PyQt6.QtCore.QDateTime` that expresses the current date and time with respect to UTC; it is equivalent to ``QDateTime::currentDateTime(QTimeZone::UTC)``.

The :sip:ref:`~PyQt6.QtCore.QDateTime.date` and :sip:ref:`~PyQt6.QtCore.QDateTime.time` functions provide access to the date and time parts of the datetime. The same information is provided in textual format by the :sip:ref:`~PyQt6.QtCore.QDateTime.toString` function.

:sip:ref:`~PyQt6.QtCore.QDateTime` provides a full set of operators to compare two :sip:ref:`~PyQt6.QtCore.QDateTime` objects, where smaller means earlier and larger means later.

You can increment (or decrement) a datetime by a given number of milliseconds using :sip:ref:`~PyQt6.QtCore.QDateTime.addMSecs`, seconds using :sip:ref:`~PyQt6.QtCore.QDateTime.addSecs`, or days using :sip:ref:`~PyQt6.QtCore.QDateTime.addDays`. Similarly, you can use :sip:ref:`~PyQt6.QtCore.QDateTime.addMonths` and :sip:ref:`~PyQt6.QtCore.QDateTime.addYears`. The :sip:ref:`~PyQt6.QtCore.QDateTime.daysTo` function returns the number of days between two datetimes, :sip:ref:`~PyQt6.QtCore.QDateTime.secsTo` returns the number of seconds between two datetimes, and :sip:ref:`~PyQt6.QtCore.QDateTime.msecsTo` returns the number of milliseconds between two datetimes. These operations are aware of daylight-saving time (DST) and other time-zone transitions, where applicable.

Use :sip:ref:`~PyQt6.QtCore.QDateTime.toTimeZone` to re-express a datetime in terms of a different time representation. By passing a lightweight :sip:ref:`~PyQt6.QtCore.QTimeZone` that represents local time, UTC or a fixed offset from UTC, you can convert the datetime to use the corresponding time representation; or you can pass a full time zone (whose :sip:ref:`~PyQt6.QtCore.QTimeZone.timeSpec` is ``Qt::TimeZone``) to use that instead.

**Note:** :sip:ref:`~PyQt6.QtCore.QDateTime` does not account for leap seconds.

.. _qdatetime-remarks:

Remarks
-------

**Note:** All conversion to and from string formats is done using the C locale. For localized conversions, see :sip:ref:`~PyQt6.QtCore.QLocale`.

**Note:** There is no year 0 in the Gregorian calendar. Dates in that year are considered invalid. The year -1 is the year "1 before Christ" or "1 before common era." The day before 1 January 1 CE is 31 December 1 BCE.

.. _qdatetime-range-of-valid-dates:

Range of Valid Dates
....................

The range of values that :sip:ref:`~PyQt6.QtCore.QDateTime` can represent is dependent on the internal storage implementation. :sip:ref:`~PyQt6.QtCore.QDateTime` is currently stored in a qint64 as a serial msecs value encoding the date and time. This restricts the date range to about +/- 292 million years, compared to the :sip:ref:`~PyQt6.QtCore.QDate` range of +/- 2 billion years. Care must be taken when creating a :sip:ref:`~PyQt6.QtCore.QDateTime` with extreme values that you do not overflow the storage. The exact range of supported values varies depending on the time representation used.

.. _qdatetime-use-of-timezones:

Use of Timezones
................

:sip:ref:`~PyQt6.QtCore.QDateTime` uses the system's time zone information to determine the current local time zone and its offset from UTC. If the system is not configured correctly or not up-to-date, :sip:ref:`~PyQt6.QtCore.QDateTime` will give wrong results.

:sip:ref:`~PyQt6.QtCore.QDateTime` likewise uses system-provided information to determine the offsets of other timezones from UTC. If this information is incomplete or out of date, :sip:ref:`~PyQt6.QtCore.QDateTime` will give wrong results. See the :sip:ref:`~PyQt6.QtCore.QTimeZone` documentation for more details.

On modern Unix systems, this means :sip:ref:`~PyQt6.QtCore.QDateTime` usually has accurate information about historical transitions (including DST, see below) whenever possible. On Windows, where the system doesn't support historical timezone data, historical accuracy is not maintained with respect to timezone transitions, notably including DST. However, building Qt with the ICU library will equipe :sip:ref:`~PyQt6.QtCore.QTimeZone` with the same timezone database as is used on Unix.

.. _qdatetime-daylight-saving-time-dst:

Daylight-Saving Time (DST)
..........................

:sip:ref:`~PyQt6.QtCore.QDateTime` takes into account transitions between Standard Time and Daylight-Saving Time. For example, if the transition is at 2am and the clock goes forward to 3am, then there is a "missing" hour from 02:00:00 to 02:59:59.999 which :sip:ref:`~PyQt6.QtCore.QDateTime` considers to be invalid. Any date arithmetic performed will take this missing hour into account and return a valid result. For example, adding one second to 01:59:59 will get 03:00:00.

For datetimes that the system ``time_t`` can represent (from 1901-12-14 to 2038-01-18 on systems with 32-bit ``time_t``; for the full range :sip:ref:`~PyQt6.QtCore.QDateTime` can represent if the type is 64-bit), the standard system APIs are used to determine local time's offset from UTC. For datetimes not handled by these system APIs, :sip:ref:`~PyQt6.QtCore.QTimeZone.systemTimeZone` is used. In either case, the offset information used depends on the system and may be incomplete or, for past times, historically inaccurate. In any case, for future dates, the local time zone's offsets and DST rules may change before that date comes around.

.. _qdatetime-offsets-from-utc:

Offsets From UTC
................

Offsets from UTC are measured in seconds east of Greenwich. The moment described by a particular date and time, such as noon on a particular day, depends on the time representation used. Those with a higher offset from UTC describe an earlier moment, and those with a lower offset a later moment, by any given combination of date and time.

There is no explicit size restriction on an offset from UTC, but there is an implicit limit imposed when using the :sip:ref:`~PyQt6.QtCore.QDateTime.toString` and :sip:ref:`~PyQt6.QtCore.QDateTime.fromString` methods which use a [+|-]hh:mm format, effectively limiting the range to +/- 99 hours and 59 minutes and whole minutes only. Note that currently no time zone has an offset outside the range of ±14 hours and all known offsets are multiples of five minutes.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDate`, :sip:ref:`~PyQt6.QtCore.QTime`, :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit`, :sip:ref:`~PyQt6.QtCore.QTimeZone`.
