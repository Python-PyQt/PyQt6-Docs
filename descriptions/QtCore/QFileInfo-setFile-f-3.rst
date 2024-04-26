.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: f76c77f577790564c9f1777ae51ec9e9

Sets the path of the file system entry that this :sip:ref:`~PyQt6.QtCore.QFileInfo` provides information about to *path* that can be absolute or relative.

On Unix, absolute paths begin with the directory separator ``'/'``. On Windows, absolute paths begin with a drive specification (for example, ``D:/``).

Relative paths begin with a directory name or a regular file name and specify a file system entry's path relative to the current working directory.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qfileinfo.py
    :lines: 95-105

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.isFile`, :sip:ref:`~PyQt6.QtCore.QFileInfo.isRelative`, :sip:ref:`~PyQt6.QtCore.QDir.setCurrent`, :sip:ref:`~PyQt6.QtCore.QDir.isRelativePath`.
