.. sip:class-description::
    :status: todo
    :brief: General counting system semaphore
    :digest: 803110c7b34ef044fa784f53cc7be4d2

The :sip:ref:`~PyQt6.QtCore.QSystemSemaphore` class provides a general counting system semaphore.

A semaphore is a generalization of a mutex. While a mutex can be locked only once, a semaphore can be acquired multiple times. Typically, a semaphore is used to protect a certain number of identical resources.

Like its lighter counterpart :sip:ref:`~PyQt6.QtCore.QSemaphore`, a :sip:ref:`~PyQt6.QtCore.QSystemSemaphore` can be accessed from multiple :sip:ref:`~PyQt6.QtCore.QThread`. Unlike :sip:ref:`~PyQt6.QtCore.QSemaphore`, a :sip:ref:`~PyQt6.QtCore.QSystemSemaphore` can also be accessed from multiple `processes <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_. This means :sip:ref:`~PyQt6.QtCore.QSystemSemaphore` is a much heavier class, so if your application doesn't need to access your semaphores across multiple processes, you will probably want to use :sip:ref:`~PyQt6.QtCore.QSemaphore`.

Semaphores support two fundamental operations, :sip:ref:`~PyQt6.QtCore.QSystemSemaphore.acquire` and :sip:ref:`~PyQt6.QtCore.QSystemSemaphore.release`:

:sip:ref:`~PyQt6.QtCore.QSystemSemaphore.acquire` tries to acquire one resource. If there isn't a resource available, the call blocks until a resource becomes available. Then the resource is acquired and the call returns.

:sip:ref:`~PyQt6.QtCore.QSystemSemaphore.release` releases one resource so it can be acquired by another process. The function can also be called with a parameter n > 1, which releases n resources.

A system semaphore is created with a string key that other processes can use to use the same semaphore.

Example: Create a system semaphore

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qsystemsemaphore.py
    :lines: 54-60

A typical application of system semaphores is for controlling access to a circular buffer shared by a producer process and a consumer processes.

.. _qsystemsemaphore-platform-specific-behavior:

Platform-Specific Behavior
--------------------------

When using this class, be aware of the following platform differences:

**Windows:** :sip:ref:`~PyQt6.QtCore.QSystemSemaphore` does not own its underlying system semaphore. Windows owns it. This means that when all instances of :sip:ref:`~PyQt6.QtCore.QSystemSemaphore` for a particular key have been destroyed, either by having their destructors called, or because one or more processes crash, Windows removes the underlying system semaphore.

**Unix:**

* :sip:ref:`~PyQt6.QtCore.QSystemSemaphore` owns the underlying system semaphore in Unix systems. This means that the last process having an instance of :sip:ref:`~PyQt6.QtCore.QSystemSemaphore` for a particular key must remove the underlying system semaphore in its destructor. If the last process crashes without running the :sip:ref:`~PyQt6.QtCore.QSystemSemaphore` destructor, Unix does not automatically remove the underlying system semaphore, and the semaphore survives the crash. A subsequent process that constructs a :sip:ref:`~PyQt6.QtCore.QSystemSemaphore` with the same key will then be given the existing system semaphore. In that case, if the :sip:ref:`~PyQt6.QtCore.QSystemSemaphore` constructor has specified its :sip:ref:`~PyQt6.QtCore.QSystemSemaphore.AccessMode` as :sip:ref:`~PyQt6.QtCore.QSystemSemaphore.AccessMode.Open`, its initial resource count will not be reset to the one provided but remain set to the value it received in the crashed process. To protect against this, the first process to create a semaphore for a particular key (usually a server), must pass its :sip:ref:`~PyQt6.QtCore.QSystemSemaphore.AccessMode` as :sip:ref:`~PyQt6.QtCore.QSystemSemaphore.AccessMode.Create`, which will force Unix to reset the resource count in the underlying system semaphore.

* When a process using :sip:ref:`~PyQt6.QtCore.QSystemSemaphore` terminates for any reason, Unix automatically reverses the effect of all acquire operations that were not released. Thus if the process acquires a resource and then exits without releasing it, Unix will release that resource.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSharedMemory`, :sip:ref:`~PyQt6.QtCore.QSemaphore`.
