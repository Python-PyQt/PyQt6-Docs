.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 8f188293b7acaa2843bf123cf8f4cd99

Returns the legacy key assigned with :sip:ref:`~PyQt6.QtCore.QSharedMemory.setKey` to this shared memory, or a null key if no key has been assigned, or if the segment is using a :sip:ref:`~PyQt6.QtCore.QSharedMemory.nativeKey`. The key is the identifier used by Qt applications to identify the shared memory segment.

You can find the native, platform specific, key used by the operating system by calling :sip:ref:`~PyQt6.QtCore.QSharedMemory.nativeKey`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSharedMemory.setKey`, :sip:ref:`~PyQt6.QtCore.QSharedMemory.setNativeKey`.
