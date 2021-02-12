.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: 51235612d8674f4434b3d9eff83252e0

Sets the platform independent *key* for this shared memory object. If *key* is the same as the current key, the function returns without doing anything.

You can call :sip:ref:`~PyQt6.QtCore.QSharedMemory.key` to retrieve the platform independent key. Internally, :sip:ref:`~PyQt6.QtCore.QSharedMemory` converts this key into a platform specific key. If you instead call :sip:ref:`~PyQt6.QtCore.QSharedMemory.nativeKey`, you will get the platform specific, converted key.

If the shared memory object is attached to an underlying shared memory segment, it will :sip:ref:`~PyQt6.QtCore.QSharedMemory.detach` from it before setting the new key. This function does not do an :sip:ref:`~PyQt6.QtCore.QSharedMemory.attach`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSharedMemory.key`, :sip:ref:`~PyQt6.QtCore.QSharedMemory.nativeKey`, :sip:ref:`~PyQt6.QtCore.QSharedMemory.isAttached`.
