.. sip:method-description::
    :status: todo
    :pysig: 9edf5b3d30cf0afe089ca09990919fd0
    :realsig: (const QString&, const QString&, int, QCalendar)
    :digest: 5c8bdf7854dc9f5240a5ddcc75fe0a67

Returns the :sip:ref:`~PyQt6.QtCore.QDateTime` represented by the *string*, using the *format* given, or an invalid datetime if the string cannot be parsed.

Uses the calendar *cal* if supplied, else Gregorian.

When *format* only specifies the last two digits of a year, the 100 years starting at *baseYear* are the candidates first considered. Prior to 6.7 there was no *baseYear* parameter and 1900 was always used. This is the default for *baseYear*, selecting a year from then to 1999. In some cases, other fields may lead to the next or previous century being selected, to get a result consistent with all fields given. See :sip:ref:`~PyQt6.QtCore.QDate.fromString` for details.

In addition to the expressions, recognized in the format string to represent parts of the date and time, by :sip:ref:`~PyQt6.QtCore.QDate.fromString` and :sip:ref:`~PyQt6.QtCore.QTime.fromString`, this method supports:

+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Expression | Output                                                                                                                                                                       |
+============+==============================================================================================================================================================================+
| t          | the timezone (offset, name, "Z" or offset with "UTC" prefix)                                                                                                                 |
+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| tt         | the timezone in offset format with no colon between hours and minutes (for example "+0200")                                                                                  |
+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ttt        | the timezone in offset format with a colon between hours and minutes (for example "+02:00")                                                                                  |
+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| tttt       | the timezone name (for example "Europe/Berlin"). The name recognized are those known to :sip:ref:`~PyQt6.QtCore.QTimeZone`, which may depend on the operating system in use. |
+------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

If no 't' format specifier is present, the system's local time-zone is used. For the defaults of all other fields, see :sip:ref:`~PyQt6.QtCore.QDate.fromString` and :sip:ref:`~PyQt6.QtCore.QTime.fromString`.

For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_time_qdatetime.py
    :lines: 156-159

All other input characters will be treated as text. Any non-empty sequence of characters enclosed in single quotes will also be treated (stripped of the quotes) as text and not be interpreted as expressions.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_time_qdatetime.py
    :lines: 139-146

If the format is not satisfied, an invalid :sip:ref:`~PyQt6.QtCore.QDateTime` is returned. If the format is satisfied but *string* represents an invalid datetime (e.g. in a gap skipped by a time-zone transition), an valid :sip:ref:`~PyQt6.QtCore.QDateTime` is returned, that represents a near-by datetime that is valid.

The expressions that don't have leading zeroes (d, M, h, m, s, z) will be greedy. This means that they will use two digits (or three, for z) even if this will put them outside the range and/or leave too few digits for other sections.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_time_qdatetime.py
    :lines: 151-151

This could have meant 1 January 00:30.00 but the M will grab two digits.

Incorrectly specified fields of the *string* will cause an invalid :sip:ref:`~PyQt6.QtCore.QDateTime` to be returned. Only datetimes between the local time start of year 100 and end of year 9999 are supported. Note that datetimes near the ends of this range in other time-zones, notably including UTC, may fall outside the range (and thus be treated as invalid) depending on local time zone.

**Note:** Day and month names as well as AM/PM indicators must be given in English (C locale). If localized month and day names or localized forms of AM/PM are to be recognized, use :sip:ref:`~PyQt6.QtCore.QLocale.system`.toDateTime().

**Note:** If a format character is repeated more times than the longest expression in the table above using it, this part of the format will be read as several expressions with no separator between them; the longest above, possibly repeated as many times as there are copies of it, ending with a residue that may be a shorter expression. Thus ``'tttttt'`` would match ``"Europe/BerlinEurope/Berlin"`` and set the zone to Berlin time; if the datetime string contained "Europe/BerlinZ" it would "match" but produce an inconsistent result, leading to an invalid datetime.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime.toString`, :sip:ref:`~PyQt6.QtCore.QDate.fromString`, :sip:ref:`~PyQt6.QtCore.QTime.fromString`, :sip:ref:`~PyQt6.QtCore.QLocale.toDateTime`.
