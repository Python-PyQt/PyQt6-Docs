.. sip:method-description::
    :status: todo
    :pysig: e48a49a16893a71bf9b5b2a1de49f66f
    :realsig: (QDate) const
    :digest: aad801bc4d41e49b506b50e127378e36

Returns the day of the week number for the given *date*.

Returns zero if the calendar is unable to represent the indicated date. Returns 1 for Monday through 7 for Sunday. Calendars with intercallary days may use other numbers to represent these.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCalendar.partsFromDate`, :sip:ref:`~PyQt6.QtCore.Qt.DayOfWeek`.
