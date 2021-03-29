.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 0d5cf5efe5d1ba01977788b95eab5c8f

Acquires one of the resources guarded by this semaphore, if there is one available, and returns ``true``. If all the resources guarded by this semaphore have already been acquired, the call blocks until one of them is released by another process or thread having a semaphore with the same key.

If false is returned, a system error has occurred. Call :sip:ref:`~PyQt6.QtCore.QSystemSemaphore.error` to get a value of :sip:ref:`~PyQt6.QtCore.QSystemSemaphore.SystemSemaphoreError` that indicates which error occurred.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSystemSemaphore.release`.
