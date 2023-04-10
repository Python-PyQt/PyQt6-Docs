.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: c91402f3142feeabe18fa476872b6768

Returns the datetime as a number of seconds after the start, in UTC, of the year 1970.

On systems that do not support time zones, this function will behave as if local time were :sip:ref:`~PyQt6.QtCore.Qt.TimeSpec.UTC`.

The behavior for this function is undefined if the datetime stored in this object is not valid. However, for all valid dates, this function returns a unique value.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime.toMSecsSinceEpoch`, :sip:ref:`~PyQt6.QtCore.QDateTime.fromSecsSinceEpoch`, :sip:ref:`~PyQt6.QtCore.QDateTime.setSecsSinceEpoch`.
