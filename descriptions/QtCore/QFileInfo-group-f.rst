.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: d8c627a7766e87734bb2c14abdcdcab4

Returns the group of the file. On Windows, on systems where files do not have groups, or if an error occurs, an empty string is returned.

This function can be time consuming under Unix (in the order of milliseconds).

If the file is a symlink, this function returns information about the target, not the symlink.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.groupId`, :sip:ref:`~PyQt6.QtCore.QFileInfo.owner`, :sip:ref:`~PyQt6.QtCore.QFileInfo.ownerId`.
