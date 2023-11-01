.. sip:method-description::
    :status: todo
    :pysig: 7196d5afe7051c0b69382f21afc5470d
    :realsig: (qint64,qint64,Qt::TimerType)
    :digest: 675d7da1a63953667d0b6d92305b3001

Sets the remaining time for this :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` object to *secs* seconds plus *nsecs* nanoseconds from now, if *secs* has a positive value. If *secs* is negative, this :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` will be set it to never expire (this behavior does not apply to *nsecs*). If both parameters are zero, this :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` will be marked as expired.

For optimization purposes, if both *secs* and *nsecs* are zero, this function may skip obtaining the current time and may instead use a value known to be in the past. If that happens, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.deadline` may return an unexpected value and this object cannot be used in calculation of how long it is overdue. If that functionality is required, use :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.current` and add time to it.

The timer type for this :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` object will be set to the specified *timerType*.

**Note:** Prior to Qt 6.6, the only condition that caused the timer to never expire was when *secs* was -1.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.setRemainingTime`, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.hasExpired`, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.isForever`, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.remainingTime`.
