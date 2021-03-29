.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 1fbe7ed20c056455d9d2f67e9142238f

Returns the native, platform specific, key for this shared memory object. The native key is the identifier used by the operating system to identify the shared memory segment.

You can use the native key to access shared memory segments that have not been created by Qt, or to grant shared memory access to non-Qt applications.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSharedMemory.setKey`, :sip:ref:`~PyQt6.QtCore.QSharedMemory.setNativeKey`.
