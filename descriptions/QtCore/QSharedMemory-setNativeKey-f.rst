.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: d89a0a7caac3ce7451fdf8c0c2553734

Sets the native, platform specific, *key* for this shared memory object. If *key* is the same as the current native key, the function returns without doing anything. If all you want is to assign a key to a segment, you should call :sip:ref:`~PyQt6.QtCore.QSharedMemory.setKey` instead.

You can call :sip:ref:`~PyQt6.QtCore.QSharedMemory.nativeKey` to retrieve the native key. If a native key has been assigned, calling :sip:ref:`~PyQt6.QtCore.QSharedMemory.key` will return a null string.

If the shared memory object is attached to an underlying shared memory segment, it will :sip:ref:`~PyQt6.QtCore.QSharedMemory.detach` from it before setting the new key. This function does not do an :sip:ref:`~PyQt6.QtCore.QSharedMemory.attach`.

The application will not be portable if you set a native key.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSharedMemory.nativeKey`, :sip:ref:`~PyQt6.QtCore.QSharedMemory.key`, :sip:ref:`~PyQt6.QtCore.QSharedMemory.isAttached`.
