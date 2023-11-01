.. sip:method-description::
    :status: todo
    :pysig: 5ae4df144bb6014c3175a8eeb873f7f7
    :realsig: (const QString&)
    :digest: 2beb30f4a97522d11f968904a635e051

Returns the absolute path of the file or directory referred to by the symlink (or shortcut on Windows) specified by *fileName*, or returns an empty string if the *fileName* does not correspond to a symbolic link.

This name may not represent an existing file; it is only a string. :sip:ref:`~PyQt6.QtCore.QFile.exists` returns ``true`` if the symlink points to an existing file.
