.. sip:method-description::
    :status: todo
    :pysig: 7196d5afe7051c0b69382f21afc5470d
    :realsig: (qint64,qint64,Qt::TimerType)
    :digest: 90d57d3fb35ee9f8cac6c10c105fb790

Sets the deadline for this :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` object to be *secs* seconds and *nsecs* nanoseconds since the reference clock epoch (the same as :sip:ref:`~PyQt6.QtCore.QElapsedTimer.msecsSinceReference`), and the timer type to *timerType*. If the value is in the past, this :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` will be marked as expired.

If *secs* or *nsecs* is ``std::numeric_limits<qint64>::max()``, this :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` will be set to never expire. If *nsecs* is more than 1 billion nanoseconds (1 second), then *secs* will be adjusted accordingly.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.setDeadline`, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.deadline`, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.deadlineNSecs`, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.setRemainingTime`.
