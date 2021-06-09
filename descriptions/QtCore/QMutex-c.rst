.. sip:class-description::
    :status: todo
    :brief: Access serialization between threads
    :digest: cd9d12f11c85e7e5562228550dfaedfc

The :sip:ref:`~PyQt6.QtCore.QMutex` class provides access serialization between threads.

The purpose of a :sip:ref:`~PyQt6.QtCore.QMutex` is to protect an object, data structure or section of code so that only one thread can access it at a time (this is similar to the Java ``synchronized`` keyword). It is usually best to use a mutex with a QMutexLocker since this makes it easy to ensure that locking and unlocking are performed consistently.

For example, say there is a method that prints a message to the user on two lines:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_thread_qmutex.py
    :lines: 54-66

If these two methods are called in succession, the following happens:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_thread_qmutex.py
    :lines: 71-77

If these two methods are called simultaneously from two threads then the following sequence could result:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_thread_qmutex.py
    :lines: 82-93

If we add a mutex, we should get the result we want:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_thread_qmutex.py
    :lines: 98-115

Then only one thread can modify ``number`` at any given time and the result is correct. This is a trivial example, of course, but applies to any other case where things need to happen in a particular sequence.

When you call :sip:ref:`~PyQt6.QtCore.QMutex.lock` in a thread, other threads that try to call :sip:ref:`~PyQt6.QtCore.QMutex.lock` in the same place will block until the thread that got the lock calls :sip:ref:`~PyQt6.QtCore.QMutex.unlock`. A non-blocking alternative to :sip:ref:`~PyQt6.QtCore.QMutex.lock` is :sip:ref:`~PyQt6.QtCore.QMutex.tryLock`.

:sip:ref:`~PyQt6.QtCore.QMutex` is optimized to be fast in the non-contended case. It will not allocate memory if there is no contention on that mutex. It is constructed and destroyed with almost no overhead, which means it is fine to have many mutexes as part of other classes.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRecursiveMutex`, QMutexLocker, :sip:ref:`~PyQt6.QtCore.QReadWriteLock`, :sip:ref:`~PyQt6.QtCore.QSemaphore`, :sip:ref:`~PyQt6.QtCore.QWaitCondition`.
