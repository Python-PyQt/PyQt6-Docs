.. sip:method-description::
    :status: todo
    :pysig: 00c0a76926beac9cc58a7342efe189f6
    :realsig: (const QString&, QNativeIpcKey::Type)
    :digest: 8cf4a05977991f01d66ee57389053e32

Sets the native, platform specific, *key* for this shared memory object of type *type* (the type parameter has been available since Qt 6.6). If *key* is the same as the current native key, the function returns without doing anything. Otherwise, if the shared memory object is attached to an underlying shared memory segment, it will :sip:ref:`~PyQt6.QtCore.QSharedMemory.detach` from it before setting the new key. This function does not do an :sip:ref:`~PyQt6.QtCore.QSharedMemory.attach`.

This function is useful if the native key was shared from another process, though the application must take care to ensure the key type matches what the other process expects. See `Native IPC Keys <https://doc.qt.io/qt-6/native-ipc-keys.html>`_ for more information.

Portable native keys can be obtained using platformSafeKey().

You can call :sip:ref:`~PyQt6.QtCore.QSharedMemory.nativeKey` to retrieve the native key.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSharedMemory.nativeKey`, :sip:ref:`~PyQt6.QtCore.QSharedMemory.nativeIpcKey`, :sip:ref:`~PyQt6.QtCore.QSharedMemory.isAttached`.
