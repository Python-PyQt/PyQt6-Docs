.. sip:method-description::
    :status: todo
    :pysig: 66883c67b8346c29659446e444062f18
    :realsig: (const QNativeIpcKey&)
    :digest: 4bbecf180bef3b786938438a5057e170

Sets the native, platform specific, *key* for this shared memory object. If *key* is the same as the current native key, the function returns without doing anything. Otherwise, if the shared memory object is attached to an underlying shared memory segment, it will :sip:ref:`~PyQt6.QtCore.QSharedMemory.detach` from it before setting the new key. This function does not do an :sip:ref:`~PyQt6.QtCore.QSharedMemory.attach`.

This function is useful if the native key was shared from another process. See `Native IPC Keys <https://doc.qt.io/qt-6/native-ipc-keys.html>`_ for more information.

Portable native keys can be obtained using platformSafeKey().

You can call :sip:ref:`~PyQt6.QtCore.QSharedMemory.nativeKey` to retrieve the native key.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSharedMemory.nativeKey`, :sip:ref:`~PyQt6.QtCore.QSharedMemory.nativeIpcKey`, :sip:ref:`~PyQt6.QtCore.QSharedMemory.isAttached`.
