.. sip:method-description::
    :status: todo
    :pysig: 4fa0960f626986883b81c619e8915efb
    :realsig: (const QString&) const
    :digest: d6ea71fcb57b7ea696994f3163378fb8

Returns the path name of a file in the temporary directory. Does *not* check if the file actually exists in the directory. Redundant multiple separators or "." and ".." directories in *fileName* are not removed (see :sip:ref:`~PyQt6.QtCore.QDir.cleanPath`). Absolute paths are not allowed.

The returned path will be relative or absolulte depending on whether :sip:ref:`~PyQt6.QtCore.QTemporaryDir` was constructed with a relative or absolute path, respectively.
