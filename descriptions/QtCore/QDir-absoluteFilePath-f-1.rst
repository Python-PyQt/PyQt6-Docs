.. sip:method-description::
    :status: todo
    :pysig: 4fa0960f626986883b81c619e8915efb
    :realsig: (const QString&) const
    :digest: 5231857d66eba03f333f604b79d37cce

Returns the absolute path name of a file in the directory. Does *not* check if the file actually exists in the directory; but see :sip:ref:`~PyQt6.QtCore.QDir.exists`. Redundant multiple separators or "." and ".." directories in *fileName* are not removed (see :sip:ref:`~PyQt6.QtCore.QDir.cleanPath`).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir.relativeFilePath`, :sip:ref:`~PyQt6.QtCore.QDir.filePath`, :sip:ref:`~PyQt6.QtCore.QDir.canonicalPath`.
