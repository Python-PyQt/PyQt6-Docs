.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 101941e995d3ad1ad12c352af059b24f

Attempts to lock the mutex. This function returns ``true`` if the lock was obtained; otherwise it returns ``false``.

If the lock was obtained, the mutex must be unlocked with :sip:ref:`~PyQt6.QtCore.QMutex.unlock` before another thread can successfully lock it.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMutex.lock`, :sip:ref:`~PyQt6.QtCore.QMutex.unlock`.
