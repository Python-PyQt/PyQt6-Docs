.. sip:method-description::
    :status: todo
    :pysig: 6e5c186d1b81a246f8e7172abfcae394
    :realsig: (int,int,int,QCalendar)
    :digest: de61e445efa8ec0eda3f7f97567a042a

Sets this to represent the date, in the given calendar *cal*, with the given *year*, *month* and *day* numbers. Returns true if the resulting date is valid, otherwise it sets this to represent an invalid date and returns false.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDate.isValid`, :sip:ref:`~PyQt6.QtCore.QCalendar.dateFromParts`.
