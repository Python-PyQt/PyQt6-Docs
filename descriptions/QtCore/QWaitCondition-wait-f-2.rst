.. sip:method-description::
    :status: todo
    :pysig: 84b763c6a7249f66b9f7f79e21893e63
    :realsig: (QReadWriteLock*,QDeadlineTimer)
    :digest: bdcaab33624b6282b80a22ca0629d6f3

Releases the *lockedReadWriteLock* and waits on the wait condition. The *lockedReadWriteLock* must be initially locked by the calling thread. If *lockedReadWriteLock* is not in a locked state, this function returns immediately. The *lockedReadWriteLock* must not be locked recursively, otherwise this function will not release the lock properly. The *lockedReadWriteLock* will be unlocked, and the calling thread will block until either of these conditions is met:

* Another thread signals it using :sip:ref:`~PyQt6.QtCore.QWaitCondition.wakeOne` or :sip:ref:`~PyQt6.QtCore.QWaitCondition.wakeAll`. This function will return true in this case.

* the deadline given by *deadline* is reached. If *deadline* is ``QDeadlineTimer::Forever`` (the default), then the wait will never timeout (the event must be signalled). This function will return false if the wait timed out.

The *lockedReadWriteLock* will be returned to the same locked state. This function is provided to allow the atomic transition from the locked state to the wait state.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QWaitCondition.wakeOne`, :sip:ref:`~PyQt6.QtCore.QWaitCondition.wakeAll`.
