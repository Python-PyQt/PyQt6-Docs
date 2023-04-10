.. sip:method-description::
    :status: todo
    :pysig: 41249efbb941c4220a2536f4c7898d9d
    :realsig: (int) const
    :digest: ce6ba62a4d3fef8f130248b544d4970b

Returns a copy of this datetime converted to a spec of :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.OffsetFromUTC` with the given *offsetSeconds*. Equivalent to ``toTimeZone(QTimeZone::fromSecondsAheadOfUtc(offsetSeconds))``.

If the *offsetSeconds* equals 0 then a UTC datetime will be returned.

The result represents the same moment in time as, and is equal to, this datetime.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime.setOffsetFromUtc`, :sip:ref:`~PyQt6.QtCore.QDateTime.offsetFromUtc`, :sip:ref:`~PyQt6.QtCore.QDateTime.toTimeZone`.
