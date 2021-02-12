.. sip:method-description::
    :status: todo
    :pysig: d7cfe561d8d8635bcf100d8950014329
    :realsig: (Qt::TimerType)
    :digest: f5e3bd05c22b4ce0efaadec221623a20

Constructs an expired :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` object. For this object, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.remainingTime` will return 0.

The timer type *timerType* may be ignored, since the timer is already expired. Similarly, for optimization purposes, this function will not attempt to obtain the current time and will use a value known to be in the past. Therefore, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.deadline` may return an unexpected value and this object cannot be used in calculation of how long it is overdue. If that functionality is required, use :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.current`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.hasExpired`, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.remainingTime`, :sip:ref:`~PyQt6.QtCore.Qt.TimerType`, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.current`.
