.. sip:class-description::
    :status: todo
    :brief: Access to a shared memory segment
    :digest: e1ecea39c31c71c41850812e239dd730

The :sip:ref:`~PyQt6.QtCore.QSharedMemory` class provides access to a shared memory segment.

:sip:ref:`~PyQt6.QtCore.QSharedMemory` provides access to a shared memory segment by multiple threads and processes. It also provides a way for a single thread or process to lock the memory for exclusive access.

When using this class, be aware of the following platform differences:

* Windows: :sip:ref:`~PyQt6.QtCore.QSharedMemory` does not "own" the shared memory segment. When all threads or processes that have an instance of :sip:ref:`~PyQt6.QtCore.QSharedMemory` attached to a particular shared memory segment have either destroyed their instance of :sip:ref:`~PyQt6.QtCore.QSharedMemory` or exited, the Windows kernel releases the shared memory segment automatically.

* Unix: :sip:ref:`~PyQt6.QtCore.QSharedMemory` "owns" the shared memory segment. When the last thread or process that has an instance of :sip:ref:`~PyQt6.QtCore.QSharedMemory` attached to a particular shared memory segment detaches from the segment by destroying its instance of :sip:ref:`~PyQt6.QtCore.QSharedMemory`, the Unix kernel release the shared memory segment. But if that last thread or process crashes without running the :sip:ref:`~PyQt6.QtCore.QSharedMemory` destructor, the shared memory segment survives the crash.

* HP-UX: Only one attach to a shared memory segment is allowed per process. This means that :sip:ref:`~PyQt6.QtCore.QSharedMemory` should not be used across multiple threads in the same process in HP-UX.

* Apple platforms: Sandboxed applications (including apps shipped through the Apple App Store) require the use of POSIX shared memory (instead of System V shared memory), which adds a number of limitations, including:

  * The key must be in the form ``<application group identifier>/<custom identifier>``, as documented `here <https://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/AppSandboxInDepth/AppSandboxInDepth.html#//apple_ref/doc/uid/TP40011183-CH3-SW24>`_ and `here <https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_application-groups>`_.

  * The key length is limited to 30 characters.

  * On process exit, the named shared memory entries are not cleaned up, so restarting the application and re-creating the shared memory under the same name will fail. To work around this, fall back to attaching to the existing shared memory entry:

    ::

        QSharedMemory shm("DEVTEAMID.app-group/shared");
        if (!shm.create(42) && shm.error() == QSharedMemory::AlreadyExists)
            shm.attach();

Remember to lock the shared memory with :sip:ref:`~PyQt6.QtCore.QSharedMemory.lock` before reading from or writing to the shared memory, and remember to release the lock with :sip:ref:`~PyQt6.QtCore.QSharedMemory.unlock` after you are done.

:sip:ref:`~PyQt6.QtCore.QSharedMemory` automatically destroys the shared memory segment when the last instance of :sip:ref:`~PyQt6.QtCore.QSharedMemory` is detached from the segment, and no references to the segment remain.

**Warning:** :sip:ref:`~PyQt6.QtCore.QSharedMemory` changes the key in a Qt-specific way, unless otherwise specified. Interoperation with non-Qt applications is achieved by first creating a default shared memory with :sip:ref:`~PyQt6.QtCore.QSharedMemory` and then setting a native key with :sip:ref:`~PyQt6.QtCore.QSharedMemory.setNativeKey`. When using native keys, shared memory is not protected against multiple accesses on it (for example, unable to :sip:ref:`~PyQt6.QtCore.QSharedMemory.lock`) and a user-defined mechanism should be used to achieve such protection.
