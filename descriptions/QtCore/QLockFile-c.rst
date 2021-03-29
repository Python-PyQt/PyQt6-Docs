.. sip:class-description::
    :status: todo
    :brief: Locking between processes using a file
    :digest: 3fad97a9a6e60b3df9c90bca91685cfc

The :sip:ref:`~PyQt6.QtCore.QLockFile` class provides locking between processes using a file.

A lock file can be used to prevent multiple processes from accessing concurrently the same resource. For instance, a configuration file on disk, or a socket, a port, a region of shared memory...

Serialization is only guaranteed if all processes that access the shared resource use :sip:ref:`~PyQt6.QtCore.QLockFile`, with the same file path.

:sip:ref:`~PyQt6.QtCore.QLockFile` supports two use cases: to protect a resource for a short-term operation (e.g. verifying if a configuration file has changed before saving new settings), and for long-lived protection of a resource (e.g. a document opened by a user in an editor) for an indefinite amount of time.

When protecting for a short-term operation, it is acceptable to call :sip:ref:`~PyQt6.QtCore.QLockFile.lock` and wait until any running operation finishes. When protecting a resource over a long time, however, the application should always call :sip:ref:`~PyQt6.QtCore.QLockFile.setStaleLockTime`\ (0) and then :sip:ref:`~PyQt6.QtCore.QLockFile.tryLock` with a short timeout, in order to warn the user that the resource is locked.

If the process holding the lock crashes, the lock file stays on disk and can prevent any other process from accessing the shared resource, ever. For this reason, :sip:ref:`~PyQt6.QtCore.QLockFile` tries to detect such a "stale" lock file, based on the process ID written into the file. To cover the situation that the process ID got reused meanwhile, the current process name is compared to the name of the process that corresponds to the process ID from the lock file. If the process names differ, the lock file is considered stale. Additionally, the last modification time of the lock file (30s by default, for the use case of a short-lived operation) is taken into account. If the lock file is found to be stale, it will be deleted.

For the use case of protecting a resource over a long time, you should therefore call :sip:ref:`~PyQt6.QtCore.QLockFile.setStaleLockTime`\ (0), and when :sip:ref:`~PyQt6.QtCore.QLockFile.tryLock` returns :sip:ref:`~PyQt6.QtCore.QLockFile.LockError.LockFailedError`, inform the user that the document is locked, possibly using :sip:ref:`~PyQt6.QtCore.QLockFile.getLockInfo` for more details.

**Note:** On Windows, this class has problems detecting a stale lock if the machine's hostname contains characters outside the US-ASCII character set.
