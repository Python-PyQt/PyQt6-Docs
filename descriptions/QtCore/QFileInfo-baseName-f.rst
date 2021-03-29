.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 3837c07ed1dd1037f2b8899aeb5ee4c2

Returns the base name of the file without the path.

The base name consists of all characters in the file up to (but not including) the *first* '.' character.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qfileinfo.py
    :lines: 122-123

The base name of a file is computed equally on all platforms, independent of file naming conventions (e.g., ".bashrc" on Unix has an empty base name, and the suffix is "bashrc").

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.fileName`, :sip:ref:`~PyQt6.QtCore.QFileInfo.suffix`, :sip:ref:`~PyQt6.QtCore.QFileInfo.completeSuffix`, :sip:ref:`~PyQt6.QtCore.QFileInfo.completeBaseName`.
