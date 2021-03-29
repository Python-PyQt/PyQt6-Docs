.. sip:method-description::
    :status: todo
    :pysig: ba95021d0047096d6c0be78658074098
    :realsig: (const QString&,int,QSystemSemaphore::AccessMode)
    :digest: 3a46163283967a43521d272c53bb923f

Requests a system semaphore for the specified *key*. The parameters *initialValue* and *mode* are used according to the following rules, which are system dependent.

In Unix, if the *mode* is :sip:ref:`~PyQt6.QtCore.QSystemSemaphore.AccessMode.Open` and the system already has a semaphore identified by *key*, that semaphore is used, and the semaphore's resource count is not changed, i.e., *initialValue* is ignored. But if the system does not already have a semaphore identified by *key*, it creates a new semaphore for that key and sets its resource count to *initialValue*.

In Unix, if the *mode* is :sip:ref:`~PyQt6.QtCore.QSystemSemaphore.AccessMode.Create` and the system already has a semaphore identified by *key*, that semaphore is used, and its resource count is set to *initialValue*. If the system does not already have a semaphore identified by *key*, it creates a new semaphore for that key and sets its resource count to *initialValue*.

In Windows, *mode* is ignored, and the system always tries to create a semaphore for the specified *key*. If the system does not already have a semaphore identified as *key*, it creates the semaphore and sets its resource count to *initialValue*. But if the system already has a semaphore identified as *key* it uses that semaphore and ignores *initialValue*.

The :sip:ref:`~PyQt6.QtCore.QSystemSemaphore.AccessMode` parameter is only used in Unix systems to handle the case where a semaphore survives a process crash. In that case, the next process to allocate a semaphore with the same *key* will get the semaphore that survived the crash, and unless *mode* is :sip:ref:`~PyQt6.QtCore.QSystemSemaphore.AccessMode.Create`, the resource count will not be reset to *initialValue* but will retain the initial value it had been given by the crashed process.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSystemSemaphore.acquire`, :sip:ref:`~PyQt6.QtCore.QSystemSemaphore.key`.
