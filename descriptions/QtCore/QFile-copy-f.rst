.. sip:method-description::
    :status: todo
    :pysig: 9d2496c01394f04863ec354dfad3b4be
    :realsig: (const QString&)
    :digest: a0dadfb472d32aa5f783020f1030f075

Copies the file named :sip:ref:`~PyQt6.QtCore.QFile.fileName` to *newName*.

This file is closed before it is copied.

If the copied file is a symbolic link (symlink), the file it refers to is copied, not the link itself. With the exception of permissions, which are copied, no other file metadata is copied.

Returns ``true`` if successful; otherwise returns ``false``.

Note that if a file with the name *newName* already exists,  returns ``false``. This means :sip:ref:`~PyQt6.QtCore.QFile` will not overwrite it.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFile.setFileName`.
