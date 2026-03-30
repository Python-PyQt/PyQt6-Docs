.. sip:method-description::
    :status: todo
    :pysig: 701e3b3003ec0691dbea36dc1558e3e5
    :realsig: (const QDateTime&) const
    :digest: 43d7e217d261f06758b2c35eef14601e

Returns the number of milliseconds from this datetime to the *other* datetime. If the *other* datetime is earlier than this datetime, the value returned is negative.

Before performing the comparison, the two datetimes are converted to :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.UTC` to ensure that the result is correct if daylight-saving (DST) applies to one of the two datetimes and but not the other.

Returns 0 if either datetime is invalid.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime.addMSecs`, :sip:ref:`~PyQt6.QtCore.QDateTime.daysTo`, :sip:ref:`~PyQt6.QtCore.QTime.msecsTo`.
