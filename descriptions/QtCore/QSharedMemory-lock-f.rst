.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: b5d0c2474de906c5168da151c3c9bd88

This is a semaphore that locks the shared memory segment for access by this process and returns ``true``. If another process has locked the segment, this function blocks until the lock is released. Then it acquires the lock and returns ``true``. If this function returns ``false``, it means that you have ignored a false return from :sip:ref:`~PyQt6.QtCore.QSharedMemory.create` or :sip:ref:`~PyQt6.QtCore.QSharedMemory.attach`, that you have set the key with :sip:ref:`~PyQt6.QtCore.QSharedMemory.setNativeKey` or that :sip:ref:`~PyQt6.QtCore.QSystemSemaphore.acquire` failed due to an unknown system error.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSharedMemory.unlock`, :sip:ref:`~PyQt6.QtCore.QSharedMemory.data`, :sip:ref:`~PyQt6.QtCore.QSystemSemaphore.acquire`.
