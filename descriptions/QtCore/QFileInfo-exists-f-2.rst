.. sip:method-description::
    :status: todo
    :pysig: dd431a34e6382be8567cf5b44f2db6a6
    :realsig: (const QString&)
    :digest: 971763057775da6fe20e7f3a2adbc02c

Returns ``true`` if the *file* exists; otherwise returns ``false``.

**Note:** If *file* is a symlink that points to a non-existing file, false is returned.

**Note:** Using this function is faster than using ``QFileInfo(file).exists()`` for file system access.
