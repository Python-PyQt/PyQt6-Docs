.. sip:method-description::
    :status: todo
    :pysig: 1ab98a4411fb7d10d5134d664f82b37e
    :realsig: (const QString&)
    :digest: 04bfec61ea98a0937eaa64ae871c2fb3

Copies the file named :sip:ref:`~PyQt6.QtCore.QFile.fileName` to *newName*.

This file is closed before it is copied.

If the copied file is a symbolic link (symlink), the file it refers to is copied, not the link itself. With the exception of permissions, which are copied, no other file metadata is copied.

Returns ``true`` if successful; otherwise returns ``false``.

Note that if a file with the name *newName* already exists, copy() returns ``false``. This means :sip:ref:`~PyQt6.QtCore.QFile` will not overwrite it.

**Note:** On Android, this operation is not yet supported for ``content`` scheme URIs.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFile.setFileName`.
