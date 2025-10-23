.. sip:method-description::
    :status: todo
    :pysig: de73bee7c95e21348f60101258658424
    :realsig: (QDeadlineTimer)
    :digest: e2c6814bc474857a572fb52bb7a99897

Attempts to lock the mutex. This function returns ``true`` if the lock was obtained; otherwise it returns ``false``. If another thread has locked the mutex, this function will wait until *timer* expires for the mutex to become available.

If the lock was obtained, the mutex must be unlocked with :sip:ref:`~PyQt6.QtCore.QMutex.unlock` before another thread can successfully lock it.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMutex.lock`, :sip:ref:`~PyQt6.QtCore.QMutex.unlock`.
