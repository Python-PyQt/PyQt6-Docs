.. sip:method-description::
    :status: todo
    :pysig: 4c3a752d95ed5d317c790e03e77c13da
    :realsig: (const QNativeIpcKey&, int, QSystemSemaphore::AccessMode)
    :digest: e0cf4623b7f7fb9839ff296d7dc866f4

This function works the same as the constructor. It reconstructs this :sip:ref:`~PyQt6.QtCore.QSystemSemaphore` object. If the new *key* is different from the old key, calling this function is like calling the destructor of the semaphore with the old key, then calling the constructor to create a new semaphore with the new *key*. The *initialValue* and *mode* parameters are as defined for the constructor.

This function is useful if the native key was shared from another process. See `Native IPC Keys <https://doc.qt.io/qt-6/native-ipc-keys.html>`_ for more information.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSystemSemaphore`, :sip:ref:`~PyQt6.QtCore.QSystemSemaphore.nativeIpcKey`.
