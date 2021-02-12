.. sip:method-description::
    :status: todo
    :pysig: bc433f34a736713d77fa06b4c6325f0a
    :realsig: (const QString&)
    :digest: 2beb30f4a97522d11f968904a635e051

Returns the absolute path of the file or directory referred to by the symlink (or shortcut on Windows) specified by *fileName*, or returns an empty string if the *fileName* does not correspond to a symbolic link.

This name may not represent an existing file; it is only a string. :sip:ref:`~PyQt6.QtCore.QFile.exists` returns ``true`` if the symlink points to an existing file.
