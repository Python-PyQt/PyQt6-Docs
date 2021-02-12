.. sip:method-description::
    :status: todo
    :pysig: 5329e60a1199da82aaf4002273cdd0e3
    :realsig: (Qt::DateFormat) const
    :digest: 1f8ed0dc134a691f3e3e1d8ece5b08fd

This is an overloaded function.

Returns the datetime as a string in the *format* given.

If the *format* is :sip:ref:`~PyQt6.QtCore.Qt.DateFormat.TextDate`, the string is formatted in the default way. The day and month names will be in English. An example of this formatting is "Wed May 20 03:40:13 1998". For localized formatting, see :sip:ref:`~PyQt6.QtCore.QLocale.toString`.

If the *format* is :sip:ref:`~PyQt6.QtCore.Qt.DateFormat.ISODate`, the string format corresponds to the ISO 8601 extended specification for representations of dates and times, taking the form yyyy-MM-ddTHH:mm:ss[Z|[+|-]HH:mm], depending on the :sip:ref:`~PyQt6.QtCore.QDateTime.timeSpec` of the :sip:ref:`~PyQt6.QtCore.QDateTime`. If the :sip:ref:`~PyQt6.QtCore.QDateTime.timeSpec` is :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.UTC`, Z will be appended to the string; if the :sip:ref:`~PyQt6.QtCore.QDateTime.timeSpec` is :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.OffsetFromUTC`, the offset in hours and minutes from UTC will be appended to the string. To include milliseconds in the ISO 8601 date, use the *format* :sip:ref:`~PyQt6.QtCore.Qt.DateFormat.ISODateWithMs`, which corresponds to yyyy-MM-ddTHH:mm:ss.zzz[Z|[+|-]HH:mm].

If the *format* is :sip:ref:`~PyQt6.QtCore.Qt.DateFormat.RFC2822Date`, the string is formatted following RFC 2822.

If the datetime is invalid, an empty string will be returned.

**Warning:** The :sip:ref:`~PyQt6.QtCore.Qt.DateFormat.ISODate` format is only valid for years in the range 0 to 9999.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime.fromString`, :sip:ref:`~PyQt6.QtCore.QDate.toString`, :sip:ref:`~PyQt6.QtCore.QTime.toString`, :sip:ref:`~PyQt6.QtCore.QLocale.toString`.
