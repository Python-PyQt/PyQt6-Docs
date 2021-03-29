.. sip:class-description::
    :status: todo
    :brief: Contains parameters that describe a timer event
    :digest: a4bb621aba3e3a0296181e76afd6f6b5

The :sip:ref:`~PyQt6.QtCore.QTimerEvent` class contains parameters that describe a timer event.

Timer events are sent at regular intervals to objects that have started one or more timers. Each timer has a unique identifier. A timer is started with :sip:ref:`~PyQt6.QtCore.QObject.startTimer`.

The :sip:ref:`~PyQt6.QtCore.QTimer` class provides a high-level programming interface that uses signals instead of events. It also provides single-shot timers.

The event handler :sip:ref:`~PyQt6.QtCore.QObject.timerEvent` receives timer events.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimer`, :sip:ref:`~PyQt6.QtCore.QObject.timerEvent`, :sip:ref:`~PyQt6.QtCore.QObject.startTimer`, :sip:ref:`~PyQt6.QtCore.QObject.killTimer`.
