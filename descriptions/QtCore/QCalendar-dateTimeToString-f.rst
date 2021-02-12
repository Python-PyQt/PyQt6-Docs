.. sip:method-description::
    :status: todo
    :pysig: c821ffe073a708db15396ae57560c3a2
    :realsig: (QStringView,const QDateTime&,QDate,QTime,const QLocale&) const
    :digest: d361a0aeec50c9f5836997e4b2d2e1a8

Returns a string representing a given date, time or date-time.

If *datetime* is valid, it is represented and format specifiers for both date and time fields are recognized; otherwise, if *dateOnly* is valid, it is represented and only format specifiers for date fields are recognized; finally, if *timeOnly* is valid, it is represented and only format specifiers for time fields are recognized. If none of these is valid, an empty string is returned.

See :sip:ref:`~PyQt6.QtCore.QDate.toString` and :sip:ref:`~PyQt6.QtCore.QTime.toString` for the supported field specifiers. Characters in *format* that are recognized as field specifiers are replaced by text representing appropriate data from the date and/or time being represented. The texts to represent them may depend on the *locale* specified. Other charagers in *format* are copied verbatim into the returned string.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCalendar.monthName`, :sip:ref:`~PyQt6.QtCore.QCalendar.weekDayName`, :sip:ref:`~PyQt6.QtCore.QDate.toString`, :sip:ref:`~PyQt6.QtCore.QTime.toString`.
