.. sip:class-description::
    :status: todo
    :brief: Access serialization between threads
    :digest: b404297ca65c5dd4f644fc67e915e95d

The :sip:ref:`~PyQt6.QtCore.QRecursiveMutex` class provides access serialization between threads.

The :sip:ref:`~PyQt6.QtCore.QRecursiveMutex` class is a mutex, like :sip:ref:`~PyQt6.QtCore.QMutex`, with which it is API-compatible. It differs from :sip:ref:`~PyQt6.QtCore.QMutex` by accepting :sip:ref:`~PyQt6.QtCore.QRecursiveMutex.lock` calls from the same thread any number of times. :sip:ref:`~PyQt6.QtCore.QMutex` would deadlock in this situation.

:sip:ref:`~PyQt6.QtCore.QRecursiveMutex` is much more expensive to construct and operate on, so use a plain :sip:ref:`~PyQt6.QtCore.QMutex` whenever you can. Sometimes, one public function, however, calls another public function, and they both need to lock the same mutex. In this case, you have two options:

* Factor the code that needs mutex protection into private functions, which assume that the mutex is held when they are called, and lock a plain :sip:ref:`~PyQt6.QtCore.QMutex` in the public functions before you call the private implementation ones.

* Or use a recursive mutex, so it doesn't matter that the first public function has already locked the mutex when the second one wishes to do so.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMutex`, QMutexLocker, :sip:ref:`~PyQt6.QtCore.QReadWriteLock`, :sip:ref:`~PyQt6.QtCore.QSemaphore`, :sip:ref:`~PyQt6.QtCore.QWaitCondition`.
