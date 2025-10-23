.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 72c5bee90343a5612a926587ac258905

Starts or restarts the timer with a timeout interval of *msec* milliseconds.

This is equivalent to:

::

    timer.setInterval(msec);
    timer.start();

If the timer is already running, it will be :sip:ref:`~PyQt6.QtCore.QTimer.stop` and restarted. This will also change its :sip:ref:`~PyQt6.QtCore.QTimer.id`.

If :sip:ref:`~PyQt6.QtCore.QTimer.singleShot` is true, the timer will be activated only once.

Starting from Qt 6.10, setting a negative interval will result in a run-time warning and the value being reset to 1ms. Before Qt 6.10 a Qt Timer would let you set a negative interval but behave in surprising ways (for example stop the timer if it was running or not start it at all).

**Note:** Keeping the event loop busy with a zero-timer is bound to cause trouble and highly erratic behavior of the UI.
