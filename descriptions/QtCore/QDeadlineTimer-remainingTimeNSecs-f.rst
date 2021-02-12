.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 99df80d68ddebdf1464c5d230fcdd245

Returns the remaining time in this :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` object in nanoseconds. If the timer has already expired, this function will return zero and it is not possible to obtain the amount of time overdue with this function. If the timer was set to never expire, this function returns -1.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.remainingTime`, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.isForever`, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.hasExpired`.
