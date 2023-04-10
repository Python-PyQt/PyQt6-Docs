.. sip:method-description::
    :status: todo
    :pysig: 8e2eb029a1edf7b5c64e6b25f7203431
    :realsig: (QDate,QTime,Qt::TimeSpec,int)
    :digest: ab03df62ac194db6e43afb847b46d60e

Use ``QDateTime(date, time)`` or ``QDateTime(date, time, QTimeZone::fromSecondsAheadOfUtc(offsetSeconds))``.

Constructs a datetime with the given *date* and *time*, using the time representation implied by *spec* and *offsetSeconds* seconds.

If *date* is valid and *time* is not, the time will be set to midnight.

If *spec* is not :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.OffsetFromUTC` then *offsetSeconds* will be ignored. If *spec* is :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.OffsetFromUTC` and *offsetSeconds* is 0 then the :sip:ref:`~PyQt6.QtCore.QDateTime.timeSpec` will be set to :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.UTC`, i.e. an offset of 0 seconds.

If *spec* is :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.TimeZone` then the spec will be set to :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.LocalTime`, i.e. the current system time zone. To create a :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.TimeZone` datetime use the correct constructor.

If *date* lies outside the range of dates representable by :sip:ref:`~PyQt6.QtCore.QDateTime`, the result is invalid. If *spec* is :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.LocalTime` and the system's time-zone skipped over the given date and time, the result is invalid.
