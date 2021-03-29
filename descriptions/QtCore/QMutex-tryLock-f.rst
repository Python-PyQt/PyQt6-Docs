.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 1700bacb8a19d8bf2f6901dff6afb0fb

This is an overloaded function.

Attempts to lock the mutex. This function returns ``true`` if the lock was obtained; otherwise it returns ``false``.

If the lock was obtained, the mutex must be unlocked with :sip:ref:`~PyQt6.QtCore.QMutex.unlock` before another thread can successfully lock it.

Calling this function multiple times on the same mutex from the same thread will cause a *dead-lock*.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMutex.lock`, :sip:ref:`~PyQt6.QtCore.QMutex.unlock`.
