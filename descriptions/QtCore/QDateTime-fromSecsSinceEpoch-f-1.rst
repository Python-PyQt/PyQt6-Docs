.. sip:method-description::
    :status: todo
    :pysig: 38ae5154b09fef91af6725d15ceaa6dc
    :realsig: (qint64,Qt::TimeSpec,int)
    :digest: 90347e383c1a782820b241c10458fe5f

Returns a datetime whose date and time are the number of seconds *secs* that have passed since 1970-01-01T00:00:00.000, Coordinated Universal Time (\ :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.UTC`) and converted to the given *spec*.

Note that there are possible values for *secs* that lie outside the valid range of :sip:ref:`~PyQt6.QtCore.QDateTime`, both negative and positive. The behavior of this function is undefined for those values.

If the *spec* is not :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.OffsetFromUTC` then the *offsetSeconds* will be ignored. If the *spec* is :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.OffsetFromUTC` and the *offsetSeconds* is 0 then the spec will be set to :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.UTC`, i.e. an offset of 0 seconds.

If *spec* is :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.TimeZone` then the spec will be set to :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.LocalTime`, i.e. the current system time zone.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime.toSecsSinceEpoch`, :sip:ref:`~PyQt6.QtCore.QDateTime.setSecsSinceEpoch`.
