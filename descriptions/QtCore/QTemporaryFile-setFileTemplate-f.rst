.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: 789dad9882b75bc44b57af5191cf3736

Sets the static portion of the file name to *name*. If the file template contains XXXXXX that will automatically be replaced with the unique part of the filename, otherwise a filename will be determined automatically based on the static portion specified.

If *name* contains a relative file path, the path will be relative to the current working directory. You can use :sip:ref:`~PyQt6.QtCore.QDir.tempPath` to construct *name* if you want use the system's temporary directory. It is important to specify the correct directory if the :sip:ref:`~PyQt6.QtCore.QTemporaryFile.rename` function will be called, as :sip:ref:`~PyQt6.QtCore.QTemporaryFile` can only rename files within the same volume / filesystem as the temporary file itself was created on.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTemporaryFile.fileTemplate`.
