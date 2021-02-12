.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: ef5a7a86f555810e75cea204eb245c9e

Locks the mutex. If another thread has locked the mutex then this call will block until that thread has unlocked it.

Calling this function multiple times on the same mutex from the same thread will cause a *dead-lock*.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMutex.unlock`.
