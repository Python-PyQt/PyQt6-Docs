.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: f57e81e026bfd22ee789e670a81b0a50

Returns the key assigned with :sip:ref:`~PyQt6.QtCore.QSharedMemory.setKey` to this shared memory, or a null key if no key has been assigned, or if the segment is using a :sip:ref:`~PyQt6.QtCore.QSharedMemory.nativeKey`. The key is the identifier used by Qt applications to identify the shared memory segment.

You can find the native, platform specific, key used by the operating system by calling :sip:ref:`~PyQt6.QtCore.QSharedMemory.nativeKey`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSharedMemory.setKey`, :sip:ref:`~PyQt6.QtCore.QSharedMemory.setNativeKey`.
