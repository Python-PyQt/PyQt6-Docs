.. sip:method-description::
    :status: todo
    :pysig: 41249efbb941c4220a2536f4c7898d9d
    :realsig: (qint64) const
    :digest: 082c18f653b172367f9fd3b292998324

Returns a :sip:ref:`~PyQt6.QtCore.QDateTime` object containing a datetime *ndays* days later than the datetime of this object (or earlier if *ndays* is negative).

If the :sip:ref:`~PyQt6.QtCore.QDateTime.timeSpec` is :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.LocalTime` or :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.TimeZone` and the resulting date and time fall in the Standard Time to Daylight-Saving Time transition hour then the result will be just beyond this gap, in the direction of change. If the transition is at 2am and the clock goes forward to 3am, the result of aiming between 2am and 3am will be adjusted to fall before 2am (if ``ndays < 0``) or after 3am (otherwise).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime.daysTo`, :sip:ref:`~PyQt6.QtCore.QDateTime.addMonths`, :sip:ref:`~PyQt6.QtCore.QDateTime.addYears`, :sip:ref:`~PyQt6.QtCore.QDateTime.addSecs`, :ref:`qdatetime-timezone-transitions`.
