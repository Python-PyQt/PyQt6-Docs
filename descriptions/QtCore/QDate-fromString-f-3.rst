.. sip:method-description::
    :status: todo
    :pysig: 8d10cb57a598dd5f04f160c8303f7cac
    :realsig: (const QString&, const QString&, QCalendar)
    :digest: 2b7e7aa8f9b90de72f9f0ad74e2689f6

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

+-------+---------------+
| Field | Default value |
+=======+===============+
| Year  | 1900          |
+-------+---------------+
| Month | 1 (January)   |
+-------+---------------+
| Day   | 1             |
+-------+---------------+

The following examples demonstrate the default values:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_time_qdatetime.py
    :lines: 73-75

**Note:** If a format character is repeated more times than the longest expression in the table above using it, this part of the format will be read as several expressions with no separator between them; the longest above, possibly repeated as many times as there are copies of it, ending with a residue that may be a shorter expression. Thus ``'MMMMMMMMMM'`` would match ``"MayMay05"`` and set the month to May. Likewise, ``'MMMMMM'`` would match ``"May08"`` and find it inconsistent, leading to an invalid date.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDate.toString`, :sip:ref:`~PyQt6.QtCore.QDateTime.fromString`, :sip:ref:`~PyQt6.QtCore.QTime.fromString`, :sip:ref:`~PyQt6.QtCore.QLocale.toDate`.
