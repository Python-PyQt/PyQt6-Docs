.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: cd5bf6f2137096d41935af036d448a92

Attempts to forcefully remove an existing lock file.

Calling this is not recommended when protecting a short-lived operation: :sip:ref:`~PyQt6.QtCore.QLockFile` already takes care of removing lock files after they are older than :sip:ref:`~PyQt6.QtCore.QLockFile.staleLockTime`.

This method should only be called when protecting a resource for a long time, i.e. with :sip:ref:`~PyQt6.QtCore.QLockFile.staleLockTime`\ (0), and after :sip:ref:`~PyQt6.QtCore.QLockFile.tryLock` returned :sip:ref:`~PyQt6.QtCore.QLockFile.LockError.LockFailedError`, and the user agreed on removing the lock file.

Returns ``true`` on success, false if the lock file couldn't be removed. This happens on Windows, when the application owning the lock is still running.
