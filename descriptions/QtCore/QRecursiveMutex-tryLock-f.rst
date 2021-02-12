.. sip:method-description::
    :status: todo
    :pysig: 382b2a2aedb37045cd9d00f29ea9f95e
    :realsig: (int)
    :digest: 6dd90273f5d99e20535580054b2ac82c

Attempts to lock the mutex. This function returns ``true`` if the lock was obtained; otherwise it returns ``false``. If another thread has locked the mutex, this function will wait for at most *timeout* milliseconds for the mutex to become available.

Note: Passing a negative number as the *timeout* is equivalent to calling :sip:ref:`~PyQt6.QtCore.QRecursiveMutex.lock`, i.e. this function will wait forever until mutex can be locked if *timeout* is negative.

If the lock was obtained, the mutex must be unlocked with :sip:ref:`~PyQt6.QtCore.QRecursiveMutex.unlock` before another thread can successfully lock it.

Calling this function multiple times on the same mutex from the same thread is allowed.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRecursiveMutex.lock`, :sip:ref:`~PyQt6.QtCore.QRecursiveMutex.unlock`.
