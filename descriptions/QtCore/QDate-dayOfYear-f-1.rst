.. sip:method-description::
    :status: todo
    :pysig: e5ecd4d2152c1f95e7126e45c8b15392
    :realsig: (QCalendar) const
    :digest: 2e531d957b84412929590ab2994aff51

Returns the day of the year (1 for the first day) for this date.

Uses *cal* as calendar if supplied, else the Gregorian calendar. Returns 0 if either the date or the first day of its year is invalid.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDate.day`, :sip:ref:`~PyQt6.QtCore.QDate.dayOfWeek`, :sip:ref:`~PyQt6.QtCore.QCalendar.daysInYear`.
