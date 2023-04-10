.. sip:class-description::
    :status: todo
    :brief: Timer events for objects
    :digest: 27aba15ef55a5a79094fc190ff19ed2a

The :sip:ref:`~PyQt6.QtCore.QBasicTimer` class provides timer events for objects.

This is a fast, lightweight, and low-level class used by Qt internally. We recommend using the higher-level :sip:ref:`~PyQt6.QtCore.QTimer` class rather than this class if you want to use timers in your applications. Note that this timer is a repeating timer that will send subsequent timer events unless the :sip:ref:`~PyQt6.QtCore.QBasicTimer.stop` function is called.

To use this class, create a :sip:ref:`~PyQt6.QtCore.QBasicTimer`, and call its start() function with a timeout interval and with a pointer to a :sip:ref:`~PyQt6.QtCore.QObject` subclass. When the timer times out it will send a timer event to the :sip:ref:`~PyQt6.QtCore.QObject` subclass. The timer can be stopped at any time using :sip:ref:`~PyQt6.QtCore.QBasicTimer.stop`. :sip:ref:`~PyQt6.QtCore.QBasicTimer.isActive` returns ``true`` for a timer that is running; i.e. it has been started, has not reached the timeout time, and has not been stopped. The timer's ID can be retrieved using :sip:ref:`~PyQt6.QtCore.QBasicTimer.timerId`.

Objects of this class cannot be copied, but can be moved, so you can maintain a list of basic timers by holding them in container that supports move-only types, e.g. std::vector.

The `Tetrix <https://doc.qt.io/qt-6/qtwidgets-widgets-tetrix-example.html>`_ example uses :sip:ref:`~PyQt6.QtCore.QBasicTimer` to control the rate at which pieces fall.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimer`, :sip:ref:`~PyQt6.QtCore.QTimerEvent`, :sip:ref:`~PyQt6.QtCore.QObject.timerEvent`, `Timers <https://doc.qt.io/qt-6/timers.html>`_, `Affine Transformations <https://doc.qt.io/qt-6/qtwidgets-painting-affine-example.html>`_.
