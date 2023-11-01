.. sip:class-description::
    :status: todo
    :brief: Access to a shared memory segment
    :digest: 54abf8d56c7b78ed76bc6443e0432a16

The :sip:ref:`~PyQt6.QtCore.QSharedMemory` class provides access to a shared memory segment.

:sip:ref:`~PyQt6.QtCore.QSharedMemory` provides access to a `shared memory segment <https://doc.qt.io/qt-6/shared-memory.html>`_ by multiple threads and processes. Shared memory segments are identified by a key, represented by :sip:ref:`~PyQt6.QtCore.QNativeIpcKey`. A key can be created in a cross-platform manner by using platformSafeKey().

One :sip:ref:`~PyQt6.QtCore.QSharedMemory` object must :sip:ref:`~PyQt6.QtCore.QSharedMemory.create` the segment and this call specifies the size of the segment. All other processes simply :sip:ref:`~PyQt6.QtCore.QSharedMemory.attach` to the segment that must already exist. After either operation is successful, the application may call :sip:ref:`~PyQt6.QtCore.QSharedMemory.data` to obtain a pointer to the data.

To support non-atomic operations, :sip:ref:`~PyQt6.QtCore.QSharedMemory` provides API to gain exclusive access: you may lock the shared memory with :sip:ref:`~PyQt6.QtCore.QSharedMemory.lock` before reading from or writing to the shared memory, but remember to release the lock with :sip:ref:`~PyQt6.QtCore.QSharedMemory.unlock` after you are done.

By default, :sip:ref:`~PyQt6.QtCore.QSharedMemory` automatically destroys the shared memory segment when the last instance of :sip:ref:`~PyQt6.QtCore.QSharedMemory` is :sip:ref:`~PyQt6.QtCore.QSharedMemory.detach` from the segment, and no references to the segment remain.

For details on the key types, platform-specific limitations, and interoperability with older or non-Qt applications, see the `Native IPC Keys <https://doc.qt.io/qt-6/native-ipc-keys.html>`_ documentation. That includes important information for sandboxed applications on Apple platforms, including all apps obtained via the Apple App Store.

.. seealso:: `Inter-Process Communication <https://doc.qt.io/qt-6/ipc.html>`_, :sip:ref:`~PyQt6.QtCore.QSystemSemaphore`.
