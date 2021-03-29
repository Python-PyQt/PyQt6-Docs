.. sip:method-description::
    :status: todo
    :pysig: 787ad3d0f6e2063950bbbf6e050908f3
    :realsig: (const QString&)
    :digest: 971763057775da6fe20e7f3a2adbc02c

Returns ``true`` if the *file* exists; otherwise returns ``false``.

**Note:** If *file* is a symlink that points to a non-existing file, false is returned.

**Note:** Using this function is faster than using ``QFileInfo(file).exists()`` for file system access.
