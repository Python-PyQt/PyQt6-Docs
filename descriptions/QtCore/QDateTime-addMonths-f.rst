.. sip:method-description::
    :status: todo
    :pysig: 41249efbb941c4220a2536f4c7898d9d
    :realsig: (int) const
    :digest: cc10745b1b917c135a6c47aa2d2038be

Returns a :sip:ref:`~PyQt6.QtCore.QDateTime` object containing a datetime *nmonths* months later than the datetime of this object (or earlier if *nmonths* is negative).

If the :sip:ref:`~PyQt6.QtCore.QDateTime.timeSpec` is :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.LocalTime` or :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.TimeZone` and the resulting date and time fall in the Standard Time to Daylight-Saving Time transition hour then the result will be adjusted accordingly, i.e. if the transition is at 2am and the clock goes forward to 3am and the result falls between 2am and 3am then the result will be adjusted to fall after 3am.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime.daysTo`, :sip:ref:`~PyQt6.QtCore.QDateTime.addDays`, :sip:ref:`~PyQt6.QtCore.QDateTime.addYears`, :sip:ref:`~PyQt6.QtCore.QDateTime.addSecs`.
