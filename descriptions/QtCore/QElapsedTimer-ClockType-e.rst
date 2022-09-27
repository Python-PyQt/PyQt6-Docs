.. sip:enum-description::
    :status: todo
    :digest: 1930c6fe3de1ad2709f5e9892a9648d7

This enum contains the different clock types that :sip:ref:`~PyQt6.QtCore.QElapsedTimer` may use.

:sip:ref:`~PyQt6.QtCore.QElapsedTimer` will always use the same clock type in a particular machine, so this value will not change during the lifetime of a program. It is provided so that :sip:ref:`~PyQt6.QtCore.QElapsedTimer` can be used with other non-Qt implementations, to guarantee that the same reference clock is being used.

SystemTime
..........

The system time clock is purely the real time, expressed in milliseconds since Jan 1, 1970 at 0:00 UTC. It's equivalent to the value returned by the C and POSIX ``time`` function, with the milliseconds added. This clock type is currently only used on Unix systems that do not support monotonic clocks (see below).

This is the only non-monotonic clock that :sip:ref:`~PyQt6.QtCore.QElapsedTimer` may use.

MonotonicClock
..............

This is the system's monotonic clock, expressed in milliseconds since an arbitrary point in the past. This clock type is used on Unix systems which support POSIX monotonic clocks (``_POSIX_MONOTONIC_CLOCK``).

MachAbsoluteTime
................

This clock type is based on the absolute time presented by Mach kernels, such as that found on macOS. This clock type is presented separately from :sip:ref:`~PyQt6.QtCore.QElapsedTimer.ClockType.MonotonicClock` since macOS and iOS are also Unix systems and may support a POSIX monotonic clock with values differing from the Mach absolute time.

This clock is monotonic.

PerformanceCounter
..................

This clock uses the Windows functions ``QueryPerformanceCounter`` and ``QueryPerformanceFrequency`` to access the system's performance counter.

This clock is monotonic.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QElapsedTimer.clockType`, :sip:ref:`~PyQt6.QtCore.QElapsedTimer.isMonotonic`.
