.. sip:method-description::
    :status: todo
    :pysig: 11e6f1e212907a6fa349e999a9447a9c
    :realsig: (const QLocale&,int,QLocale::FormatType) const
    :digest: 0b125565ff66549930e24a81de1f6958

Returns a suitably localised standalone name for a day of the week.

The days of the week are numbered from 1 for Monday through 7 for Sunday. Some calendars may support higher numbers for other days (e.g. intercallary days, that are not part of any week). Returns an empty string if the *day* number is unrecognized.

The name is returned in the form that would be used in isolation (for example as a column heading in a calendar's tabular display of a month with successive weeks as rows) in the specified *locale*; the *format* determines how fully it shall be expressed (i.e. to what extent it is abbreviated).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCalendar.weekDayName`, :sip:ref:`~PyQt6.QtCore.QCalendar.dayOfWeek`.
