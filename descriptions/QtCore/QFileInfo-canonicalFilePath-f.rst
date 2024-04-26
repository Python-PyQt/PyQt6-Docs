.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: fb47ea21ccfd1a482506b3a03a565b07

Returns the file system entry's canonical path, including the entry's name, that is, an absolute path without symbolic links or redundant ``'.'`` or ``'..'`` elements.

If the entry does not exist, canonicalFilePath() returns an empty string.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileInfo.filePath`, :sip:ref:`~PyQt6.QtCore.QFileInfo.absoluteFilePath`, :sip:ref:`~PyQt6.QtCore.QFileInfo.dir`.
