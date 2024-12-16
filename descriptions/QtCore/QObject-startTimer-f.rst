.. sip:method-description::
    :status: todo
    :pysig: e089caa2e876507943e5ec09f7bd4dcf
    :realsig: (int,Qt::TimerType)
    :digest: cf87e8ea00e2b081877c39a7094cd47e

This is an overloaded function that will start a timer of type *timerType* and a timeout of *interval* milliseconds. This is equivalent to calling:

::

    startTimer(std::chrono::milliseconds{interval}, timerType);

.. seealso:: :sip:ref:`~PyQt6.QtCore.QObject.timerEvent`, :sip:ref:`~PyQt6.QtCore.QObject.killTimer`, QChronoTimer, :sip:ref:`~PyQt6.QtCore.QBasicTimer`.
