.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: b20ed9530cc344085f6288dbc9ef61af

Returns the canonical path including the file name, i.e. an absolute path without symbolic links or redundant "." or ".." elements.

If the file does not exist, canonicalFilePath() returns an empty string.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.filePath`, :sip:ref:`~PyQt6.QtCore.QFileInfo.absoluteFilePath`, :sip:ref:`~PyQt6.QtCore.QFileInfo.dir`.
