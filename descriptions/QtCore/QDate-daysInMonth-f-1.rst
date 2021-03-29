.. sip:method-description::
    :status: todo
    :pysig: e5ecd4d2152c1f95e7126e45c8b15392
    :realsig: (QCalendar) const
    :digest: b8c018e4f0b41c1d32a35db7eb8c0bfc

Returns the number of days in the month for this date.

Uses *cal* as calendar if supplied, else the Gregorian calendar (for which the result ranges from 28 to 31). Returns 0 if the date is invalid.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDate.day`, :sip:ref:`~PyQt6.QtCore.QDate.daysInYear`, :sip:ref:`~PyQt6.QtCore.QCalendar.daysInMonth`, :sip:ref:`~PyQt6.QtCore.QCalendar.maximumDaysInMonth`, :sip:ref:`~PyQt6.QtCore.QCalendar.minimumDaysInMonth`.
