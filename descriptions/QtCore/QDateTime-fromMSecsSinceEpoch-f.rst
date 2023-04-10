.. sip:method-description::
    :status: todo
    :pysig: 38b67f4848c5ac5a7ef890559f14d475
    :realsig: (qint64,const QTimeZone&)
    :digest: 3aa1c632d651ffd09f431e8b466b71ba

This is an overloaded function.

Returns a datetime representing a moment the given number *msecs* of milliseconds after the start, in UTC, of the year 1970, described as specified by *timeZone*. The default time representation is local time.

Note that there are possible values for *msecs* that lie outside the valid range of :sip:ref:`~PyQt6.QtCore.QDateTime`, both negative and positive. The behavior of this function is undefined for those values.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime.fromSecsSinceEpoch`, :sip:ref:`~PyQt6.QtCore.QDateTime.toMSecsSinceEpoch`, :sip:ref:`~PyQt6.QtCore.QDateTime.setMSecsSinceEpoch`.
