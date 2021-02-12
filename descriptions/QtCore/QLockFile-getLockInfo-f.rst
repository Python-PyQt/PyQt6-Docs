.. sip:method-description::
    :status: todo
    :pysig: 3560d6fdc813c7934c8f024d20b35a80
    :realsig: (qint64*,QString*,QString*) const
    :digest: 09c7e402d6a21e6ce42009e60689974f

Retrieves information about the current owner of the lock file.

If :sip:ref:`~PyQt6.QtCore.QLockFile.tryLock` returns ``false``, and :sip:ref:`~PyQt6.QtCore.QLockFile.error` returns :sip:ref:`~PyQt6.QtCore.QLockFile.LockError.LockFailedError`, this function can be called to find out more information about the existing lock file:

* the PID of the application (returned in *pid*)

* the *hostname* it's running on (useful in case of networked filesystems),

* the name of the application which created it (returned in *appname*),

Note that :sip:ref:`~PyQt6.QtCore.QLockFile.tryLock` automatically deleted the file if there is no running application with this PID, so :sip:ref:`~PyQt6.QtCore.QLockFile.LockError.LockFailedError` can only happen if there is an application with this PID (it could be unrelated though).

This can be used to inform users about the existing lock file and give them the choice to delete it. After removing the file using :sip:ref:`~PyQt6.QtCore.QLockFile.removeStaleLockFile`, the application can call :sip:ref:`~PyQt6.QtCore.QLockFile.tryLock` again.

This function returns ``true`` if the information could be successfully retrieved, false if the lock file doesn't exist or doesn't contain the expected data. This can happen if the lock file was deleted between the time where :sip:ref:`~PyQt6.QtCore.QLockFile.tryLock` failed and the call to this function. Simply call :sip:ref:`~PyQt6.QtCore.QLockFile.tryLock` again if this happens.
