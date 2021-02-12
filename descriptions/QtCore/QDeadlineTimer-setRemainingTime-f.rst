.. sip:method-description::
    :status: todo
    :pysig: e93f2860b26a60bc1405b55c3061b147
    :realsig: (qint64,Qt::TimerType)
    :digest: a31b3643914c05753f9e87a9d092792f

Sets the remaining time for this :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` object to *msecs* milliseconds from now, if *msecs* has a positive value. If *msecs* is zero, this :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` object will be marked as expired, whereas a value of -1 will set it to never expire.

The timer type for this :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` object will be set to the specified *timerType*.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.setPreciseRemainingTime`, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.hasExpired`, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.isForever`, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.remainingTime`.
