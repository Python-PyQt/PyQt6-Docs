.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: bb0f77aa5170cd95ac039f8d25cc45a5

This function overloads start().

Starts or restarts the timer with the timeout specified in :sip:ref:`~PyQt6.QtCore.QTimer.interval`.

If the timer is already running, it will be :sip:ref:`~PyQt6.QtCore.QTimer.stop` and restarted. This will also change its :sip:ref:`~PyQt6.QtCore.QTimer.id`.

If :sip:ref:`~PyQt6.QtCore.QTimer.singleShot` is true, the timer will be activated only once.
