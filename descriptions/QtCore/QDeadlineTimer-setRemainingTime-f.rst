.. sip:method-description::
    :status: todo
    :pysig: e93f2860b26a60bc1405b55c3061b147
    :realsig: (qint64,Qt::TimerType)
    :digest: 563ef96c499b39a57b0248489fb93024

Sets the remaining time for this :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` object to *msecs* milliseconds from now, if *msecs* has a positive value. If *msecs* is zero, this :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` object will be marked as expired, whereas a negative value will set it to never expire.

For optimization purposes, if *msecs* is zero, this function may skip obtaining the current time and may instead use a value known to be in the past. If that happens, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.deadline` may return an unexpected value and this object cannot be used in calculation of how long it is overdue. If that functionality is required, use :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.current` and add time to it.

The timer type for this :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` object will be set to the specified *timerType*.

**Note:** Prior to Qt 6.6, the only value that caused the timer to never expire was -1.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.setPreciseRemainingTime`, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.hasExpired`, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.isForever`, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.remainingTime`.
