.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: 13e8a03d1f5cc6bc7e12a6bbb130cecc

Sets the static portion of the file name to *name*. If the file template contains XXXXXX that will automatically be replaced with the unique part of the filename, otherwise a filename will be determined automatically based on the static portion specified.

If *name* contains a relative file path, the path will be relative to the current working directory. You can use :sip:ref:`~PyQt6.QtCore.QDir.tempPath` to construct *name* if you want use the system's temporary directory.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTemporaryFile.fileTemplate`.
