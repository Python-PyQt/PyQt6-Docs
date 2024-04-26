.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 7f2a13d8d46362bc792cfa439a72420c

Returns ``true`` if the user can write to the file system entry this :sip:ref:`~PyQt6.QtCore.QFileInfo` refers to; otherwise returns ``false``.

If the file is a symlink, this function returns information about the target, not the symlink.

**Note:** If the :ref:`qfileinfo-ntfs-permissions` check has not been enabled, the result on Windows will merely reflect whether the entry is marked as Read Only.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.isReadable`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isExecutable`, :sip:ref:`~PyQt6.QtCore.QFileInfo.permission`.
