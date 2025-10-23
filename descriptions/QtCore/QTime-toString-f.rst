.. sip:method-description::
    :status: todo
    :pysig: 5329e60a1199da82aaf4002273cdd0e3
    :realsig: (Qt::DateFormat) const
    :digest: eb9de1a06fef09ecd293dfc09a858406

Returns the time as a string. The *format* parameter determines the format of the string.

If *format* is :sip:ref:`~PyQt6.QtCore.Qt.DateFormat.TextDate`, the string format is HH:mm:ss; e.g. 1 second before midnight would be "23:59:59".

If *format* is :sip:ref:`~PyQt6.QtCore.Qt.DateFormat.ISODate`, the string format corresponds to the ISO 8601 extended specification for representations of dates, represented by HH:mm:ss. To include milliseconds in the ISO 8601 date, use the *format* :sip:ref:`~PyQt6.QtCore.Qt.DateFormat.ISODateWithMs`, which corresponds to HH:mm:ss.zzz.

If the *format* is :sip:ref:`~PyQt6.QtCore.Qt.DateFormat.RFC2822Date`, the string is formatted in an RFC 2822 compatible way. An example of this formatting is "23:59:20".

If the time is invalid, an empty string will be returned.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTime.fromString`, :sip:ref:`~PyQt6.QtCore.QDate.toString`, :sip:ref:`~PyQt6.QtCore.QDateTime.toString`, :sip:ref:`~PyQt6.QtCore.QLocale.toString`.
