.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 42e52288686b8e8bd1bf97fca53f89b9

Starts or restarts the timer with the timeout specified in :sip:ref:`~PyQt6.QtCore.QTimer.interval`.

If the timer is already running, it will be :sip:ref:`~PyQt6.QtCore.QTimer.stop` and restarted. This will also change its :sip:ref:`~PyQt6.QtCore.QTimer.id`.

If :sip:ref:`~PyQt6.QtCore.QTimer.singleShot` is true, the timer will be activated only once.

**Note:** Keeping the event loop busy with a zero-timer is bound to cause trouble and highly erratic behavior of the UI.
