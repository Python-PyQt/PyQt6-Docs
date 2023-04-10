.. sip:method-description::
    :status: todo
    :pysig: 6b5df3cd8b894dbcfbc298c87fe08d5f
    :realsig: (const QDateTime&) const
    :digest: 51c553f30561a632c7461558dd968fb5

Returns the standard time offset at the given *atDateTime*, i.e. the number of seconds to add to UTC to obtain the local Standard Time. This excludes any DST offset that may be in effect.

For example, for the time zone "Europe/Berlin" the standard time offset is +3600 seconds. During both standard and DST :sip:ref:`~PyQt6.QtCore.QTimeZone.offsetFromUtc` will return +3600 (UTC+01:00).

This method is only available when feature ``timezone`` is enabled.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.offsetFromUtc`, :sip:ref:`~PyQt6.QtCore.QTimeZone.daylightTimeOffset`.
