.. sip:class-description::
    :status: todo
    :brief: General counting semaphore
    :digest: 146291c0f1b5c8e2ac07ec563bbdf2f5

The :sip:ref:`~PyQt6.QtCore.QSemaphore` class provides a general counting semaphore.

A semaphore is a generalization of a mutex. While a mutex can only be locked once, it's possible to acquire a semaphore multiple times. Semaphores are typically used to protect a certain number of identical resources.

Semaphores support two fundamental operations, :sip:ref:`~PyQt6.QtCore.QSemaphore.acquire` and :sip:ref:`~PyQt6.QtCore.QSemaphore.release`:

* acquire(\ *n*) tries to acquire *n* resources. If there aren't that many resources available, the call will block until this is the case.

* release(\ *n*) releases *n* resources.

There's also a :sip:ref:`~PyQt6.QtCore.QSemaphore.tryAcquire` function that returns immediately if it cannot acquire the resources, and an :sip:ref:`~PyQt6.QtCore.QSemaphore.available` function that returns the number of available resources at any time.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_thread_qsemaphore.py
    :lines: 54-62

A typical application of semaphores is for controlling access to a circular buffer shared by a producer thread and a consumer thread. The `Semaphores Example <https://doc.qt.io/qt-6/qtcore-threads-semaphores-example.html>`_ shows how to use :sip:ref:`~PyQt6.QtCore.QSemaphore` to solve that problem.

A non-computing example of a semaphore would be dining at a restaurant. A semaphore is initialized with the number of chairs in the restaurant. As people arrive, they want a seat. As seats are filled, :sip:ref:`~PyQt6.QtCore.QSemaphore.available` is decremented. As people leave, the :sip:ref:`~PyQt6.QtCore.QSemaphore.available` is incremented, allowing more people to enter. If a party of 10 people want to be seated, but there are only 9 seats, those 10 people will wait, but a party of 4 people would be seated (taking the available seats to 5, making the party of 10 people wait longer).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSemaphoreReleaser`, :sip:ref:`~PyQt6.QtCore.QMutex`, :sip:ref:`~PyQt6.QtCore.QWaitCondition`, :sip:ref:`~PyQt6.QtCore.QThread`, `Semaphores Example <https://doc.qt.io/qt-6/qtcore-threads-semaphores-example.html>`_.
