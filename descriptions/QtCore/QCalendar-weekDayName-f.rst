.. sip:method-description::
    :status: todo
    :pysig: 11e6f1e212907a6fa349e999a9447a9c
    :realsig: (const QLocale&,int,QLocale::FormatType) const
    :digest: 69d544863b51fe2c18614b80e8d48025

Returns a suitably localised name for a day of the week.

The days of the week are numbered from 1 for Monday through 7 for Sunday. Some calendars may support higher numbers for other days (e.g. intercallary days, that are not part of any week). Returns an empty string if the *day* number is unrecognized.

The name is returned in the form that would normally be used in a full date, in the specified *locale*; the *format* determines how fully it shall be expressed (i.e. to what extent it is abbreviated).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCalendar.standaloneWeekDayName`, :sip:ref:`~PyQt6.QtCore.QCalendar.dayOfWeek`.
