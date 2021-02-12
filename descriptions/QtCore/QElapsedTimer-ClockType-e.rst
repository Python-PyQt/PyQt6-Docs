.. sip:enum-description::
    :status: todo
    :digest: 3be02a385602d5f7a6caad7706a1c60c

This enum contains the different clock types that :sip:ref:`~PyQt6.QtCore.QElapsedTimer` may use.

:sip:ref:`~PyQt6.QtCore.QElapsedTimer` will always use the same clock type in a particular machine, so this value will not change during the lifetime of a program. It is provided so that :sip:ref:`~PyQt6.QtCore.QElapsedTimer` can be used with other non-Qt implementations, to guarantee that the same reference clock is being used.

SystemTime
..........

The system time clock is purely the real time, expressed in milliseconds since Jan 1, 1970 at 0:00 UTC. It's equivalent to the value returned by the C and POSIX ``time`` function, with the milliseconds added. This clock type is currently only used on Unix systems that do not support monotonic clocks (see below).

This is the only non-monotonic clock that :sip:ref:`~PyQt6.QtCore.QElapsedTimer` may use.

MonotonicClock
..............

This is the system's monotonic clock, expressed in milliseconds since an arbitrary point in the past. This clock type is used on Unix systems which support POSIX monotonic clocks (``_POSIX_MONOTONIC_CLOCK``).

This clock does not overflow.

TickCounter
...........

The tick counter clock type is based on the system's or the processor's tick counter, multiplied by the duration of a tick. This clock type is used on Windows platforms. If the high-precision performance counter is available on Windows, the ``\ :sip:ref:`~PyQt6.QtCore.QElapsedTimer.ClockType.PerformanceCounter``` clock type is used instead.

The :sip:ref:`~PyQt6.QtCore.QElapsedTimer.ClockType.TickCounter` clock type is the only clock type that may overflow. Windows Vista and Windows Server 2008 support the extended 64-bit tick counter, which allows avoiding the overflow.

On Windows systems, the clock overflows after 2^32 milliseconds, which corresponds to roughly 49.7 days. This means two processes' reckoning of the time since the reference may be different by multiples of 2^32 milliseconds. When comparing such values, it's recommended that the high 32 bits of the millisecond count be masked off.

MachAbsoluteTime
................

This clock type is based on the absolute time presented by Mach kernels, such as that found on macOS. This clock type is presented separately from :sip:ref:`~PyQt6.QtCore.QElapsedTimer.ClockType.MonotonicClock` since macOS and iOS are also Unix systems and may support a POSIX monotonic clock with values differing from the Mach absolute time.

This clock is monotonic and does not overflow.

PerformanceCounter
..................

This clock uses the Windows functions ``QueryPerformanceCounter`` and ``QueryPerformanceFrequency`` to access the system's high-precision performance counter. Since this counter may not be available on all systems, :sip:ref:`~PyQt6.QtCore.QElapsedTimer` will fall back to the ``\ :sip:ref:`~PyQt6.QtCore.QElapsedTimer.ClockType.TickCounter``` clock automatically, if this clock cannot be used.

This clock is monotonic and does not overflow.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QElapsedTimer.clockType`, :sip:ref:`~PyQt6.QtCore.QElapsedTimer.isMonotonic`.
