.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 70a9a59c7ee74f9987de0c0221747760

Returns the number of milliseconds between last time this :sip:ref:`~PyQt6.QtCore.QElapsedTimer` object was started and its reference clock's start.

This number is usually arbitrary for all clocks except the :sip:ref:`~PyQt6.QtCore.QElapsedTimer.ClockType.SystemTime` clock. For that clock type, this number is the number of milliseconds since January 1st, 1970 at 0:00 UTC (that is, it is the Unix time expressed in milliseconds).

On Linux, Windows and Apple platforms, this value is usually the time since the system boot, though it usually does not include the time the system has spent in sleep states.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QElapsedTimer.clockType`, :sip:ref:`~PyQt6.QtCore.QElapsedTimer.elapsed`.
