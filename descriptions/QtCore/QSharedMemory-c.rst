.. sip:class-description::
    :status: todo
    :brief: Access to a shared memory segment
    :digest: 016a276c42cd807575c8a1c67b2ab077

The :sip:ref:`~PyQt6.QtCore.QSharedMemory` class provides access to a shared memory segment.

:sip:ref:`~PyQt6.QtCore.QSharedMemory` provides access to a shared memory segment by multiple threads and processes. It also provides a way for a single thread or process to lock the memory for exclusive access.

When using this class, be aware of the following platform differences:

* Windows: :sip:ref:`~PyQt6.QtCore.QSharedMemory` does not "own" the shared memory segment. When all threads or processes that have an instance of :sip:ref:`~PyQt6.QtCore.QSharedMemory` attached to a particular shared memory segment have either destroyed their instance of :sip:ref:`~PyQt6.QtCore.QSharedMemory` or exited, the Windows kernel releases the shared memory segment automatically.

* Unix: :sip:ref:`~PyQt6.QtCore.QSharedMemory` "owns" the shared memory segment. When the last thread or process that has an instance of :sip:ref:`~PyQt6.QtCore.QSharedMemory` attached to a particular shared memory segment detaches from the segment by destroying its instance of :sip:ref:`~PyQt6.QtCore.QSharedMemory`, the destructor releases the shared memory segment. But if that last thread or process crashes without running the :sip:ref:`~PyQt6.QtCore.QSharedMemory` destructor, the shared memory segment survives the crash.

* Unix: :sip:ref:`~PyQt6.QtCore.QSharedMemory` can be implemented by one of two different backends, selected at Qt build time: System V or POSIX. Qt defaults to using the System V API if it is available, and POSIX if not. These two backends do not interoperate, so two applications must ensure they use the same one, even if the native key (see :sip:ref:`~PyQt6.QtCore.QSharedMemory.setNativeKey`) is the same.

  The POSIX backend can be explicitly selected using the ``-feature-ipc_posix`` option to the Qt configure script. If it is enabled, the ``QT_POSIX_IPC`` macro will be defined.

* Sandboxed applications on Apple platforms (including apps shipped through the Apple App Store): This environment requires the use of POSIX shared memory (instead of System V shared memory).

  Qt for iOS is built with support for POSIX shared memory out of the box. However, Qt for macOS builds (including those from the Qt installer) default to System V, making them unsuitable for App Store submission if :sip:ref:`~PyQt6.QtCore.QSharedMemory` is needed. See above for instructions to explicitly select the POSIX backend when building Qt.

  In addition, in a sandboxed environment, the following caveats apply:

  * The key must be in the form ``<application group identifier>/<custom identifier>``, as documented `here <https://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/AppSandboxInDepth/AppSandboxInDepth.html#//apple_ref/doc/uid/TP40011183-CH3-SW24>`_ and `here <https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_application-groups>`_.

  * The key length is limited to 30 characters.

  * On process exit, the named shared memory entries are not cleaned up, so restarting the application and re-creating the shared memory under the same name will fail. To work around this, fall back to attaching to the existing shared memory entry:

    ::

        QSharedMemory shm("DEVTEAMID.app-group/shared");
        if (!shm.create(42) && shm.error() == QSharedMemory::AlreadyExists)
            shm.attach();

* Android: :sip:ref:`~PyQt6.QtCore.QSharedMemory` is not supported.

Remember to lock the shared memory with :sip:ref:`~PyQt6.QtCore.QSharedMemory.lock` before reading from or writing to the shared memory, and remember to release the lock with :sip:ref:`~PyQt6.QtCore.QSharedMemory.unlock` after you are done.

:sip:ref:`~PyQt6.QtCore.QSharedMemory` automatically destroys the shared memory segment when the last instance of :sip:ref:`~PyQt6.QtCore.QSharedMemory` is detached from the segment, and no references to the segment remain.

**Warning:** :sip:ref:`~PyQt6.QtCore.QSharedMemory` changes the key in a Qt-specific way, unless otherwise specified. Interoperation with non-Qt applications is achieved by first creating a default shared memory with :sip:ref:`~PyQt6.QtCore.QSharedMemory` and then setting a native key with :sip:ref:`~PyQt6.QtCore.QSharedMemory.setNativeKey`, after ensuring they use the same low-level API (System V or POSIX). When using native keys, shared memory is not protected against multiple accesses on it (for example, unable to :sip:ref:`~PyQt6.QtCore.QSharedMemory.lock`) and a user-defined mechanism should be used to achieve such protection.

