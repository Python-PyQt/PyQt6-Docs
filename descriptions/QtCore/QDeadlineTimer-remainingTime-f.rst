.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 2acef4a7890738532c60a053581b4fb6

Returns the remaining time in this :sip:ref:`~PyQt6.QtCore.QDeadlineTimer` object in milliseconds. If the timer has already expired, this function will return zero and it is not possible to obtain the amount of time overdue with this function (to do that, see :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.deadline`). If the timer was set to never expire, this function returns -1.

This function is suitable for use in Qt APIs that take a millisecond timeout, such as the many :sip:ref:`~PyQt6.QtCore.QIODevice` ``waitFor`` functions or the timed lock functions in :sip:ref:`~PyQt6.QtCore.QMutex`, :sip:ref:`~PyQt6.QtCore.QWaitCondition`, :sip:ref:`~PyQt6.QtCore.QSemaphore`, or :sip:ref:`~PyQt6.QtCore.QReadWriteLock`. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qdeadlinetimer.py
    :lines: 94-94

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.setRemainingTime`, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.remainingTimeNSecs`, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.isForever`, :sip:ref:`~PyQt6.QtCore.QDeadlineTimer.hasExpired`.
