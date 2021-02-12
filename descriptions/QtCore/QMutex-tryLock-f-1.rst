.. sip:method-description::
    :status: todo
    :pysig: 47bc384ef78158df7bdc68df0f06aef9
    :realsig: (int)
    :digest: f2a378516b731747c1dbf395ac5db6ea

Attempts to lock the mutex. This function returns ``true`` if the lock was obtained; otherwise it returns ``false``. If another thread has locked the mutex, this function will wait for at most *timeout* milliseconds for the mutex to become available.

Note: Passing a negative number as the *timeout* is equivalent to calling :sip:ref:`~PyQt6.QtCore.QMutex.lock`, i.e. this function will wait forever until mutex can be locked if *timeout* is negative.

If the lock was obtained, the mutex must be unlocked with :sip:ref:`~PyQt6.QtCore.QMutex.unlock` before another thread can successfully lock it.

Calling this function multiple times on the same mutex from the same thread will cause a *dead-lock*.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMutex.lock`, :sip:ref:`~PyQt6.QtCore.QMutex.unlock`.
