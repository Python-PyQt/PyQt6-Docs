.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: e8886c0b6f602ff70b95fedc9a53f2a6

This is an overloaded function.

Sets the legacy *key* for this shared memory object. If *key* is the same as the current key, the function returns without doing anything. Otherwise, if the shared memory object is attached to an underlying shared memory segment, it will :sip:ref:`~PyQt6.QtCore.QSharedMemory.detach` from it before setting the new key. This function does not do an :sip:ref:`~PyQt6.QtCore.QSharedMemory.attach`.

You can call :sip:ref:`~PyQt6.QtCore.QSharedMemory.key` to retrieve the legacy key. This function is mostly the same as:

::

    shm.setNativeKey(QSharedMemory::legacyNativeKey(key));

except that it enables obtaining the legacy key using :sip:ref:`~PyQt6.QtCore.QSharedMemory.key`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSharedMemory.key`, :sip:ref:`~PyQt6.QtCore.QSharedMemory.nativeKey`, :sip:ref:`~PyQt6.QtCore.QSharedMemory.isAttached`.
