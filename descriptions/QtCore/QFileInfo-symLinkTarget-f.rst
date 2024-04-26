.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: c81592038b778ed90a3c72574744ff53

Returns the absolute path to the file or directory a symbolic link points to, or an empty string if the object isn't a symbolic link.

This name may not represent an existing file; it is only a string.

**Note:** :sip:ref:`~PyQt6.QtCore.QFileInfo.exists` returns ``true`` if the symlink points to an existing target, otherwise it returns ``false``.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.exists`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isSymLink`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isDir`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isFile`.
