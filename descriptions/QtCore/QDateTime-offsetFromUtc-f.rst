.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: b4205f2222af9750d9f72b033866102c

Returns this datetime's Offset From UTC in seconds.

The result depends on :sip:ref:`~PyQt6.QtCore.QDateTime.timeSpec`:

* ``Qt::UTC`` The offset is 0.

* ``Qt::OffsetFromUTC`` The offset is the value originally set.

* ``Qt::LocalTime`` The local time's offset from UTC is returned.

* ``Qt::TimeZone`` The offset used by the time-zone is returned.

For the last two, the offset at this date and time will be returned, taking account of Daylight-Saving Offset. The offset is the difference between the local time or time in the given time-zone and UTC time; it is positive in time-zones ahead of UTC (East of The Prime Meridian), negative for those behind UTC (West of The Prime Meridian).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime.setOffsetFromUtc`.
