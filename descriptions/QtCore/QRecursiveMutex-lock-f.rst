.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 466b24b4bcb356c830a00d35924d595b

Locks the mutex. If another thread has locked the mutex then this call will block until that thread has unlocked it.

Calling this function multiple times on the same mutex from the same thread is allowed.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRecursiveMutex.unlock`.
