.. sip:method-description::
    :status: todo
    :pysig: cb88e6482ff2daba05a75da39bcb15b7
    :realsig: (int,QIODeviceBase::OpenMode,QFileDevice::FileHandleFlags)
    :digest: 0dac7e54d2d1820e73535555cd9218e3

This is an overloaded function.

Opens the existing file descriptor *fd* in the given *mode*. *handleFlags* may be used to specify additional options. Returns ``true`` if successful; otherwise returns ``false``.

When a :sip:ref:`~PyQt6.QtCore.QFile` is opened using this function, behaviour of close() is controlled by the :sip:ref:`~PyQt6.QtCore.QFileDevice.FileHandleFlags.AutoCloseHandle` flag. If :sip:ref:`~PyQt6.QtCore.QFileDevice.FileHandleFlags.AutoCloseHandle` is specified, and this function succeeds, then calling close() closes the adopted handle. Otherwise, close() does not actually close the file, but only flushes it.

**Warning:** If *fd* is not a regular file, e.g, it is 0 (``stdin``), 1 (``stdout``), or 2 (``stderr``), you may not be able to seek(). In those cases, :sip:ref:`~PyQt6.QtCore.QFile.size` returns ``0``. See :sip:ref:`~PyQt6.QtCore.QIODevice.isSequential` for more information.

**Warning:** Since this function opens the file without specifying the file name, you cannot use this :sip:ref:`~PyQt6.QtCore.QFile` with a :sip:ref:`~PyQt6.QtCore.QFileInfo`.

.. seealso:: close().
