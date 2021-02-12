.. sip:method-description::
    :status: todo
    :pysig: 0ec537fe6f9ba105f044cfe06a333dc1
    :realsig: (int,QCalendar) const
    :digest: 1804a7bb4b80a4a2c7c126f601852817

Returns a :sip:ref:`~PyQt6.QtCore.QDate` object containing a date *nyears* later than the date of this object (or earlier if *nyears* is negative).

Uses *cal* as calendar, if supplied, else the Gregorian calendar.

**Note:** If the ending day/month combination does not exist in the resulting year (e.g., for the Gregorian calendar, if the date was Feb 29 and the final year is not a leap year), this function will return a date that is the latest valid date in the given month (in the example, Feb 28).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDate.addDays`, :sip:ref:`~PyQt6.QtCore.QDate.addMonths`.
