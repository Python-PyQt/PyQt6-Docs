.. sip:method-description::
    :status: todo
    :pysig: 41249efbb941c4220a2536f4c7898d9d
    :realsig: (int) const
    :digest: fccf9cabb920c76fed415dbb40829fc0

Returns a :sip:ref:`~PyQt6.QtCore.QDateTime` object containing a datetime *nmonths* months later than the datetime of this object (or earlier if *nmonths* is negative).

If the :sip:ref:`~PyQt6.QtCore.QDateTime.timeSpec` is :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.LocalTime` or :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.TimeZone` and the resulting date and time fall in the Standard Time to Daylight-Saving Time transition hour then the result will be just beyond this gap, in the direction of change. If the transition is at 2am and the clock goes forward to 3am, the result of aiming between 2am and 3am will be adjusted to fall before 2am (if ``nmonths < 0``) or after 3am (otherwise).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime.daysTo`, :sip:ref:`~PyQt6.QtCore.QDateTime.addDays`, :sip:ref:`~PyQt6.QtCore.QDateTime.addYears`, :sip:ref:`~PyQt6.QtCore.QDateTime.addSecs`, :ref:`qdatetime-timezone-transitions`.
