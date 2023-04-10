.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 6ff50921fbd9ad94ce835bab121d217d

Returns ``true`` if this datetime represents a definite moment, otherwise ``false``.

A datetime is valid if both its date and its time are valid and the time representation used gives a valid meaning to their combination. When the time representation is a specific time-zone or local time, there may be times on some dates that the zone skips in its representation, as when a daylight-saving transition skips an hour (typically during a night in spring). For example, if DST ends at 2am with the clock advancing to 3am, then datetimes from 02:00:00 to 02:59:59.999 on that day are invalid.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime.YearRange`, :sip:ref:`~PyQt6.QtCore.QDate.isValid`, :sip:ref:`~PyQt6.QtCore.QTime.isValid`.
