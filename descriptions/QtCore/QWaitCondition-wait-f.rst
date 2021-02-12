.. sip:method-description::
    :status: todo
    :pysig: 69bb698039878847e2621339fa03744a
    :realsig: (QMutex*,QDeadlineTimer)
    :digest: 4fc92230ccbc2efe5bc0832947de7ec5

Releases the *lockedMutex* and waits on the wait condition. The *lockedMutex* must be initially locked by the calling thread. If *lockedMutex* is not in a locked state, the behavior is undefined. If *lockedMutex* is a recursive mutex, this function returns immediately. The *lockedMutex* will be unlocked, and the calling thread will block until either of these conditions is met:

* Another thread signals it using :sip:ref:`~PyQt6.QtCore.QWaitCondition.wakeOne` or :sip:ref:`~PyQt6.QtCore.QWaitCondition.wakeAll`. This function will return true in this case.

* the deadline given by *deadline* is reached. If *deadline* is ``QDeadlineTimer::Forever`` (the default), then the wait will never timeout (the event must be signalled). This function will return false if the wait timed out.

The *lockedMutex* will be returned to the same locked state. This function is provided to allow the atomic transition from the locked state to the wait state.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QWaitCondition.wakeOne`, :sip:ref:`~PyQt6.QtCore.QWaitCondition.wakeAll`.
