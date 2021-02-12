.. sip:method-description::
    :status: todo
    :pysig: 382b2a2aedb37045cd9d00f29ea9f95e
    :realsig: (int)
    :digest: 7b6e5972ace3f77c4a6cfd7a3d5b0903

Attempts to create the lock file. This function returns ``true`` if the lock was obtained; otherwise it returns ``false``. If another process (or another thread) has created the lock file already, this function will wait for at most *timeout* milliseconds for the lock file to become available.

Note: Passing a negative number as the *timeout* is equivalent to calling :sip:ref:`~PyQt6.QtCore.QLockFile.lock`, i.e. this function will wait forever until the lock file can be locked if *timeout* is negative.

If the lock was obtained, it must be released with :sip:ref:`~PyQt6.QtCore.QLockFile.unlock` before another process (or thread) can successfully lock it.

Calling this function multiple times on the same lock from the same thread without unlocking first is not allowed, this function will *always* return false when attempting to lock the file recursively.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLockFile.lock`, :sip:ref:`~PyQt6.QtCore.QLockFile.unlock`.
