.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 66a6c9d61b2d285d433a16e19c61f9c7

Returns the suffix (extension) of the file.

The suffix consists of all characters in the file after (but not including) the last '.'.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qfileinfo.py
    :lines: 140-141

The suffix of a file is computed equally on all platforms, independent of file naming conventions (e.g., ".bashrc" on Unix has an empty base name, and the suffix is "bashrc").

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.fileName`, :sip:ref:`~PyQt6.QtCore.QFileInfo.completeSuffix`, :sip:ref:`~PyQt6.QtCore.QFileInfo.baseName`, :sip:ref:`~PyQt6.QtCore.QFileInfo.completeBaseName`.
