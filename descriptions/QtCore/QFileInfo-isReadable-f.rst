.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: afd6773cd78bebda1d8fc2001d7c4a7a

Returns ``true`` if the user can read the file; otherwise returns ``false``.

If the file is a symlink, this function returns true if the target is readable (not the symlink).

**Note:** If the :ref:`NTFS permissions<qfileinfo-ntfs-permissions>` check has not been enabled, the result on Windows will merely reflect whether the file exists.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.isWritable`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isExecutable`, :sip:ref:`~PyQt6.QtCore.QFileInfo.permission`.
