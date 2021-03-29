.. sip:method-description::
    :status: todo
    :pysig: 6b5df3cd8b894dbcfbc298c87fe08d5f
    :realsig: (const QDateTime&) const
    :digest: 7017170850ab20b01491e7739b3e00d9

Returns the standard time offset at the given *atDateTime*, i.e. the number of seconds to add to UTC to obtain the local Standard Time. This excludes any DST offset that may be in effect.

For example, for the time zone "Europe/Berlin" the standard time offset is +3600 seconds. During both standard and DST :sip:ref:`~PyQt6.QtCore.QTimeZone.offsetFromUtc` will return +3600 (UTC+01:00).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.offsetFromUtc`, :sip:ref:`~PyQt6.QtCore.QTimeZone.daylightTimeOffset`.
