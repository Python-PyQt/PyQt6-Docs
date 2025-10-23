.. sip:method-description::
    :status: todo
    :pysig: 38ae5154b09fef91af6725d15ceaa6dc
    :realsig: (qint64,Qt::TimeSpec,int)
    :digest: 6961039d201e57f3d0b8265988117bd2

Pass a :sip:ref:`~PyQt6.QtCore.QTimeZone` instead, or omit *spec* and *offsetSeconds*.

Returns a datetime representing a moment the given number *msecs* of milliseconds after the start, in UTC, of the year 1970, described as specified by *spec* and *offsetSeconds*.

Note that there are possible values for *msecs* that lie outside the valid range of :sip:ref:`~PyQt6.QtCore.QDateTime`, both negative and positive. The behavior of this function is undefined for those values.

If the *spec* is not :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.OffsetFromUTC` then the *offsetSeconds* will be ignored. If the *spec* is :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.OffsetFromUTC` and the *offsetSeconds* is 0 then :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.UTC` will be used as the *spec*, since UTC has zero offset.

If *spec* is :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.TimeZone` then :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.LocalTime` will be used in its place, equivalent to using the current system time zone (but differently represented).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime.fromSecsSinceEpoch`, :sip:ref:`~PyQt6.QtCore.QDateTime.toMSecsSinceEpoch`, :sip:ref:`~PyQt6.QtCore.QDateTime.setMSecsSinceEpoch`.
