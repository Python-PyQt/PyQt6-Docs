.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: e9b3f85ec5640ee1a0bdf0ecf7f064cd

Creates the lock file.

If another process (or another thread) has created the lock file already, this function will block until that process (or thread) releases it.

Calling this function multiple times on the same lock from the same thread without unlocking first is not allowed. This function will *dead-lock* when the file is locked recursively.

Returns ``true`` if the lock was acquired, false if it could not be acquired due to an unrecoverable error, such as no permissions in the parent directory.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLockFile.unlock`, :sip:ref:`~PyQt6.QtCore.QLockFile.tryLock`.
