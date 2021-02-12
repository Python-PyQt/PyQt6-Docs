.. sip:method-description::
    :status: todo
    :pysig: 8b05429aed100b36ea75598ca87299a0
    :realsig: (QSharedMemory::AccessMode)
    :digest: 49c8b087c45befbd08fb530ad54bf98e

Attempts to attach the process to the shared memory segment identified by the key that was passed to the constructor or to a call to :sip:ref:`~PyQt6.QtCore.QSharedMemory.setKey` or :sip:ref:`~PyQt6.QtCore.QSharedMemory.setNativeKey`. The access *mode* is :sip:ref:`~PyQt6.QtCore.QSharedMemory.AccessMode.ReadWrite` by default. It can also be :sip:ref:`~PyQt6.QtCore.QSharedMemory.AccessMode.ReadOnly`. Returns ``true`` if the attach operation is successful. If false is returned, call :sip:ref:`~PyQt6.QtCore.QSharedMemory.error` to determine which error occurred. After attaching the shared memory segment, a pointer to the shared memory can be obtained by calling :sip:ref:`~PyQt6.QtCore.QSharedMemory.data`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSharedMemory.isAttached`, :sip:ref:`~PyQt6.QtCore.QSharedMemory.detach`, :sip:ref:`~PyQt6.QtCore.QSharedMemory.create`.
