.. sip:method-description::
    :status: todo
    :pysig: 8a61ed400de190ee2387d9e67258a1df
    :realsig: (Qt::TimerType)
    :digest: 60ab330409c4e94cb18e217ee71c3701

Changes the timer type for this object to *timerType*.

The behavior for each possible value of *timerType* is operating-system dependent. :sip:ref:`~PyQt6.QtCore.Qt.TimerType.PreciseTimer` will use the most precise timer that Qt can find, with resolution of 1 millisecond or better, whereas :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` will try to use a more coarse timer for :sip:ref:`~PyQt6.QtCore.Qt.TimerType.CoarseTimer` and :sip:ref:`~PyQt6.QtCore.Qt.TimerType.VeryCoarseTimer`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.timerType`, :sip:ref:`~PyQt6.QtCore.Qt.TimerType`.
