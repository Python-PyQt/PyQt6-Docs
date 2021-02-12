.. sip:method-description::
    :status: todo
    :pysig: 883579c2ad1a92ea9bbe04c13915d560
    :realsig: (int,int,int)
    :digest: 552c2dfdcf18cae0636b8ab3f7268e4b

Constructs a date with year *y*, month *m* and day *d*.

The date is understood in terms of the Gregorian calendar. If the specified date is invalid, the date is not set and :sip:ref:`~PyQt6.QtCore.QDate.isValid` returns ``false``.

**Warning:** Years 1 to 99 are interpreted as is. Year 0 is invalid.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDate.isValid`, :sip:ref:`~PyQt6.QtCore.QCalendar.dateFromParts`.
