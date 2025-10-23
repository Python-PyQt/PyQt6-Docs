.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: b750a7ded4c54634367212a182d0d34c

Returns the absolute path of the file or directory a symlink (or shortcut on Windows) points to, or a an empty string if the object isn't a symbolic link.

This name may not represent an existing file; it is only a string. :sip:ref:`~PyQt6.QtCore.QFile.exists` returns ``true`` if the symlink points to an existing file.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFile.fileName`, :sip:ref:`~PyQt6.QtCore.QFile.setFileName`.
