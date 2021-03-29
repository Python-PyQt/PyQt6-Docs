.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 1c0b81e41c2923ad9193b3abf7c97f3f

Returns the group of the file. On Windows, on systems where files do not have groups, or if an error occurs, an empty string is returned.

This function can be time consuming under Unix (in the order of milliseconds).

If the file is a symlink, this function returns the owning group of the target (not the symlink).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.groupId`, :sip:ref:`~PyQt6.QtCore.QFileInfo.owner`, :sip:ref:`~PyQt6.QtCore.QFileInfo.ownerId`.
