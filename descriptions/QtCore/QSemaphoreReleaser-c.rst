.. sip:class-description::
    :status: todo
    :brief: Exception-safe deferral of a QSemaphore::release() call
    :digest: 85186ca8fb47fd8240e28499f711375a

The :sip:ref:`~PyQt6.QtCore.QSemaphoreReleaser` class provides exception-safe deferral of a :sip:ref:`~PyQt6.QtCore.QSemaphore.release` call.

:sip:ref:`~PyQt6.QtCore.QSemaphoreReleaser` can be used wherever you would otherwise use :sip:ref:`~PyQt6.QtCore.QSemaphore.release`. Constructing a :sip:ref:`~PyQt6.QtCore.QSemaphoreReleaser` defers the release() call on the semaphore until the :sip:ref:`~PyQt6.QtCore.QSemaphoreReleaser` is destroyed (see `RAII pattern <http://en.cppreference.com/w/cpp/language/raii>`_).

You can use this to reliably release a semaphore to avoid dead-lock in the face of exceptions or early returns:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_thread_qsemaphore.py
    :lines: 88-89

If an early return is taken or an exception is thrown before the ``sem.release()`` call is reached, the semaphore is not released, possibly preventing the thread waiting in the corresponding ``sem.acquire()`` call from ever continuing execution.

When using RAII instead:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_thread_qsemaphore.py
    :lines: 93-95

this can no longer happen, because the compiler will make sure that the :sip:ref:`~PyQt6.QtCore.QSemaphoreReleaser` destructor is always called, and therefore the semaphore is always released.

:sip:ref:`~PyQt6.QtCore.QSemaphoreReleaser` is move-enabled and can therefore be returned from functions to transfer responsibility for releasing a semaphore out of a function or a scope:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_thread_qsemaphore.py
    :lines: 99-107

A :sip:ref:`~PyQt6.QtCore.QSemaphoreReleaser` can be canceled by a call to :sip:ref:`~PyQt6.QtCore.QSemaphoreReleaser.cancel`. A canceled semaphore releaser will no longer call :sip:ref:`~PyQt6.QtCore.QSemaphore.release` in its destructor.

.. seealso:: QMutexLocker.
