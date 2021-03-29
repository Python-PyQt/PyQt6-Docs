.. sip:method-description::
    :status: todo
    :pysig: e93f2860b26a60bc1405b55c3061b147
    :realsig: (qint64,Qt::TimerType)
    :digest: 6df9394bc92c9648477115920301a4eb

Sets the deadline for this :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` object to be the *msecs* absolute time point, counted in milliseconds since the reference clock (the same as :sip:ref:`~PyQt6.QtCore.QElapsedTimer.msecsSinceReference`), and the timer type to *timerType*. If the value is in the past, this :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` will be marked as expired.

If *msecs* is ``std::numeric_limits<qint64>::max()`` or the deadline is beyond a representable point in the future, this :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` will be set to never expire.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.setPreciseDeadline`, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.deadline`, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.deadlineNSecs`, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.setRemainingTime`.
