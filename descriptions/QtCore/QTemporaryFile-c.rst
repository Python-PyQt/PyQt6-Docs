.. sip:class-description::
    :status: todo
    :brief: I/O device that operates on temporary files
    :digest: bac632be6396f1d1897f85ec4e1b446b

The :sip:ref:`~PyQt6.QtCore.QTemporaryFile` class is an I/O device that operates on temporary files.

:sip:ref:`~PyQt6.QtCore.QTemporaryFile` is used to create unique temporary files safely. The file itself is created by calling :sip:ref:`~PyQt6.QtCore.QTemporaryFile.open`. The name of the temporary file is guaranteed to be unique (i.e., you are guaranteed to not overwrite an existing file), and the file will subsequently be removed upon destruction of the :sip:ref:`~PyQt6.QtCore.QTemporaryFile` object. This is an important technique that avoids data corruption for applications that store data in temporary files. The file name is either auto-generated, or created based on a template, which is passed to :sip:ref:`~PyQt6.QtCore.QTemporaryFile`'s constructor.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qtemporaryfile.py
    :lines: 55-63

Reopening a :sip:ref:`~PyQt6.QtCore.QTemporaryFile` after calling close() is safe. For as long as the :sip:ref:`~PyQt6.QtCore.QTemporaryFile` object itself is not destroyed, the unique temporary file will exist and be kept open internally by :sip:ref:`~PyQt6.QtCore.QTemporaryFile`.

The file name of the temporary file can be found by calling :sip:ref:`~PyQt6.QtCore.QTemporaryFile.fileName`. Note that this is only defined after the file is first opened; the function returns an empty string before this.

A temporary file will have some static part of the name and some part that is calculated to be unique. The default filename will be determined from :sip:ref:`~PyQt6.QtCore.QCoreApplication.applicationName` (otherwise ``qt_temp``) and will be placed into the temporary path as returned by :sip:ref:`~PyQt6.QtCore.QDir.tempPath`. If you specify your own filename, a relative file path will not be placed in the temporary directory by default, but be relative to the current working directory. It is important to specify the correct directory if the :sip:ref:`~PyQt6.QtCore.QTemporaryFile.rename` function will be called, as :sip:ref:`~PyQt6.QtCore.QTemporaryFile` can only rename files within the same volume / filesystem as the temporary file itself was created on.

Specified filenames can contain the following template ``XXXXXX`` (six upper case "X" characters), which will be replaced by the auto-generated portion of the filename. Note that the template is case sensitive. If the template is not present in the filename, :sip:ref:`~PyQt6.QtCore.QTemporaryFile` appends the generated part to the filename given.

**Note:** On Linux, :sip:ref:`~PyQt6.QtCore.QTemporaryFile` will attempt to create unnamed temporary files. If that succeeds, :sip:ref:`~PyQt6.QtCore.QTemporaryFile.open` will return true but exists() will be false. If you call :sip:ref:`~PyQt6.QtCore.QTemporaryFile.fileName` or any function that calls it, :sip:ref:`~PyQt6.QtCore.QTemporaryFile` will give the file a name, so most applications will not see a difference.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir.tempPath`, :sip:ref:`~PyQt6.QtCore.QFile`.
