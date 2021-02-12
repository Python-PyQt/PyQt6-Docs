.. sip:method-description::
    :status: todo
    :pysig: 67ee2b41666e72cf350bc2e589a4b154
    :realsig: (const QDateTime&) const
    :digest: b221fa5ba1d34a20a807bde3e58e8d63

Returns the time zone abbreviation at the given *atDateTime*. The abbreviation may change depending on DST or even historical events.

Note that the abbreviation is not guaranteed to be unique to this time zone and should not be used in place of the ID or display name.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeZone.displayName`.
