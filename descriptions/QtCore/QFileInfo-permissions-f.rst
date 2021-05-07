.. sip:method-description::
    :status: todo
    :pysig: 36080ac8dbb72076607a14924d2352db
    :realsig: () const
    :digest: 2dbbfb0ffa401b6b200ce46451675d1d

Returns the complete OR-ed together combination of QFile::Permissions for the file.

**Note:** The result might be inaccurate on Windows if the :ref:`NTFS permissions<qfileinfo-ntfs-permissions>` check has not been enabled.

If the file is a symlink, this function returns the permissions of the target (not the symlink).
