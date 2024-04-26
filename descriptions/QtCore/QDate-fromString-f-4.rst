.. sip:method-description::
    :status: todo
    :pysig: 5df1cbdf5a65ef65c39132fe988780e5
    :realsig: (const QString&, const QString&, int, QCalendar)
    :digest: 92f81f3c085434bee0b95b3d22e36990

Returns the :sip:ref:`~PyQt6.QtCore.QDate` represented by the *string*, using the *format* given, or an invalid date if the string cannot be parsed.

Uses *cal* as calendar if supplied, else the Gregorian calendar. Ranges of values in the format descriptions below are for the latter; they may be different for other calendars.

These expressions may be used for the format:

+------------+-----------------------------------------------------------------------------------------+
| Expression | Output                                                                                  |
+============+=========================================================================================+
| d          | The day as a number without a leading zero (1 to 31)                                    |
+------------+-----------------------------------------------------------------------------------------+
| dd         | The day as a number with a leading zero (01 to 31)                                      |
+------------+-----------------------------------------------------------------------------------------+
| ddd        | The abbreviated day name ('Mon' to 'Sun').                                              |
+------------+-----------------------------------------------------------------------------------------+
| dddd       | The long day name ('Monday' to 'Sunday').                                               |
+------------+-----------------------------------------------------------------------------------------+
| M          | The month as a number without a leading zero (1 to 12)                                  |
+------------+-----------------------------------------------------------------------------------------+
| MM         | The month as a number with a leading zero (01 to 12)                                    |
+------------+-----------------------------------------------------------------------------------------+
| MMM        | The abbreviated month name ('Jan' to 'Dec').                                            |
+------------+-----------------------------------------------------------------------------------------+
| MMMM       | The long month name ('January' to 'December').                                          |
+------------+-----------------------------------------------------------------------------------------+
| yy         | The year as a two digit number (00 to 99)                                               |
+------------+-----------------------------------------------------------------------------------------+
| yyyy       | The year as a four digit number, possibly plus a leading minus sign for negative years. |
+------------+-----------------------------------------------------------------------------------------+

**Note:** Day and month names must be given in English (C locale). If localized month and day names are to be recognized, use :sip:ref:`~PyQt6.QtCore.QLocale.system`.toDate().

All other input characters will be treated as text. Any non-empty sequence of characters enclosed in single quotes will also be treated (stripped of the quotes) as text and not be interpreted as expressions. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_time_qdatetime.py
    :lines: 62-63

If the format is not satisfied, an invalid :sip:ref:`~PyQt6.QtCore.QDate` is returned. The expressions that don't expect leading zeroes (d, M) will be greedy. This means that they will use two digits even if this will put them outside the accepted range of values and leaves too few digits for other sections. For example, the following format string could have meant January 30 but the M will grab two digits, resulting in an invalid date:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_time_qdatetime.py
    :lines: 68-68

For any field that is not represented in the format the following defaults are used:

+-------+----------------------+
| Field | Default value        |
+=======+======================+
| Year  | *baseYear* (or 1900) |
+-------+----------------------+
| Month | 1 (January)          |
+-------+----------------------+
| Day   | 1                    |
+-------+----------------------+

When *format* only specifies the last two digits of a year, the 100 years starting at *baseYear* are the candidates first considered. Prior to 6.7 there was no *baseYear* parameter and 1900 was always used. This is the default for *baseYear*, selecting a year from then to 1999. Passing 1976 as *baseYear* will select a year from 1976 through 2075, for example. When the format also includes month, day (of month) and day-of-week, these suffice to imply the century. In such a case, a matching date is selected in the nearest century to the one indicated by *baseYear*, prefering later over earlier. See :sip:ref:`~PyQt6.QtCore.QCalendar.matchCenturyToWeekday` and Date ambiguities for further details,

The following examples demonstrate the default values:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_time_qdatetime.py
    :lines: 73-75

**Note:** If a format character is repeated more times than the longest expression in the table above using it, this part of the format will be read as several expressions with no separator between them; the longest above, possibly repeated as many times as there are copies of it, ending with a residue that may be a shorter expression. Thus ``'MMMMMMMMMM'`` would match ``"MayMay05"`` and set the month to May. Likewise, ``'MMMMMM'`` would match ``"May08"`` and find it inconsistent, leading to an invalid date.

Date ambiguities
................

Different cultures use different formats for dates and, as a result, users may mix up the order in which date fields should be given. For example, ``"Wed 28-Nov-01"`` might mean either 2028 November 1st or the 28th of November, 2001 (each of which happens to be a Wednesday). Using format ``"ddd yy-MMM-dd"`` it shall be interpreted the first way, using ``"ddd dd-MMM-yy"`` the second. However, which the user meant may depend on the way the user normally writes dates, rather than the format the code was expecting.

The example considered above mixed up day of the month and a two-digit year. Similar confusion can arise over interchanging the month and day of the month, when both are given as numbers. In these cases, including a day of the week field in the date format can provide some redundancy, that may help to catch errors of this kind. However, as in the example above, this is not always effective: the interchange of two fields (or their meanings) may produce dates with the same day of the week.

Including a day of the week in the format can also resolve the century of a date specified using only the last two digits of its year. Unfortunately, when combined with a date in which the user (or other source of data) has mixed up two of the fields, this resolution can lead to finding a date which does match the format's reading but isn't the one intended by its author. Likewise, if the user simply gets the day of the week wrong, in an otherwise correct date, this can lead a date in a different century. In each case, finding a date in a different century can turn a wrongly-input date into a wildly different one.

The best way to avoid date ambiguities is to use four-digit years and months specified by name (whether full or abbreviated), ideally collected via user interface idioms that make abundantly clear to the user which part of the date they are selecting. Including a day of the week can also help by providing the means to check consistency of the data. Where data comes from the user, using a format supplied by a locale selected by the user, it is best to use a long format as short formats are more likely to use two-digit years. Of course, it is not always possible to control the format - data may come from a source you do not control, for example.

As a result of these possible sources of confusion, particularly when you cannot be sure an unambiguous format is in use, it is important to check that the result of reading a string as a date is not just valid but reasonable for the purpose for which it was supplied. If the result is outside some range of reasonable values, it may be worth getting the user to confirm their date selection, showing the date read from the string in a long format that does include month name and four-digit year, to make it easier for them to recognize any errors.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDate.toString`, :sip:ref:`~PyQt6.QtCore.QDateTime.fromString`, :sip:ref:`~PyQt6.QtCore.QTime.fromString`, :sip:ref:`~PyQt6.QtCore.QLocale.toDate`.
