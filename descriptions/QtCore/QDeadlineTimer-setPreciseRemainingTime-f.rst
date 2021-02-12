.. sip:method-description::
    :status: todo
    :pysig: 7196d5afe7051c0b69382f21afc5470d
    :realsig: (qint64,qint64,Qt::TimerType)
    :digest: ef4413ef300215437d4b59df37bff006

Sets the remaining time for this :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` object to *secs* seconds plus *nsecs* nanoseconds from now, if *secs* has a positive value. If *secs* is -1, this :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` will be set it to never expire. If both parameters are zero, this :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` will be marked as expired.

The timer type for this :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` object will be set to the specified *timerType*.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.setRemainingTime`, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.hasExpired`, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.isForever`, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.remainingTime`.
