.. sip:method-description::
    :status: todo
    :pysig: 4fa0960f626986883b81c619e8915efb
    :realsig: (const QString&) const
    :digest: 999a5d05a651df754ed402d4dce93faf

Returns the path name of a file in the temporary directory. Does *not* check if the file actually exists in the directory. Redundant multiple separators or "." and ".." directories in *fileName* are not removed (see :sip:ref:`~PyQt6.QtCore.QDir.cleanPath`). Absolute paths are not allowed.
