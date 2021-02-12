.. sip:method-description::
    :status: todo
    :pysig: e5ecd4d2152c1f95e7126e45c8b15392
    :realsig: (QCalendar) const
    :digest: 462f82bb000546fd19222683bb9d91e2

Returns the number of days in the year for this date.

Uses *cal* as calendar if supplied, else the Gregorian calendar (for which the result is 365 or 366). Returns 0 if the date is invalid.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDate.day`, :sip:ref:`~PyQt6.QtCore.QDate.daysInMonth`, :sip:ref:`~PyQt6.QtCore.QCalendar.daysInYear`, :sip:ref:`~PyQt6.QtCore.QCalendar.maximumMonthsInYear`.
