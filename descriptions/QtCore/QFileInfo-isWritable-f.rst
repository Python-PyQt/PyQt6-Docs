.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 54633ded330a60fa3a8ce6dc97f855ff

Returns ``true`` if the user can write to the file; otherwise returns ``false``.

If the file is a symlink, this function returns true if the target is writeable (not the symlink).

**Note:** If the :ref:`NTFS permissions<qfileinfo-ntfs-permissions>` check has not been enabled, the result on Windows will merely reflect whether the file is marked as Read Only.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.isReadable`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isExecutable`, :sip:ref:`~PyQt6.QtCore.QFileInfo.permission`.