.. _qsharedmemory-alternative-memory-mapped-file:

Alternative: Memory-Mapped File
...............................

Another way to share memory between processes is by opening the same file using :sip:ref:`~PyQt6.QtCore.QFile` and mapping it into memory using QFile::map() (without specifying the :sip:ref:`~PyQt6.QtCore.QFileDevice.MemoryMapFlag.MapPrivateOption` option). Any writes to the mapped segment will be observed by all other processes that have mapped the same file. This solution has the major advantages of being independent of the backend API and of being simpler to interoperate with from non-Qt applications. And since :sip:ref:`~PyQt6.QtCore.QTemporaryFile` is a :sip:ref:`~PyQt6.QtCore.QFile`, applications can use that class to achieve clean-up semantics and to create unique shared memory segments too.

To achieve locking of the shared memory segment, applications will need to deploy their own mechanisms. This can be achieved by using QBasicAtomicInteger or ``std::atomic`` in a pre-determined offset in the segment itself. Higher-level locking primitives may be available on some operating systems; for example, on Linux, ``pthread_mutex_create()`` can be passed a flag to indicate that the mutex resides in a shared memory segment.

A major drawback of using file-backed shared memory is that the operating system will attempt to write the data to permanent storage, possibly causing noticeable performance penalties. To avoid this, applications should locate a RAM-backed filesystem, such as ``tmpfs`` on Linux (see :sip:ref:`~PyQt6.QtCore.QStorageInfo.fileSystemType`), or pass a flag to the native file-opening function to inform the OS to avoid committing the contents to storage.

File-backed shared memory must be used with care if another process participating is untrusted. The files may be truncated/shrunk and cause applications accessing memory beyond the file's size to crash.

.. _qsharedmemory-linux-hints-on-memory-mapped-files:

Linux hints on memory-mapped files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On modern Linux systems, while the ``/tmp`` directory is often a ``tmpfs`` mount point, that is not a requirement. However, the ``/dev/shm`` directory is required to be a ``tmpfs`` and exists for this very purpose. Do note that it is world-readable and writable (like ``/tmp`` and ``/var/tmp``), so one must be careful of the contents revealed there. Another alternative is to use the XDG Runtime Directory (see :sip:ref:`~PyQt6.QtCore.QStandardPaths.writableLocation` and :sip:ref:`~PyQt6.QtCore.QStandardPaths.StandardLocation.RuntimeLocation`), which on Linux systems using systemd is a user-specific ``tmpfs``.

An even more secure solution is to create a "memfd" using ``memfd_create(2)`` and use interprocess communication to pass the file descriptor, like :sip:ref:`~PyQt6.QtDBus.QDBusUnixFileDescriptor` or by letting the child process of a :sip:ref:`~PyQt6.QtCore.QProcess` inherit it. "memfds" can also be sealed against being shrunk, so they are safe to be used when communicating with processes with a different privilege level.

.. _qsharedmemory-freebsd-hints-on-memory-mapped-files:

FreeBSD hints on memory-mapped files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

FreeBSD also has ``memfd_create(2)`` and can pass file descriptors to other processes using the same techniques as Linux. It does not have temporary filesystems mounted by default.

.. _qsharedmemory-windows-hints-on-memory-mapped-files:

Windows hints on memory-mapped files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On Windows, the application can request the operating system avoid committing the file's contents to permanent storage. This request is performed by passing the ``FILE_ATTRIBUTE_TEMPORARY`` flag in the ``dwFlagsAndAttributes`` ``CreateFile`` Win32 function, the ``_O_SHORT_LIVED`` flag to ``_open()`` low-level function, or by including the modifier "T" to the ``fopen()`` C runtime function.

There's also a flag to inform the operating system to delete the file when the last handle to it is closed (``FILE_FLAG_DELETE_ON_CLOSE``, ``_O_TEMPORARY``, and the "D" modifier), but do note that all processes attempting to open the file must agree on using this flag or not using it. A mismatch will likely cause a sharing violation and failure to open the file.
