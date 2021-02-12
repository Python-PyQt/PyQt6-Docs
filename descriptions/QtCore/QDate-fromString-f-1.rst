.. sip:method-description::
    :status: todo
    :pysig: 7c9f37a0015cd9683f9bd3de0975f230
    :realsig: (const QString&,const QString&,QCalendar)
    :digest: ebf43133a27b5f243dc965ac0edc4f0a

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

**Note:** Day and month names must be given in English (C locale). If localized month and day names are used, use :sip:ref:`~PyQt6.QtCore.QLocale.system`.toDate().

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

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDate.toString`, :sip:ref:`~PyQt6.QtCore.QDateTime.fromString`, :sip:ref:`~PyQt6.QtCore.QTime.fromString`, :sip:ref:`~PyQt6.QtCore.QLocale.toDate`.
