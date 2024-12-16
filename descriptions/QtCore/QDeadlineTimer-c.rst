.. sip:class-description::
    :status: todo
    :brief: Marks a deadline in the future
    :digest: 35ecc2b7f1ce333326ac58ceffb0370c

The :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` class marks a deadline in the future.

The :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` class is usually used to calculate future deadlines and verify whether the deadline has expired. :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` can also be used for deadlines without expiration ("forever"). It forms a counterpart to :sip:ref:`~PyQt6.QtCore.QElapsedTimer`, which calculates how much time has elapsed since :sip:ref:`~PyQt6.QtCore.QElapsedTimer.start` was called.

:sip:ref:`~PyQt6.QtCore.QDeadlineTimer` provides a more convenient API compared to :sip:ref:`~PyQt6.QtCore.QElapsedTimer.hasExpired`.

The typical use-case for the class is to create a :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` before the operation in question is started, and then use :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.remainingTime` or :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.hasExpired` to determine whether to continue trying the operation. :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` objects can be passed to functions being called to execute this operation so they know how long to still operate.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qdeadlinetimer.py
    :lines: 54-62

Many :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` functions deal with time out values, which all are measured in milliseconds. There are two special values, the same as many other Qt functions named ``waitFor`` or similar:

* 0: no time left, expired

* -1: infinite time left, timer never expires

.. _qdeadlinetimer-reference-clocks:

Reference Clocks
----------------

:sip:ref:`~PyQt6.QtCore.QDeadlineTimer` will use the same clock as :sip:ref:`~PyQt6.QtCore.QElapsedTimer` (see :sip:ref:`~PyQt6.QtCore.QElapsedTimer.clockType` and :sip:ref:`~PyQt6.QtCore.QElapsedTimer.isMonotonic`).

.. _qdeadlinetimer-timer-types:

Timer types
-----------

Like :sip:ref:`~PyQt6.QtCore.QTimer` and QChronoTimer, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` can select among different levels of coarseness on the timers. You can select precise timing by passing :sip:ref:`~PyQt6.QtCore.Qt.TimerType.PreciseTimer` to the functions that set of change the timer, or you can select coarse timing by passing :sip:ref:`~PyQt6.QtCore.Qt.TimerType.CoarseTimer`. :sip:ref:`~PyQt6.QtCore.Qt.TimerType.VeryCoarseTimer` is currently interpreted the same way as :sip:ref:`~PyQt6.QtCore.Qt.TimerType.CoarseTimer`.

This feature is dependent on support from the operating system: if the OS does not support a coarse timer functionality, then :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` will behave like :sip:ref:`~PyQt6.QtCore.Qt.TimerType.PreciseTimer` was passed.

:sip:ref:`~PyQt6.QtCore.QDeadlineTimer` defaults to :sip:ref:`~PyQt6.QtCore.Qt.TimerType.CoarseTimer` because on operating systems that do support coarse timing, making timing calls to that clock source is often much more efficient. The level of coarseness depends on the operating system, but should be in the order of a couple of milliseconds.

``std::chrono`` Compatibility
-----------------------------

:sip:ref:`~PyQt6.QtCore.QDeadlineTimer` is compatible with the ``std::chrono`` API from C++11 and can be constructed from or compared to both ``std::chrono::duration`` and ``std::chrono::time_point`` objects. In addition, it is fully compatible with the time literals from C++14, which allow one to write code as:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qdeadlinetimer.py
    :lines: 66-72

As can be seen in the example above, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` offers a templated version of :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.remainingTime` and :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.deadline` that can be used to return ``std::chrono`` objects.

Note that comparing to ``time_point`` is not as efficient as comparing to ``duration``, since :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` may need to convert from its own internal clock source to the clock source used by the ``time_point`` object. Also note that, due to this conversion, the deadlines will not be precise, so the following code is not expected to compare equally:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qdeadlinetimer.py
    :lines: 76-80

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTime`, QChronoTimer, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer`, :sip:ref:`~PyQt6.QtCore.Qt.TimerType`.
