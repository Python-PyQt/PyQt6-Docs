.. sip:method-description::
    :status: todo
    :pysig: 558877a2dde966820eb6e4a9d974f77b
    :realsig: (const QString&) const
    :digest: 92a9b957529f333dc53705055c677a6a

Returns the path name of a file in the directory. Does *not* check if the file actually exists in the directory; but see :sip:ref:`~PyQt6.QtCore.QDir.exists`. If the :sip:ref:`~PyQt6.QtCore.QDir` is relative the returned path name will also be relative. Redundant multiple separators or "." and ".." directories in *fileName* are not removed (see :sip:ref:`~PyQt6.QtCore.QDir.cleanPath`).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir.dirName`, :sip:ref:`~PyQt6.QtCore.QDir.absoluteFilePath`, :sip:ref:`~PyQt6.QtCore.QDir.isRelative`, :sip:ref:`~PyQt6.QtCore.QDir.canonicalPath`.
