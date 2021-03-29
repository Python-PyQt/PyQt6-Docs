.. sip:method-description::
    :status: todo
    :pysig: 6b5df3cd8b894dbcfbc298c87fe08d5f
    :realsig: (const QDateTime&) const
    :digest: 723fb20adddb93ec5f1a5586e7e660bc

Returns the daylight-saving time offset at the given *atDateTime*, i.e. the number of seconds to add to the standard time offset to obtain the local daylight-saving time.

For example, for the time zone "Europe/Berlin" the DST offset is +3600 seconds. During standard time  will return 0, and when daylight-saving is in effect it will return +3600.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.offsetFromUtc`, :sip:ref:`~PyQt6.QtCore.QTimeZone.standardTimeOffset`.
