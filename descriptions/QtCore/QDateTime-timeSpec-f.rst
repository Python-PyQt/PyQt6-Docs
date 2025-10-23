.. sip:method-description::
    :status: todo
    :pysig: 41145246d08568577980f08c1fee338e
    :realsig: () const
    :digest: 5dbffa747ea5b09d0e924c6831a83203

Returns the time specification of the datetime.

This classifies its time representation as local time, UTC, a fixed offset from UTC (without indicating the offset) or a time zone (without giving the details of that time zone). Equivalent to ``timeRepresentation().timeSpec()``.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDateTime.setTimeSpec`, :sip:ref:`~PyQt6.QtCore.QDateTime.setTimeZone`, :sip:ref:`~PyQt6.QtCore.QDateTime.timeRepresentation`, :sip:ref:`~PyQt6.QtCore.QDateTime.date`, :sip:ref:`~PyQt6.QtCore.QDateTime.time`.
