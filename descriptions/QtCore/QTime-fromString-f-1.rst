.. sip:method-description::
    :status: todo
    :pysig: 1e9a089946d5d1b8f9a6da6cb357ceb0
    :realsig: (const QString&,const QString&)
    :digest: 7d3c3d6fb08fb0ab4497ee6d86abf38d

Returns the :sip:ref:`~PyQt6.QtCore.QTime` represented by the *string*, using the *format* given, or an invalid time if the string cannot be parsed.

These expressions may be used for the format:

+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Expression             | Output                                                                                                                                                                                                    |
+========================+===========================================================================================================================================================================================================+
| h                      | The hour without a leading zero (0 to 23 or 1 to 12 if AM/PM display)                                                                                                                                     |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| hh                     | The hour with a leading zero (00 to 23 or 01 to 12 if AM/PM display)                                                                                                                                      |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| H                      | The hour without a leading zero (0 to 23, even with AM/PM display)                                                                                                                                        |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| HH                     | The hour with a leading zero (00 to 23, even with AM/PM display)                                                                                                                                          |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| m                      | The minute without a leading zero (0 to 59)                                                                                                                                                               |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| mm                     | The minute with a leading zero (00 to 59)                                                                                                                                                                 |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| s                      | The whole second, without any leading zero (0 to 59)                                                                                                                                                      |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ss                     | The whole second, with a leading zero where applicable (00 to 59)                                                                                                                                         |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| z                      | The fractional part of the second, to go after a decimal point, without trailing zeroes (0 to 999). Thus "``s.z``" reports the seconds to full available (millisecond) precision without trailing zeroes. |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| zzz                    | The fractional part of the second, to millisecond precision, including trailing zeroes where applicable (000 to 999).                                                                                     |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| AP, A, ap, a, aP or Ap | Either 'AM' indicating a time before 12:00 or 'PM' for later times, matched case-insensitively.                                                                                                           |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

All other input characters will be treated as text. Any non-empty sequence of characters enclosed in single quotes will also be treated (stripped of the quotes) as text and not be interpreted as expressions.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_time_qdatetime.py
    :lines: 101-102

If the format is not satisfied, an invalid :sip:ref:`~PyQt6.QtCore.QTime` is returned. Expressions that do not expect leading zeroes to be given (h, m, s and z) are greedy. This means that they will use two digits (or three, for z) even if this puts them outside the range of accepted values and leaves too few digits for other sections. For example, the following string could have meant 00:07:10, but the m will grab two digits, resulting in an invalid time:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_time_qdatetime.py
    :lines: 107-107

Any field that is not represented in the format will be set to zero. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_time_qdatetime.py
    :lines: 112-113

**Note:** If localized forms of am or pm (the AP, ap, Ap, aP, A or a formats) are to be recognized, use :sip:ref:`~PyQt6.QtCore.QLocale.system`.toTime().

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTime.toString`, :sip:ref:`~PyQt6.QtCore.QDateTime.fromString`, :sip:ref:`~PyQt6.QtCore.QDate.fromString`, :sip:ref:`~PyQt6.QtCore.QLocale.toTime`, :sip:ref:`~PyQt6.QtCore.QLocale.toDateTime`.
