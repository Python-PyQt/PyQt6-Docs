.. sip:method-description::
    :status: todo
    :pysig: 1794526a133c101ed5249f3aa1e3bdff
    :realsig: (int,QObject*)
    :digest: 7c17001e4b8ecc1a965fbeb9f327db23

Starts (or restarts) the timer with a *msec* milliseconds timeout. The timer will be a :sip:ref:`~PyQt6.QtCore.Qt.TimerType.CoarseTimer`. See :sip:ref:`~PyQt6.QtCore.Qt.TimerType` for information on the different timer types.

The given *object* will receive timer events.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QBasicTimer.stop`, :sip:ref:`~PyQt6.QtCore.QBasicTimer.isActive`, :sip:ref:`~PyQt6.QtCore.QObject.timerEvent`, :sip:ref:`~PyQt6.QtCore.Qt.TimerType.CoarseTimer`.
