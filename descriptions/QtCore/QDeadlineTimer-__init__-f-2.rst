.. sip:method-description::
    :status: todo
    :pysig: 128ee4a0714c7a52bea50ef631bd22f7
    :realsig: (QDeadlineTimer::ForeverConstant,Qt::TimerType)
    :digest: 9a7b53758d8b19827beb5d6fca676653

:sip:ref:`~PyQt6.QtCore.QDeadlineTimer` objects created with :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.ForeverConstant.ForeverConstant` never expire. For such objects, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.remainingTime` will return -1, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.deadline` will return the maximum value, and :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.isForever` will return true.

The timer type *timerType* may be ignored, since the timer will never expire.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.ForeverConstant.ForeverConstant`, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.hasExpired`, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.isForever`, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.remainingTime`, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.timerType`.
