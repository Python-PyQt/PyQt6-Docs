.. sip:method-description::
    :status: todo
    :pysig: de73bee7c95e21348f60101258658424
    :realsig: (QDeadlineTimer)
    :digest: fca702bde0e05594620317a6535f83a5

Attempts to lock the mutex. This function returns ``true`` if the lock was obtained; otherwise it returns ``false``. If another thread has locked the mutex, this function will wait until *timeout* expires for the mutex to become available.

If the lock was obtained, the mutex must be unlocked with :sip:ref:`~PyQt6.QtCore.QRecursiveMutex.unlock` before another thread can successfully lock it.

Calling this function multiple times on the same mutex from the same thread is allowed.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRecursiveMutex.lock`, :sip:ref:`~PyQt6.QtCore.QRecursiveMutex.unlock`.
