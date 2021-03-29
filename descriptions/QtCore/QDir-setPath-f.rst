.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: af5ef3f0088297c2a47ea686da17ec0c

Sets the path of the directory to *path*. The path is cleaned of redundant ".", ".." and of multiple separators. No check is made to see whether a directory with this path actually exists; but you can check for yourself using :sip:ref:`~PyQt6.QtCore.QDir.exists`.

The path can be either absolute or relative. Absolute paths begin with the directory separator "/" (optionally preceded by a drive specification under Windows). Relative file names begin with a directory name or a file name and specify a path relative to the current directory. An example of an absolute path is the string "/tmp/quartz", a relative path might look like "src/fatlib".

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir.path`, :sip:ref:`~PyQt6.QtCore.QDir.absolutePath`, :sip:ref:`~PyQt6.QtCore.QDir.exists`, :sip:ref:`~PyQt6.QtCore.QDir.cleanPath`, :sip:ref:`~PyQt6.QtCore.QDir.dirName`, :sip:ref:`~PyQt6.QtCore.QDir.absoluteFilePath`, :sip:ref:`~PyQt6.QtCore.QDir.isRelative`, :sip:ref:`~PyQt6.QtCore.QDir.makeAbsolute`.
