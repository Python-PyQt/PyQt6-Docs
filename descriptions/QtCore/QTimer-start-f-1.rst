.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: dc1f68a42bdc435d4060d23a72947d0e

Starts or restarts the timer with a timeout interval of *msec* milliseconds.

If the timer is already running, it will be :sip:ref:`~PyQt6.QtCore.QTimer.stop` and restarted.

If :sip:ref:`~PyQt6.QtCore.QTimer.singleShot` is true, the timer will be activated only once. This is equivalent to:

::

    timer.setInterval(msec);
    timer.start();

**Note:** Keeping the event loop busy with a zero-timer is bound to cause trouble and highly erratic behavior of the UI.
