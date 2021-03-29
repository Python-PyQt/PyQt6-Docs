.. sip:method-description::
    :status: todo
    :pysig: e089caa2e876507943e5ec09f7bd4dcf
    :realsig: (int,Qt::TimerType)
    :digest: 9cf48eaa8cf83b245913dd6169b7be81

Starts a timer and returns a timer identifier, or returns zero if it could not start a timer.

A timer event will occur every *interval* milliseconds until :sip:ref:`~PyQt6.QtCore.QObject.killTimer` is called. If *interval* is 0, then the timer event occurs once every time there are no more window system events to process.

The virtual :sip:ref:`~PyQt6.QtCore.QObject.timerEvent` function is called with the :sip:ref:`~PyQt6.QtCore.QTimerEvent` event parameter class when a timer event occurs. Reimplement this function to get timer events.

If multiple timers are running, the :sip:ref:`~PyQt6.QtCore.QTimerEvent.timerId` can be used to find out which timer was activated.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qobject.py
    :lines: 144-177

Note that :sip:ref:`~PyQt6.QtCore.QTimer`'s accuracy depends on the underlying operating system and hardware. The *timerType* argument allows you to customize the accuracy of the timer. See :sip:ref:`~PyQt6.QtCore.Qt.TimerType` for information on the different timer types. Most platforms support an accuracy of 20 milliseconds; some provide more. If Qt is unable to deliver the requested number of timer events, it will silently discard some.

The :sip:ref:`~PyQt6.QtCore.QTimer` class provides a high-level programming interface with single-shot timers and timer signals instead of events. There is also a :sip:ref:`~PyQt6.QtCore.QBasicTimer` class that is more lightweight than :sip:ref:`~PyQt6.QtCore.QTimer` and less clumsy than using timer IDs directly.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QObject.timerEvent`, :sip:ref:`~PyQt6.QtCore.QObject.killTimer`, :sip:ref:`~PyQt6.QtCore.QTimer.singleShot`.
