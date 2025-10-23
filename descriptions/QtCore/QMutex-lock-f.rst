.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: de27c36e7e90157c5f823c19b4e8f784

Locks the mutex. If another thread has locked the mutex then this call will block until that thread has unlocked it.

If the mutex was already locked by the current thread, this call will never return, causing a *dead-lock*.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMutex.unlock`.
