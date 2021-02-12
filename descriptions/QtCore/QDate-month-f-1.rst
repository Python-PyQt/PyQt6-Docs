.. sip:method-description::
    :status: todo
    :pysig: e5ecd4d2152c1f95e7126e45c8b15392
    :realsig: (QCalendar) const
    :digest: c184c2297672a5db2dad7fde49f0804f

Returns the month-number for the date.

Numbers the months of the year starting with 1 for the first. Uses *cal* as calendar if supplied, else the Gregorian calendar, for which the month numbering is as follows:

* 1 = "January"

* 2 = "February"

* 3 = "March"

* 4 = "April"

* 5 = "May"

* 6 = "June"

* 7 = "July"

* 8 = "August"

* 9 = "September"

* 10 = "October"

* 11 = "November"

* 12 = "December"

Returns 0 if the date is invalid. Note that some calendars may have more than 12 months in some years.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDate.year`, :sip:ref:`~PyQt6.QtCore.QDate.day`, :sip:ref:`~PyQt6.QtCore.QCalendar.partsFromDate`.
