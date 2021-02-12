.. sip:method-description::
    :status: todo
    :pysig: e5ecd4d2152c1f95e7126e45c8b15392
    :realsig: (QCalendar) const
    :digest: 1f9407c92f7c91da75fcc796ec78673d

Returns the day of the month for this date.

Uses *cal* as calendar if supplied, else the Gregorian calendar (for which the return ranges from 1 to 31). Returns 0 if the date is invalid.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDate.year`, :sip:ref:`~PyQt6.QtCore.QDate.month`, :sip:ref:`~PyQt6.QtCore.QDate.dayOfWeek`, :sip:ref:`~PyQt6.QtCore.QCalendar.partsFromDate`.
