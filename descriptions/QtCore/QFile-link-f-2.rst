.. sip:method-description::
    :status: todo
    :pysig: 1ab98a4411fb7d10d5134d664f82b37e
    :realsig: (const QString&)
    :digest: 1f893904f63bcec2152e141edfd551cc

Creates a link named *linkName* that points to the file currently specified by :sip:ref:`~PyQt6.QtCore.QFile.fileName`. What a link is depends on the underlying filesystem (be it a shortcut on Windows or a symbolic link on Unix). Returns ``true`` if successful; otherwise returns ``false``.

This function will not overwrite an already existing entity in the file system; in this case, ``link()`` will return false and set error() to return :sip:ref:`~PyQt6.QtCore.QFileDevice.FileError.RenameError`.

**Note:** To create a valid link on Windows, *linkName* must have a ``.lnk`` file extension.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFile.setFileName`.
