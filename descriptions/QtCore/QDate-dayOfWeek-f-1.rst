.. sip:method-description::
    :status: todo
    :pysig: e5ecd4d2152c1f95e7126e45c8b15392
    :realsig: (QCalendar) const
    :digest: bf3cdaa51550bf4352a0cfa4bde69c8a

Returns the weekday (1 = Monday to 7 = Sunday) for this date.

Uses *cal* as calendar if supplied, else the Gregorian calendar. Returns 0 if the date is invalid. Some calendars may give special meaning (e.g. intercallary days) to values greater than 7.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDate.day`, :sip:ref:`~PyQt6.QtCore.QDate.dayOfYear`, :sip:ref:`~PyQt6.QtCore.QCalendar.dayOfWeek`, :sip:ref:`~PyQt6.QtCore.Qt.DayOfWeek`.
