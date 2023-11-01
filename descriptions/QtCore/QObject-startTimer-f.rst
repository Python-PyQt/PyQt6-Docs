.. sip:method-description::
    :status: todo
    :pysig: e089caa2e876507943e5ec09f7bd4dcf
    :realsig: (int,Qt::TimerType)
    :digest: 672cf53c7f3f9be2c3e8efc3eceefe48

This is an overloaded function that will start a timer of type *timerType* and a timeout of *interval* milliseconds. This is equivalent to calling:

::

    startTimer(std::chrono::milliseconds{interval}, timerType);

.. seealso:: :sip:ref:`~PyQt6.QtCore.QObject.timerEvent`, :sip:ref:`~PyQt6.QtCore.QObject.killTimer`, :sip:ref:`~PyQt6.QtCore.QTimer.singleShot`.
