.. sip:method-description::
    :status: todo
    :pysig: ba95021d0047096d6c0be78658074098
    :realsig: (const QString&,int,QSystemSemaphore::AccessMode)
    :digest: 5afbedb9fe0d4d7544d7bf2ae056efb5

This function works the same as the constructor. It reconstructs this :sip:ref:`~PyQt6.QtCore.QSystemSemaphore` object. If the new *key* is different from the old key, calling this function is like calling the destructor of the semaphore with the old key, then calling the constructor to create a new semaphore with the new *key*. The *initialValue* and *mode* parameters are as defined for the constructor.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSystemSemaphore`, :sip:ref:`~PyQt6.QtCore.QSystemSemaphore.key`.
