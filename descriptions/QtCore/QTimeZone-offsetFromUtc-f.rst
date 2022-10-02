.. sip:method-description::
    :status: todo
    :pysig: 6b5df3cd8b894dbcfbc298c87fe08d5f
    :realsig: (const QDateTime&) const
    :digest: b814dc122c920d264a5a6c51d472c311

Returns the total effective offset at the given *atDateTime*, i.e. the number of seconds to add to UTC to obtain the local time. This includes any DST offset that may be in effect, i.e. it is the sum of :sip:ref:`~PyQt6.QtCore.QTimeZone.standardTimeOffset` and :sip:ref:`~PyQt6.QtCore.QTimeZone.daylightTimeOffset` for the given datetime.

For example, for the time zone "Europe/Berlin" the standard time offset is +3600 seconds and the DST offset is +3600 seconds. During standard time offsetFromUtc() will return +3600 (UTC+01:00), and during DST it will return +7200 (UTC+02:00).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.standardTimeOffset`, :sip:ref:`~PyQt6.QtCore.QTimeZone.daylightTimeOffset`.
