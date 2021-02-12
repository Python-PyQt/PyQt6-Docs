.. sip:method-description::
    :status: todo
    :pysig: e5ccfd30f8b9faaf0f78a151784e8354
    :realsig: (int,int,int) const
    :digest: bcb959f4cf62eb62363baafbf2ac9d14

Returns ``true`` precisely if the given *year*, *month*, and *day* specify a valid date in this calendar.

Usually this means 1 <= month <= :sip:ref:`~PyQt6.QtCore.QCalendar.monthsInYear`\ (year) and 1 <= day <= :sip:ref:`~PyQt6.QtCore.QCalendar.daysInMonth`\ (month, year). However, calendars with intercallary days or months may complicate that.
