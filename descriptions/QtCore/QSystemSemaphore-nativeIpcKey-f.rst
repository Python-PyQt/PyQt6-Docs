.. sip:method-description::
    :status: todo
    :pysig: 66883c67b8346c29659446e444062f18
    :realsig: () const
    :digest: d8a65f1560128243b524ba6e6a73ba90

Returns the key assigned to this system semaphore. The key is the name by which the semaphore can be accessed from other processes.

You can use the native key to access system semaphores that have not been created by Qt, or to grant access to non-Qt applications. See `Native IPC Keys <https://doc.qt.io/qt-6/native-ipc-keys.html>`_ for more information.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSystemSemaphore.setNativeKey`.
