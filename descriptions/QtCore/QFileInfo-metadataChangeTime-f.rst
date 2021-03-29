.. sip:method-description::
    :status: todo
    :pysig: 5e7341bb4cec52d103c2b47c3fb7247a
    :realsig: () const
    :digest: cea2ee67f62f2a74ebd943d2897a01ac

Returns the date and time when the file metadata was changed. A metadata change occurs when the file is created, but it also occurs whenever the user writes or sets inode information (for example, changing the file permissions).

If the file is a symlink, the time of the target file is returned (not the symlink).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.lastModified`, :sip:ref:`~PyQt6.QtCore.QFileInfo.lastRead`.
