.. sip:method-description::
    :status: todo
    :pysig: f5f338b3e4bcd644a9a6ccfeb81d97ee
    :realsig: () const
    :digest: 2dbbfb0ffa401b6b200ce46451675d1d

Returns the complete OR-ed together combination of QFile::Permissions for the file.

**Note:** The result might be inaccurate on Windows if the :ref:`NTFS permissions<qfileinfo-ntfs-permissions>` check has not been enabled.

If the file is a symlink, this function returns the permissions of the target (not the symlink).
