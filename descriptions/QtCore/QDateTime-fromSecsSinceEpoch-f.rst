.. sip:method-description::
    :status: todo
    :pysig: 38b67f4848c5ac5a7ef890559f14d475
    :realsig: (qint64,const QTimeZone&)
    :digest: 452742f818ed4efd5f29383e12119a65

This is an overloaded function.

Returns a datetime representing a moment the given number *secs* of seconds after the start, in UTC, of the year 1970, described as specified by *timeZone*. The default time representation is local time.

Note that there are possible values for *secs* that lie outside the valid range of :sip:ref:`~PyQt6.QtCore.QDateTime`, both negative and positive. The behavior of this function is undefined for those values.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime.fromMSecsSinceEpoch`, :sip:ref:`~PyQt6.QtCore.QDateTime.toSecsSinceEpoch`, :sip:ref:`~PyQt6.QtCore.QDateTime.setSecsSinceEpoch`.
