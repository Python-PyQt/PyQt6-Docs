.. sip:method-description::
    :status: todo
    :pysig: e5ecd4d2152c1f95e7126e45c8b15392
    :realsig: (QCalendar) const
    :digest: 6913c8384b18f3ddee5e6dea4e07eb74

Returns the year of this date.

Uses *cal* as calendar, if supplied, else the Gregorian calendar.

Returns 0 if the date is invalid. For some calendars, dates before their first year may all be invalid.

If using a calendar which has a year 0, check using :sip:ref:`~PyQt6.QtCore.QDate.isValid` if the return is 0. Such calendars use negative year numbers in the obvious way, with year 1 preceded by year 0, in turn preceded by year -1 and so on.

Some calendars, despite having no year 0, have a conventional numbering of the years before their first year, counting backwards from 1. For example, in the proleptic Gregorian calendar, successive years before 1 CE (the first year) are identified as 1 BCE, 2 BCE, 3 BCE and so on. For such calendars, negative year numbers are used to indicate these years before year 1, with -1 indicating the year before 1.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDate.month`, :sip:ref:`~PyQt6.QtCore.QDate.day`, :sip:ref:`~PyQt6.QtCore.QCalendar.hasYearZero`, :sip:ref:`~PyQt6.QtCore.QCalendar.isProleptic`, :sip:ref:`~PyQt6.QtCore.QCalendar.partsFromDate`.
