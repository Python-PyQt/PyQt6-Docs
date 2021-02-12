.. sip:method-description::
    :status: todo
    :pysig: 883579c2ad1a92ea9bbe04c13915d560
    :realsig: (int*,int*,int*) const
    :digest: 697f1c4d9b204d4d78bebc045471e24b

Extracts the date's year, month, and day, and assigns them to \*\ *year*, \*\ *month*, and \*\ *day*. The pointers may be null.

Returns 0 if the date is invalid.

**Note:** In Qt versions prior to 5.7, this function is marked as non-``const``.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDate.year`, :sip:ref:`~PyQt6.QtCore.QDate.month`, :sip:ref:`~PyQt6.QtCore.QDate.day`, :sip:ref:`~PyQt6.QtCore.QDate.isValid`, :sip:ref:`~PyQt6.QtCore.QCalendar.partsFromDate`.
