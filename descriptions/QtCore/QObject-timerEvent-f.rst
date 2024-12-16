.. sip:method-description::
    :status: todo
    :pysig: 8535b56d973bcd98293a2acc5afd0cf4
    :realsig: (QTimerEvent*)
    :digest: 636ab7385adcab52c3d0d423bf44324b

This event handler can be reimplemented in a subclass to receive timer events for the object.

QChronoTimer provides higher-level interfaces to the timer functionality, and also more general information about timers. The timer event is passed in the *event* parameter.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QObject.startTimer`, :sip:ref:`~PyQt6.QtCore.QObject.killTimer`, :sip:ref:`~PyQt6.QtCore.QObject.event`.
