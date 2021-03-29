.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 9855eea63bee3673e742fc9987739457

Returns the absolute time point for the deadline stored in :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` object, calculated in milliseconds relative to the reference clock, the same as :sip:ref:`~PyQt6.QtCore.QElapsedTimer.msecsSinceReference`. The value will be in the past if this :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` has expired.

If this :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` never expires, this function returns ``std::numeric_limits<qint64>::max()``.

This function can be used to calculate the amount of time a timer is overdue, by subtracting :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.current` or :sip:ref:`~PyQt6.QtCore.QElapsedTimer.msecsSinceReference`, as in the following example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qdeadlinetimer.py
    :lines: 98-105

**Note:** Timers that were created as expired have an indetermine time point in the past as their deadline, so the above calculation may not work.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.remainingTime`, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.deadlineNSecs`, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.setDeadline`.
