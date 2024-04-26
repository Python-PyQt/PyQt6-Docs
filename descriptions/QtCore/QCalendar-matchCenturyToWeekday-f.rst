.. sip:method-description::
    :status: todo
    :pysig: 360b6a8186c469249ab2a0d2db534da9
    :realsig: (const QCalendar::YearMonthDay&, int) const
    :digest: 39aa7af667d01a2d8a02db0b937a0713

Adjusts the century of a date to match a given day of the week.

For use when given a date's day of week, day of month, month and last two digits of the year. Returns a :sip:ref:`~PyQt6.QtCore.QDate` instance with the given *dow* as its :sip:ref:`~PyQt6.QtCore.QDate.dayOfWeek`, matching the given *parts* in month and day of the month. The returned :sip:ref:`~PyQt6.QtCore.QDate`'s :sip:ref:`~PyQt6.QtCore.QDate.year` shall differ from ``parts.year`` by a multiple of 100, preferring small multiples over larger and positive multiples over their negations.

If no date matches these conditions, an invalid :sip:ref:`~PyQt6.QtCore.QDate` is returned: the day of week is incompatible with the other data given. This arises, for example, with the Gregorian calendar, whose 400-year cycle is a whole number of weeks long, so any given month and day of that month only ever falls, in years with a given last two digits, on four days of the week. (In the special case of February 29th at the turn of a century, when that is a leap year, only one day of the week is possible: Tuesday.)
