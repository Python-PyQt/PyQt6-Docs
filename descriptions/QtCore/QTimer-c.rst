.. sip:class-description::
    :status: todo
    :brief: Repetitive and single-shot timers
    :digest: e1aaca5bbb27416440ef09434bbdd05c

The :sip:ref:`~PyQt6.QtCore.QTimer` class provides repetitive and single-shot timers.

The :sip:ref:`~PyQt6.QtCore.QTimer` class provides a high-level programming interface for timers. To use it, create a :sip:ref:`~PyQt6.QtCore.QTimer`, connect its :sip:ref:`~PyQt6.QtCore.QTimer.timeout` signal to the appropriate slots, and call :sip:ref:`~PyQt6.QtCore.QTimer.start`. From then on, it will emit the :sip:ref:`~PyQt6.QtCore.QTimer.timeout` signal at constant intervals.

Example for a one second (1000 millisecond) timer (from the Analog Clock example):

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-widgets-analogclock-analogclock.py
    :lines: 66-66

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-widgets-analogclock-analogclock.py
    :lines: 68-68

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-widgets-analogclock-analogclock.py
    :lines: 70-70

From then on, the ``update()`` slot is called every second.

You can set a timer to time out only once by calling :sip:ref:`~PyQt6.QtCore.QTimer.setSingleShot`\ (true). You can also use the static :sip:ref:`~PyQt6.QtCore.QTimer.singleShot` function to call a slot after a specified interval:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-timers-timers.py
    :lines: 72-72

In multithreaded applications, you can use :sip:ref:`~PyQt6.QtCore.QTimer` in any thread that has an event loop. To start an event loop from a non-GUI thread, use :sip:ref:`~PyQt6.QtCore.QThread.exec`. Qt uses the timer's :sip:ref:`~PyQt6.QtCore.QObject.thread` to determine which thread will emit the :sip:ref:`~PyQt6.QtCore.QTimer.timeout` signal. Because of this, you must start and stop the timer in its thread; it is not possible to start a timer from another thread.

As a special case, a :sip:ref:`~PyQt6.QtCore.QTimer` with a timeout of 0 will time out as soon as possible, though the ordering between zero timers and other sources of events is unspecified. Zero timers can be used to do some work while still providing a snappy user interface:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-timers-timers.py
    :lines: 78-78

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-timers-timers.py
    :lines: 80-80

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-timers-timers.py
    :lines: 82-82

From then on, ``processOneThing()`` will be called repeatedly. It should be written in such a way that it always returns quickly (typically after processing one data item) so that Qt can deliver events to the user interface and stop the timer as soon as it has done all its work. This is the traditional way of implementing heavy work in GUI applications, but as multithreading is nowadays becoming available on more and more platforms, we expect that zero-millisecond :sip:ref:`~PyQt6.QtCore.QTimer` objects will gradually be replaced by :sip:ref:`~PyQt6.QtCore.QThread`\ s.

.. _qtimer-accuracy-and-timer-resolution:

Accuracy and Timer Resolution
-----------------------------

The accuracy of timers depends on the underlying operating system and hardware. Most platforms support a resolution of 1 millisecond, though the accuracy of the timer will not equal this resolution in many real-world situations.

The accuracy also depends on the :sip:ref:`~PyQt6.QtCore.Qt.TimerType`. For :sip:ref:`~PyQt6.QtCore.Qt.TimerType.PreciseTimer`, :sip:ref:`~PyQt6.QtCore.QTimer` will try to keep the accuracy at 1 millisecond. Precise timers will also never time out earlier than expected.

For :sip:ref:`~PyQt6.QtCore.Qt.TimerType.CoarseTimer` and :sip:ref:`~PyQt6.QtCore.Qt.TimerType.VeryCoarseTimer` types, :sip:ref:`~PyQt6.QtCore.QTimer` may wake up earlier than expected, within the margins for those types: 5% of the interval for :sip:ref:`~PyQt6.QtCore.Qt.TimerType.CoarseTimer` and 500 ms for :sip:ref:`~PyQt6.QtCore.Qt.TimerType.VeryCoarseTimer`.

All timer types may time out later than expected if the system is busy or unable to provide the requested accuracy. In such a case of timeout overrun, Qt will emit :sip:ref:`~PyQt6.QtCore.QTimer.timeout` only once, even if multiple timeouts have expired, and then will resume the original interval.

.. _qtimer-alternatives-to-qtimer:

Alternatives to QTimer
----------------------

An alternative to using :sip:ref:`~PyQt6.QtCore.QTimer` is to call :sip:ref:`~PyQt6.QtCore.QObject.startTimer` for your object and reimplement the :sip:ref:`~PyQt6.QtCore.QObject.timerEvent` event handler in your class (which must inherit :sip:ref:`~PyQt6.QtCore.QObject`). The disadvantage is that :sip:ref:`~PyQt6.QtCore.QTimer.timerEvent` does not support such high-level features as single-shot timers or signals.

Another alternative is :sip:ref:`~PyQt6.QtCore.QBasicTimer`. It is typically less cumbersome than using :sip:ref:`~PyQt6.QtCore.QObject.startTimer` directly. See `Timers <https://doc.qt.io/qt-6/timers.html>`_ for an overview of all three approaches.

Some operating systems limit the number of timers that may be used; Qt tries to work around these limitations.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QBasicTimer`, :sip:ref:`~PyQt6.QtCore.QTimerEvent`, :sip:ref:`~PyQt6.QtCore.QObject.timerEvent`, `Timers <https://doc.qt.io/qt-6/timers.html>`_.
