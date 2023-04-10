.. sip:method-description::
    :status: todo
    :pysig: 25c78415fd7487087c7fbba8b11ae943
    :realsig: (const QTimeZone&) const
    :digest: 79d23d19c51b9e8c9a439ff18f6ec100

Returns the start-moment of the day.

When a day starts depends on a how time is described: each day starts and ends earlier for those in time-zones further west and later for those in time-zones further east. The time representation to use can be specified by an optional time *zone*. The default time representation is the system's local time.

Usually, the start of the day is midnight, 00:00: however, if a time-zone transition causes the given date to skip over that midnight (e.g. a DST spring-forward skipping over the first hour of the day day), the actual earliest time in the day is returned. This can only arise when the time representation is a time-zone or local time.

When *zone* has a timeSpec() of is :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.OffsetFromUTC` or :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.UTC`, the time representation has no transitions so the start of the day is :sip:ref:`~PyQt6.QtCore.QTime`\ (0, 0).

In the rare case of a date that was entirely skipped (this happens when a zone east of the international date-line switches to being west of it), the return shall be invalid. Passing an invalid time-zone as *zone* will also produce an invalid result, as shall dates that start outside the range representable by :sip:ref:`~PyQt6.QtCore.QDateTime`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDate.endOfDay`.
