.. sip:method-description::
    :status: todo
    :pysig: 47bc384ef78158df7bdc68df0f06aef9
    :realsig: (int)
    :digest: b1b2436828add72342018ca25b76017a

Attempts to lock the mutex. This function returns ``true`` if the lock was obtained; otherwise it returns ``false``. If another thread has locked the mutex, this function will wait for at most *timeout* milliseconds for the mutex to become available.

Note: Passing a negative number as the *timeout* is equivalent to calling :sip:ref:`~PyQt6.QtCore.QMutex.lock`, i.e. this function will wait forever until mutex can be locked if *timeout* is negative.

If the lock was obtained, the mutex must be unlocked with :sip:ref:`~PyQt6.QtCore.QMutex.unlock` before another thread can successfully lock it.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMutex.lock`, :sip:ref:`~PyQt6.QtCore.QMutex.unlock`.
