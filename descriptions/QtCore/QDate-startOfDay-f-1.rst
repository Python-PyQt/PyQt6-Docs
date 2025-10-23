.. sip:method-description::
    :status: todo
    :pysig: 2d10d6c7e48af6be6801c538cf3f30ce
    :realsig: (Qt::TimeSpec,int) const
    :digest: 691aeb4c8ce595d198dbf645d3e25adf

Use ``startOfDay(const QTimeZone &)`` instead.

Returns the start-moment of the day.

When a day starts depends on a how time is described: each day starts and ends earlier for those with higher offsets from UTC and later for those with lower offsets from UTC. The time representation to use can be specified either by a *spec* and *offsetSeconds* (ignored unless *spec* is Qt::OffsetSeconds) or by a time zone.

Usually, the start of the day is midnight, 00:00: however, if a local time transition causes the given date to skip over that midnight (e.g. a DST spring-forward skipping over the first hour of the day day), the actual earliest time in the day is returned.

When *spec* is :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.OffsetFromUTC`, *offsetSeconds* gives an implied zone's offset from UTC. As UTC and such zones have no transitions, the start of the day is :sip:ref:`~PyQt6.QtCore.QTime`\ (0, 0) in these cases.

In the rare case of a date that was entirely skipped (this happens when a zone east of the international date-line switches to being west of it), the return shall be invalid. Passing :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.TimeZone` as *spec* (instead of passing a :sip:ref:`~PyQt6.QtCore.QTimeZone`) will also produce an invalid result, as shall dates that start outside the range representable by :sip:ref:`~PyQt6.QtCore.QDateTime`.
