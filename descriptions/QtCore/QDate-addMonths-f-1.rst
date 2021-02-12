.. sip:method-description::
    :status: todo
    :pysig: 0ec537fe6f9ba105f044cfe06a333dc1
    :realsig: (int,QCalendar) const
    :digest: b150be0696d8b59e918e9d98545a8607

Returns a :sip:ref:`~PyQt6.QtCore.QDate` object containing a date *nmonths* later than the date of this object (or earlier if *nmonths* is negative).

Uses *cal* as calendar, if supplied, else the Gregorian calendar.

**Note:** If the ending day/month combination does not exist in the resulting month/year, this function will return a date that is the latest valid date in the selected month.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDate.addDays`, :sip:ref:`~PyQt6.QtCore.QDate.addYears`.
