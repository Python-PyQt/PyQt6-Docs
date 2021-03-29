.. sip:method-description::
    :status: todo
    :pysig: e93f2860b26a60bc1405b55c3061b147
    :realsig: (qint64,Qt::TimerType)
    :digest: 55a5d2ea27d8f743e765657cb0823836

Constructs a :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` object with an expiry time of *msecs* msecs from the moment of the creation of this object, if msecs is positive. If *msecs* is zero, this :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` will be marked as expired, causing :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.remainingTime` to return zero and :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.deadline` to return an indeterminate time point in the past. If *msecs* is -1, the timer will be set to never expire, causing :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.remainingTime` to return -1 and :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.deadline` to return the maximum value.

The :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` object will be constructed with the specified timer *type*.

For optimization purposes, if *msecs* is zero, this function may skip obtaining the current time and may instead use a value known to be in the past. If that happens, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.deadline` may return an unexpected value and this object cannot be used in calculation of how long it is overdue. If that functionality is required, use :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.current` and add time to it.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.hasExpired`, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.isForever`, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.remainingTime`, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.setRemainingTime`.
