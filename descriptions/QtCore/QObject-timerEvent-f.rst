.. sip:method-description::
    :status: todo
    :pysig: 8535b56d973bcd98293a2acc5afd0cf4
    :realsig: (QTimerEvent*)
    :digest: d146af2a0833f2ebd3e750b0cba7abc5

This event handler can be reimplemented in a subclass to receive timer events for the object.

:sip:ref:`~PyQt6.QtCore.QTimer` provides a higher-level interface to the timer functionality, and also more general information about timers. The timer event is passed in the *event* parameter.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QObject.startTimer`, :sip:ref:`~PyQt6.QtCore.QObject.killTimer`, :sip:ref:`~PyQt6.QtCore.QObject.event`.
