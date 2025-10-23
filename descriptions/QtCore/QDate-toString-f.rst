.. sip:method-description::
    :status: todo
    :pysig: 5329e60a1199da82aaf4002273cdd0e3
    :realsig: (Qt::DateFormat) const
    :digest: 6841259106a8a18783307a48d44af6ac

Returns the date as a string. The *format* parameter determines the format of the string.

If the *format* is :sip:ref:`~PyQt6.QtCore.Qt.DateFormat.TextDate`, the string is formatted in the default way. The day and month names will be in English. An example of this formatting is "Sat May 20 1995". For localized formatting, see :sip:ref:`~PyQt6.QtCore.QLocale.toString`.

If the *format* is :sip:ref:`~PyQt6.QtCore.Qt.DateFormat.ISODate`, the string format corresponds to the ISO 8601 extended specification for representations of dates and times, taking the form yyyy-MM-dd, where yyyy is the year, MM is the month of the year (between 01 and 12), and dd is the day of the month between 01 and 31.

If the *format* is :sip:ref:`~PyQt6.QtCore.Qt.DateFormat.RFC2822Date`, the string is formatted in an RFC 2822 compatible way. An example of this formatting is "20 May 1995".

If the date is invalid, an empty string will be returned.

**Warning:** The :sip:ref:`~PyQt6.QtCore.Qt.DateFormat.ISODate` format is only valid for years in the range 0 to 9999.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDate.fromString`, :sip:ref:`~PyQt6.QtCore.QLocale.toString`.
