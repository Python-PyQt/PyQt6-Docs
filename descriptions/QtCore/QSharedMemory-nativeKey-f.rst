.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: a380c1f0bf9860fd49abb3ff9bdad2af

Returns the native, platform specific, key for this shared memory object. The native key is the identifier used by the operating system to identify the shared memory segment.

You can use the native key to access shared memory segments that have not been created by Qt, or to grant shared memory access to non-Qt applications. See `Native IPC Keys <https://doc.qt.io/qt-6/native-ipc-keys.html>`_ for more information.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSharedMemory.setNativeKey`, :sip:ref:`~PyQt6.QtCore.QSharedMemory.nativeIpcKey`.
