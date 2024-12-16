.. sip:method-description::
    :status: todo
    :pysig: 25da2ff90bbe6956177b7ded744e49b8
    :realsig: (int,QIODeviceBase::OpenMode,QFileDevice::FileHandleFlags)
    :digest: 7c019eb79e170e595198c3f92825a374

This is an overloaded function.

Opens the existing file descriptor *fd* in the given *mode*. *handleFlags* may be used to specify additional options. Returns ``true`` if successful; otherwise returns ``false``.

When a :sip:ref:`~PyQt6.QtCore.QFile` is opened using this function, behaviour of close() is controlled by the AutoCloseHandle flag. If AutoCloseHandle is specified, and this function succeeds, then calling close() closes the adopted handle. Otherwise, close() does not actually close the file, but only flushes it.

**Warning:** If *fd* is not a regular file, e.g, it is 0 (``stdin``), 1 (``stdout``), or 2 (``stderr``), you may not be able to seek(). In those cases, :sip:ref:`~PyQt6.QtCore.QFile.size` returns ``0``. See :sip:ref:`~PyQt6.QtCore.QIODevice.isSequential` for more information.

**Warning:** Since this function opens the file without specifying the file name, you cannot use this :sip:ref:`~PyQt6.QtCore.QFile` with a :sip:ref:`~PyQt6.QtCore.QFileInfo`.

.. seealso:: close(), QT_USE_NODISCARD_FILE_OPEN.
