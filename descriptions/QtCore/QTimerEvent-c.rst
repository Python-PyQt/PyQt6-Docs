.. sip:class-description::
    :status: todo
    :brief: Contains parameters that describe a timer event
    :digest: cf07254df90ae3c4ac4a38feb4dcf511

The :sip:ref:`~PyQt6.QtCore.QTimerEvent` class contains parameters that describe a timer event.

Timer events are sent at regular intervals to objects that have started one or more timers. Each timer has a unique identifier. A timer is started with :sip:ref:`~PyQt6.QtCore.QObject.startTimer`.

The QChronoTimer class provides a high-level programming interface that uses signals instead of events.

The event handler :sip:ref:`~PyQt6.QtCore.QObject.timerEvent` receives timer events.

.. seealso:: QChronoTimer, :sip:ref:`~PyQt6.QtCore.QObject.timerEvent`, :sip:ref:`~PyQt6.QtCore.QObject.startTimer`, :sip:ref:`~PyQt6.QtCore.QObject.killTimer`.
