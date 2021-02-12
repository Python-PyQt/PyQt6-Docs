.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 2f0ffc0736b726003836fbeb4f03a7db

Returns the path. This may contain symbolic links, but never contains redundant ".", ".." or multiple separators.

The returned path can be either absolute or relative (see :sip:ref:`~PyQt6.QtCore.QDir.setPath`).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir.setPath`, :sip:ref:`~PyQt6.QtCore.QDir.absolutePath`, :sip:ref:`~PyQt6.QtCore.QDir.exists`, :sip:ref:`~PyQt6.QtCore.QDir.cleanPath`, :sip:ref:`~PyQt6.QtCore.QDir.dirName`, :sip:ref:`~PyQt6.QtCore.QDir.absoluteFilePath`, :sip:ref:`~PyQt6.QtCore.QDir.toNativeSeparators`, :sip:ref:`~PyQt6.QtCore.QDir.makeAbsolute`.
