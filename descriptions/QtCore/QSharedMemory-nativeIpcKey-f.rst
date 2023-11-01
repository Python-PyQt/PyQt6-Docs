.. sip:method-description::
    :status: todo
    :pysig: 66883c67b8346c29659446e444062f18
    :realsig: () const
    :digest: 7c60cddcf1249f72e69fa8b43d46aa2f

Returns the key type for this shared memory object. The key type complements the :sip:ref:`~PyQt6.QtCore.QSharedMemory.nativeKey` as the identifier used by the operating system to identify the shared memory segment.

You can use the native key to access shared memory segments that have not been created by Qt, or to grant shared memory access to non-Qt applications. See `Native IPC Keys <https://doc.qt.io/qt-6/native-ipc-keys.html>`_ for more information.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSharedMemory.nativeKey`, :sip:ref:`~PyQt6.QtCore.QSharedMemory.setNativeKey`.
