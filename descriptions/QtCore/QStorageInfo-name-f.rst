.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: cd6893c950100afbb6f9bbe030c8a804

Returns the human-readable name of a filesystem, usually called ``label``.

Not all filesystems support this feature. In this case, the value returned by this method could be empty. An empty string is returned if the file system does not support labels, or if no label is set.

On Linux, retrieving the volume's label requires ``udev`` to be present in the system.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QStorageInfo.fileSystemType`.
