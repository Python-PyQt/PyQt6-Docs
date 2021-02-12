.. sip:class-description::
    :status: todo
    :brief: Date functions
    :digest: 5dacc605bdd33182032098bfe713e42f

The :sip:ref:`~PyQt6.QtCore.QDate` class provides date functions.

A :sip:ref:`~PyQt6.QtCore.QDate` object represents a particular day, regardless of calendar, locale or other settings used when creating it or supplied by the system. It can report the year, month and day of the month that represent the day with respect to the proleptic Gregorian calendar or any calendar supplied as a :sip:ref:`~PyQt6.QtCore.QCalendar` object. :sip:ref:`~PyQt6.QtCore.QDate` objects should be passed by value rather than by reference to const; they simply package ``qint64``.

A :sip:ref:`~PyQt6.QtCore.QDate` object is typically created by giving the year, month, and day numbers explicitly. Note that :sip:ref:`~PyQt6.QtCore.QDate` interprets year numbers less than 100 as presented, i.e., as years 1 through 99, without adding any offset. The static function :sip:ref:`~PyQt6.QtCore.QDate.currentDate` creates a :sip:ref:`~PyQt6.QtCore.QDate` object containing the date read from the system clock. An explicit date can also be set using :sip:ref:`~PyQt6.QtCore.QDate.setDate`. The :sip:ref:`~PyQt6.QtCore.QDate.fromString` function returns a :sip:ref:`~PyQt6.QtCore.QDate` given a string and a date format which is used to interpret the date within the string.

The :sip:ref:`~PyQt6.QtCore.QDate.year`, :sip:ref:`~PyQt6.QtCore.QDate.month`, and :sip:ref:`~PyQt6.QtCore.QDate.day` functions provide access to the year, month, and day numbers. When more than one of these values is needed, it is more efficient to call :sip:ref:`~PyQt6.QtCore.QCalendar.partsFromDate`, to save repeating (potentially expensive) calendrical calculations.

Also, :sip:ref:`~PyQt6.QtCore.QDate.dayOfWeek` and :sip:ref:`~PyQt6.QtCore.QDate.dayOfYear` functions are provided. The same information is provided in textual format by :sip:ref:`~PyQt6.QtCore.QDate.toString`. :sip:ref:`~PyQt6.QtCore.QLocale` can map the day numbers to names, :sip:ref:`~PyQt6.QtCore.QCalendar` can map month numbers to names.

:sip:ref:`~PyQt6.QtCore.QDate` provides a full set of operators to compare two :sip:ref:`~PyQt6.QtCore.QDate` objects where smaller means earlier, and larger means later.

You can increment (or decrement) a date by a given number of days using :sip:ref:`~PyQt6.QtCore.QDate.addDays`. Similarly you can use :sip:ref:`~PyQt6.QtCore.QDate.addMonths` and :sip:ref:`~PyQt6.QtCore.QDate.addYears`. The :sip:ref:`~PyQt6.QtCore.QDate.daysTo` function returns the number of days between two dates.

The :sip:ref:`~PyQt6.QtCore.QDate.daysInMonth` and :sip:ref:`~PyQt6.QtCore.QDate.daysInYear` functions return how many days there are in this date's month and year, respectively. The :sip:ref:`~PyQt6.QtCore.QDate.isLeapYear` function indicates whether a date is in a leap year. :sip:ref:`~PyQt6.QtCore.QCalendar` can also supply this information, in some cases more conveniently.

.. _qdate-remarks:

Remarks
-------

**Note:** All conversion to and from string formats is done using the C locale. For localized conversions, see :sip:ref:`~PyQt6.QtCore.QLocale`.

In the Gregorian calendar, there is no year 0. Dates in that year are considered invalid. The year -1 is the year "1 before Christ" or "1 before common era." The day before 1 January 1 CE, :sip:ref:`~PyQt6.QtCore.QDate`\ (1, 1, 1), is 31 December 1 BCE, :sip:ref:`~PyQt6.QtCore.QDate`\ (-1, 12, 31). Various other calendars behave similarly; see :sip:ref:`~PyQt6.QtCore.QCalendar.hasYearZero`.

.. _qdate-range-of-valid-dates:

Range of Valid Dates
....................

Dates are stored internally as a Julian Day number, an integer count of every day in a contiguous range, with 24 November 4714 BCE in the Gregorian calendar being Julian Day 0 (1 January 4713 BCE in the Julian calendar). As well as being an efficient and accurate way of storing an absolute date, it is suitable for converting a date into other calendar systems such as Hebrew, Islamic or Chinese. The Julian Day number can be obtained using :sip:ref:`~PyQt6.QtCore.QDate.toJulianDay` and can be set using :sip:ref:`~PyQt6.QtCore.QDate.fromJulianDay`.

The range of Julian Day numbers that :sip:ref:`~PyQt6.QtCore.QDate` can represent is, for technical reasons, limited to between -784350574879 and 784354017364, which means from before 2 billion BCE to after 2 billion CE. This is more than seven times as wide as the range of dates a :sip:ref:`~PyQt6.QtCore.QDateTime` can represent.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTime`, :sip:ref:`~PyQt6.QtCore.QDateTime`, :sip:ref:`~PyQt6.QtCore.QCalendar`, :sip:ref:`~PyQt6.QtCore.QDateTime.YearRange`.
