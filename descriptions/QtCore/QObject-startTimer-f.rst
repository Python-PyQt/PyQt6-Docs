.. sip:method-description::
    :status: todo
    :pysig: e089caa2e876507943e5ec09f7bd4dcf
    :realsig: (int,Qt::TimerType)
    :digest: 237cbf9e28369961cbff74a94c65cc89

This is an overloaded function that will start a timer of type *timerType* and a timeout of *interval* milliseconds. This is equivalent to calling:

::

    startTimer(std::chrono::milliseconds{interval}, timerType);

Starting from Qt 6.10, setting a negative interval will result in a run-time warning and the value being reset to 1ms. Before Qt 6.10 a Qt Timer would let you set a negative interval but behave in surprising ways (for example stop the timer if it was running or not start it at all).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QObject.timerEvent`, :sip:ref:`~PyQt6.QtCore.QObject.killTimer`, QChronoTimer, :sip:ref:`~PyQt6.QtCore.QBasicTimer`.
