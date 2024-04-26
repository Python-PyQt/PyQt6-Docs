.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 9c968e712569fa8ea305f9ae799bc9ea

Returns ``true`` if the user can read the file system entry this :sip:ref:`~PyQt6.QtCore.QFileInfo` refers to; otherwise returns ``false``.

If the file is a symlink, this function returns information about the target, not the symlink.

**Note:** If the :ref:`qfileinfo-ntfs-permissions` check has not been enabled, the result on Windows will merely reflect whether the entry exists.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.isWritable`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isExecutable`, :sip:ref:`~PyQt6.QtCore.QFileInfo.permission`.
