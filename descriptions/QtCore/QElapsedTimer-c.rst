.. sip:class-description::
    :status: todo
    :brief: Fast way to calculate elapsed times
    :digest: c4a53ff1906487ce8d53cc13bcc0520a

The :sip:ref:`~PyQt6.QtCore.QElapsedTimer` class provides a fast way to calculate elapsed times.

The :sip:ref:`~PyQt6.QtCore.QElapsedTimer` class is usually used to quickly calculate how much time has elapsed between two events. Its API is similar to that of :sip:ref:`~PyQt6.QtCore.QTime`, so code that was using that can be ported quickly to the new class.

However, unlike :sip:ref:`~PyQt6.QtCore.QTime`, :sip:ref:`~PyQt6.QtCore.QElapsedTimer` tries to use monotonic clocks if possible. This means it's not possible to convert :sip:ref:`~PyQt6.QtCore.QElapsedTimer` objects to a human-readable time.

The typical use-case for the class is to determine how much time was spent in a slow operation. The simplest example of such a case is for debugging purposes, as in the following example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-qelapsedtimer-main.py

In this example, the timer is started by a call to :sip:ref:`~PyQt6.QtCore.QElapsedTimer.start` and the elapsed time is calculated by the :sip:ref:`~PyQt6.QtCore.QElapsedTimer.elapsed` function.

The time elapsed can also be used to recalculate the time available for another operation, after the first one is complete. This is useful when the execution must complete within a certain time period, but several steps are needed. The ``waitFor``-type functions in :sip:ref:`~PyQt6.QtCore.QIODevice` and its subclasses are good examples of such need. In that case, the code could be as follows:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-qelapsedtimer-main.py

Another use-case is to execute a certain operation for a specific timeslice. For this, :sip:ref:`~PyQt6.QtCore.QElapsedTimer` provides the :sip:ref:`~PyQt6.QtCore.QElapsedTimer.hasExpired` convenience function, which can be used to determine if a certain number of milliseconds has already elapsed:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-qelapsedtimer-main.py

It is often more convenient to use :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` in this case, which counts towards a timeout in the future instead of tracking elapsed time.

.. _qelapsedtimer-reference-clocks:

Reference Clocks
----------------

:sip:ref:`~PyQt6.QtCore.QElapsedTimer` will use the platform's monotonic reference clock in all platforms that support it (see :sip:ref:`~PyQt6.QtCore.QElapsedTimer.isMonotonic`). This has the added benefit that :sip:ref:`~PyQt6.QtCore.QElapsedTimer` is immune to time adjustments, such as the user correcting the time. Also unlike :sip:ref:`~PyQt6.QtCore.QTime`, :sip:ref:`~PyQt6.QtCore.QElapsedTimer` is immune to changes in the timezone settings, such as daylight-saving periods.

On the other hand, this means :sip:ref:`~PyQt6.QtCore.QElapsedTimer` values can only be compared with other values that use the same reference. This is especially true if the time since the reference is extracted from the :sip:ref:`~PyQt6.QtCore.QElapsedTimer` object (\ :sip:ref:`~PyQt6.QtCore.QElapsedTimer.msecsSinceReference`) and serialised. These values should never be exchanged across the network or saved to disk, since there's no telling whether the computer node receiving the data is the same as the one originating it or if it has rebooted since.

It is, however, possible to exchange the value with other processes running on the same machine, provided that they also use the same reference clock. :sip:ref:`~PyQt6.QtCore.QElapsedTimer` will always use the same clock, so it's safe to compare with the value coming from another process in the same machine. If comparing to values produced by other APIs, you should check that the clock used is the same as :sip:ref:`~PyQt6.QtCore.QElapsedTimer` (see :sip:ref:`~PyQt6.QtCore.QElapsedTimer.clockType`).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTime`, QChronoTimer, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer`.
