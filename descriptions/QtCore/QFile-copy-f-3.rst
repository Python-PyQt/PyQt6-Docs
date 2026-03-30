.. sip:method-description::
    :status: todo
    :pysig: 036e9c2cff75e17278911a538a7e62f1
    :realsig: (const QString&, const QString&)
    :digest: 5eb24f24c66f6d15695a94fe2f56b97c

Copies the file named *fileName* to *newName*.

If the copied file is a symbolic link (symlink), the file it refers to is copied, not the link itself. With the exception of permissions, which are copied, no other file metadata is copied.

Returns ``true`` if successful; otherwise returns ``false``.

Note that if a file with the name *newName* already exists, :sip:ref:`~PyQt6.QtCore.QFile.copy` returns ``false``. This means :sip:ref:`~PyQt6.QtCore.QFile` will not overwrite it.

**Note:** On Android, this operation is not yet supported for ``content`` scheme URIs.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFile.rename`.
