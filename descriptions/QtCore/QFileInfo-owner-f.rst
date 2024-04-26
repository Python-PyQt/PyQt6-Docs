.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: eb72fa190dbf9cf1315bba215919a745

Returns the owner of the file. On systems where files do not have owners, or if an error occurs, an empty string is returned.

This function can be time consuming under Unix (in the order of milliseconds). On Windows, it will return an empty string unless the :ref:`qfileinfo-ntfs-permissions` check has been enabled.

If the file is a symlink, this function returns information about the target, not the symlink.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.ownerId`, :sip:ref:`~PyQt6.QtCore.QFileInfo.group`, :sip:ref:`~PyQt6.QtCore.QFileInfo.groupId`.
