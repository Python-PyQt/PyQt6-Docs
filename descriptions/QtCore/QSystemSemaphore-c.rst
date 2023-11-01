.. sip:class-description::
    :status: todo
    :brief: General counting system semaphore
    :digest: 94f2505d58165b123fc27730668e72de

The :sip:ref:`~PyQt6.QtCore.QSystemSemaphore` class provides a general counting system semaphore.

A system semaphore is a generalization of :sip:ref:`~PyQt6.QtCore.QSemaphore`. Typically, a semaphore is used to protect a certain number of identical resources.

Like its lighter counterpart, a :sip:ref:`~PyQt6.QtCore.QSystemSemaphore` can be accessed from multiple :sip:ref:`~PyQt6.QtCore.QThread`. Unlike :sip:ref:`~PyQt6.QtCore.QSemaphore`, a :sip:ref:`~PyQt6.QtCore.QSystemSemaphore` can also be accessed from multiple :sip:ref:`~PyQt6.QtCore.QProcess`. This means :sip:ref:`~PyQt6.QtCore.QSystemSemaphore` is a much heavier class, so if your application doesn't need to access your semaphores across multiple processes, you will probably want to use :sip:ref:`~PyQt6.QtCore.QSemaphore`.

Semaphores support two fundamental operations, :sip:ref:`~PyQt6.QtCore.QSystemSemaphore.acquire` and :sip:ref:`~PyQt6.QtCore.QSystemSemaphore.release`:

:sip:ref:`~PyQt6.QtCore.QSystemSemaphore.acquire` tries to acquire one resource. If there isn't a resource available, the call blocks until a resource becomes available. Then the resource is acquired and the call returns.

:sip:ref:`~PyQt6.QtCore.QSystemSemaphore.release` releases one resource so it can be acquired by another process. The function can also be called with a parameter n > 1, which releases n resources.

System semaphores are identified by a key, represented by :sip:ref:`~PyQt6.QtCore.QNativeIpcKey`. A key can be created in a cross-platform manner by using platformSafeKey(). A system semaphore is created by the :sip:ref:`~PyQt6.QtCore.QSystemSemaphore` constructor when passed an access mode parameter of AccessMode::Create. Once it is created, other processes may attach to the same semaphore using the same key and an access mode parameter of AccessMode::Open.

Example: Create a system semaphore

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qsystemsemaphore.py
    :lines: 54-60

For details on the key types, platform-specific limitations, and interoperability with older or non-Qt applications, see the `Native IPC Keys <https://doc.qt.io/qt-6/native-ipc-keys.html>`_ documentation. That includes important information for sandboxed applications on Apple platforms, including all apps obtained via the Apple App Store.

.. seealso:: `Inter-Process Communication <https://doc.qt.io/qt-6/ipc.html>`_, :sip:ref:`~PyQt6.QtCore.QSharedMemory`, :sip:ref:`~PyQt6.QtCore.QSemaphore`.
