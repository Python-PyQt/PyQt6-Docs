.. sip:method-description::
    :status: todo
    :pysig: a74641895988c2587b61f1b4f6c273ca
    :realsig: (Qt::TimerType)
    :digest: 1d3e151989b8b17c5fde806926b4cdd3

Returns a :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` that is expired but is guaranteed to contain the current time. Objects created by this function can participate in the calculation of how long a timer is overdue, using the :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.deadline` function.

The :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` object will be constructed with the specified *timerType*.
