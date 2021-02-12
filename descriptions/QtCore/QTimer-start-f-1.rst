.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 4d88b4b7e5b4a115425dbedf3553bf6e

Starts or restarts the timer with a timeout interval of *msec* milliseconds.

If the timer is already running, it will be :sip:ref:`~PyQt6.QtCore.QTimer.stop` and restarted.

If :sip:ref:`~PyQt6.QtCore.QTimer.singleShot` is true, the timer will be activated only once.
