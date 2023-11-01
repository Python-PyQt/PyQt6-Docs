.. sip:method-description::
    :status: todo
    :pysig: 1ab98a4411fb7d10d5134d664f82b37e
    :realsig: (const QString&)
    :digest: 0dadb4125b808ce04427635dd5c843a1

Renames the file currently specified by :sip:ref:`~PyQt6.QtCore.QFile.fileName` to *newName*. Returns ``true`` if successful; otherwise returns ``false``.

If a file with the name *newName* already exists, rename() returns ``false`` (i.e., :sip:ref:`~PyQt6.QtCore.QFile` will not overwrite it).

The file is closed before it is renamed.

If the rename operation fails, Qt will attempt to copy this file's contents to *newName*, and then remove this file, keeping only *newName*. If that copy operation fails or this file can't be removed, the destination file *newName* is removed to restore the old state.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFile.setFileName`.
