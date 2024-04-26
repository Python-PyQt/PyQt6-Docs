.. sip:method-description::
    :status: todo
    :pysig: f5f338b3e4bcd644a9a6ccfeb81d97ee
    :realsig: () const
    :digest: df7138842d8a8eaa2e2c00e0e22812d5

Returns the complete OR-ed together combination of QFile::Permissions for the file.

**Note:** The result might be inaccurate on Windows if the :ref:`qfileinfo-ntfs-permissions` check has not been enabled.

If the file is a symlink, this function returns information about the target, not the symlink.
