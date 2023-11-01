.. sip:method-description::
    :status: todo
    :pysig: 2574b10d9e98d37adb00c2946608eaf3
    :realsig: (qsizetype,QSharedMemory::AccessMode)
    :digest: 6c973818ba6812ea3d9c9aea42897f64

Creates a shared memory segment of *size* bytes with the key passed to the constructor or set with :sip:ref:`~PyQt6.QtCore.QSharedMemory.setNativeKey`, then attaches to the new shared memory segment with the given access *mode* and returns ``true``. If a shared memory segment identified by the key already exists, the attach operation is not performed and ``false`` is returned. When the return value is ``false``, call :sip:ref:`~PyQt6.QtCore.QSharedMemory.error` to determine which error occurred.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSharedMemory.error`.
